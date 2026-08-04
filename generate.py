#!/usr/bin/env python3
"""
Generates the DetectOps MkDocs product-documentation site from
detectops-manifest.html + the screenshot set at ~/detectops-shots/.

Re-run this any time the manifest or screenshots change; it fully
regenerates docs/tools/** (safe to delete and rebuild), but leaves
hand-written pages (index.md, getting-started.md, etc.) alone.
"""
import os
import re
import shutil
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = Path(__file__).parent
MANIFEST = ROOT.parent / "detectops-manifest.html"
SHOTS_PNG = Path.home() / "detectops-shots" / "png"
SHOTS_INDEX = Path.home() / "detectops-shots" / "INDEX.md"
DOCS = ROOT / "docs"
TOOLS_DIR = DOCS / "tools"
SHOT_DEST = DOCS / "assets" / "screenshots"

CAT_COLORS = {
    1: "#D9724C", 2: "#4CA593", 3: "#9689D6", 4: "#5B9BD5", 5: "#7CAE72",
    6: "#B478A6", 7: "#8291B8", 8: "#4FB4BE", 9: "#C2A544", 10: "#C6768E",
}


def slugify(text):
    text = re.sub(r"&amp;", "and", text)
    text = re.sub(r"[^\w\s-]", "", text.lower())
    text = re.sub(r"[\s_]+", "-", text).strip("-")
    return text


def inline_to_md(node):
    """Convert a BeautifulSoup inline fragment (code/a/b/span/text) to Markdown."""
    out = []
    for child in node.children:
        if isinstance(child, NavigableString):
            out.append(str(child))
        elif isinstance(child, Tag):
            if child.name == "code":
                out.append(f"`{child.get_text()}`")
            elif child.name == "a":
                href = child.get("href", "")
                out.append(f"[{child.get_text()}]({href})")
            elif child.name == "b":
                out.append(f"**{inline_to_md(child)}**")
            else:
                out.append(inline_to_md(child))
    text = "".join(out)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def parse_manifest():
    soup = BeautifulSoup(MANIFEST.read_text(), "html.parser")
    categories = []
    for sec in soup.select("section.category"):
        num = int(sec.select_one(".cat-num").get_text())
        name = sec.select_one(".cat-head h2").get_text()
        blurb = sec.select_one(".cat-blurb").get_text().strip()
        entries = []
        for entry in sec.select(".entry"):
            name_row = entry.select_one(".name-row")
            tool_name = name_row.select_one(".name").get_text().strip()
            tags = name_row.select("span.tag")
            is_new = any("new" in (t.get("class") or []) for t in tags)
            main_tag = tags[0].get_text().strip() if tags else ""

            desc_el = entry.select_one(".desc")
            desc = inline_to_md(desc_el) if desc_el else ""

            path_md, run_code, notes = None, None, []
            for field in entry.select(".how > .field"):
                label = field.select_one(".flabel").get_text().strip()
                if label == "path":
                    clone = BeautifulSoup(str(field), "html.parser")
                    clone.find(class_="flabel").decompose()
                    path_md = inline_to_md(clone.div)
                elif label == "run":
                    pre = field.select_one("pre")
                    run_code = pre.get_text() if pre else ""
            for note in entry.select(".how > .note"):
                classes = note.get("class") or []
                kind = "manual" if "manual" in classes else ("win" if "win" in classes else "plain")
                notes.append((kind, inline_to_md(note)))

            entries.append({
                "name": tool_name,
                "tag": main_tag,
                "new": is_new,
                "desc": desc,
                "path": path_md,
                "run": run_code,
                "notes": notes,
                "slug": slugify(tool_name),
            })
        categories.append({
            "num": num, "name": name, "blurb": blurb,
            "slug": slugify(name), "entries": entries,
        })
    return categories


def parse_screenshot_index():
    """Returns {category_name: [png_relpath, ...]} in on-page order."""
    text = SHOTS_INDEX.read_text()
    sections = re.split(r"^## (.+)$", text, flags=re.M)[1:]
    result = {}
    for i in range(0, len(sections), 2):
        cat_name = sections[i].strip()
        body = sections[i + 1]
        pngs = re.findall(r"`(png/[^`]+\.png)`", body)
        result[cat_name] = pngs
    return result


def render_note(kind, text):
    if kind == "manual":
        return f'!!! warning "Manual step required"\n    {text}\n'
    if kind == "win":
        return f'!!! info "Windows-only"\n    {text}\n'
    return f'!!! note\n    {text}\n'


def write_tool_page(cat, entry, shot_rel):
    badge = f'<span class="cat-badge" style="background:{CAT_COLORS[cat["num"]]}">{entry["tag"]}</span>'
    if entry["new"]:
        badge += ' <span class="new-badge">NEW</span>'

    lines = [
        f'# {entry["name"]}',
        "",
        badge,
        "",
        entry["desc"],
        "",
    ]

    if shot_rel:
        lines += [f'![{entry["name"]} screenshot](../../assets/screenshots/{shot_rel})', ""]

    if entry["path"]:
        lines += ["## Location", "", entry["path"], ""]

    if entry["run"]:
        lines += ["## How to run", "", "```bash", entry["run"].rstrip("\n"), "```", ""]

    for kind, text in entry["notes"]:
        lines += [render_note(kind, text), ""]

    lines += [
        "---",
        "",
        f'*Part of the **{cat["name"]}** toolset in DetectOps.*',
    ]
    path = TOOLS_DIR / cat["slug"] / f'{entry["slug"]}.md'
    path.write_text("\n".join(lines) + "\n")


def write_category_index(cat):
    lines = [
        f'# {cat["name"]}',
        "",
        cat["blurb"],
        "",
        '<div class="tool-grid" markdown="1">',
        "",
    ]
    for e in cat["entries"]:
        badge = f'<span class="cat-badge" style="background:{CAT_COLORS[cat["num"]]}">{e["tag"]}</span>'
        new = ' <span class="new-badge">NEW</span>' if e["new"] else ""
        lines += [
            f'<div class="tool-card" markdown="1">',
            f'',
            f'### [{e["name"]}]({e["slug"]}.md)',
            f'',
            f'{badge}{new}',
            f'',
            f'{e["desc"]}',
            f'',
            f'</div>',
            "",
        ]
    lines.append("</div>")
    path = TOOLS_DIR / cat["slug"] / "index.md"
    path.write_text("\n".join(lines) + "\n")


def main():
    if TOOLS_DIR.exists():
        shutil.rmtree(TOOLS_DIR)
    TOOLS_DIR.mkdir(parents=True)
    SHOT_DEST.mkdir(parents=True, exist_ok=True)

    categories = parse_manifest()
    shots_by_cat = parse_screenshot_index()

    nav_tools = []
    total = 0
    for cat in categories:
        cat_dir = TOOLS_DIR / cat["slug"]
        cat_dir.mkdir(exist_ok=True)

        shots = shots_by_cat.get(cat["name"].replace("&amp;", "&"), [])
        if len(shots) != len(cat["entries"]):
            print(f'WARNING: shot/entry count mismatch for {cat["name"]}: '
                  f'{len(shots)} shots vs {len(cat["entries"])} entries')

        nav_entries = []
        for entry, shot in zip(cat["entries"], shots + [None] * len(cat["entries"])):
            shot_rel = None
            if shot:
                src = Path.home() / "detectops-shots" / shot
                if src.exists():
                    shot_rel = src.name
                    shutil.copy(src, SHOT_DEST / shot_rel)
            write_tool_page(cat, entry, shot_rel)
            nav_entries.append((entry["name"], f'tools/{cat["slug"]}/{entry["slug"]}.md'))
            total += 1

        write_category_index(cat)
        nav_tools.append((cat["name"].replace("&amp;", "&"), f'tools/{cat["slug"]}/index.md', nav_entries))

    # Emit a nav snippet for mkdocs.yml (manual copy-in, printed to stdout)
    print(f"\nGenerated {total} tool pages across {len(categories)} categories.")
    print("\n--- paste into mkdocs.yml nav: 'Tools:' block ---\n")
    for cat_name, cat_index, entries in nav_tools:
        print(f"      - {cat_name}:")
        print(f"        - Overview: {cat_index}")
        for name, path in entries:
            safe_name = name.replace(":", "-")
            print(f"        - {safe_name}: {path}")


if __name__ == "__main__":
    main()
