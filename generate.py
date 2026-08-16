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

# Reference link for each tool's official upstream repo/homepage, keyed by
# the same slug generate.py produces from the manifest's tool name. Sourced
# from the actual clone_or_update/github_latest_asset URLs baked into
# config/hooks/live/*.hook.chroot wherever a hook exists (so it matches
# exactly what's vendored on disk, not just "whatever repo has that name" -
# e.g. kubiscan/pmapper/eksholmes point at the RedCloudOS forks actually
# installed, not the original upstream projects they were forked from).
# Tools with no single canonical repo (apt packages, language toolchains,
# closed-source freeware) link to the official project homepage instead.
REFERENCE_URLS = {
    # Attack Simulation
    "caldera": "https://github.com/apache/caldera",
    "splunk-attack-range-local": "https://github.com/splunk/attack_range_local",
    "splunk-attack-range-cloud": "https://github.com/splunk/attack_range_cloud",
    "atomic-red-team": "https://github.com/redcanaryco/atomic-red-team",
    "invoke-atomicredteam": "https://github.com/redcanaryco/invoke-atomicredteam",
    "powershell-yaml": "https://github.com/cloudbase/powershell-yaml",
    "purplesharp": "https://github.com/mvelazc0/PurpleSharp",
    "infection-monkey": "https://github.com/guardicore/monkey",
    "stratus-red-team": "https://github.com/DataDog/stratus-red-team",
    "metasploit-framework": "https://github.com/rapid7/metasploit-framework",
    "prelude-operator": "https://www.prelude.org/",
    "leonidas": "https://github.com/ReversecLabs/leonidas",
    "msinvader": "https://github.com/mvelazc0/msInvader",
    "vulnerable-cloudk8sci-cd-labs-redcloudos-goat-set": "https://github.com/RedCloudOS/vm-packages",
    # Detection Engineering
    "sigma": "https://github.com/SigmaHQ/sigma",
    "sigma-specification": "https://github.com/SigmaHQ/sigma-specification",
    "pysigma-sigma-cli": "https://github.com/SigmaHQ/pySigma",
    "yara": "https://github.com/VirusTotal/yara",
    "yara-x": "https://github.com/VirusTotal/yara-x",
    "osquery": "https://github.com/osquery/osquery",
    # Threat Hunting & Endpoint Analysis
    "velociraptor": "https://github.com/Velocidex/velociraptor",
    "hayabusa": "https://github.com/Yamato-Security/hayabusa",
    "chainsaw": "https://github.com/WithSecureLabs/chainsaw",
    "zircolite": "https://github.com/wagga40/Zircolite",
    "plaso-log2timeline": "https://github.com/log2timeline/plaso",
    "volatility3": "https://github.com/volatilityfoundation/volatility3",
    "sysmon-config": "https://github.com/SwiftOnSecurity/sysmon-config",
    "sysinternals-suite": "https://learn.microsoft.com/en-us/sysinternals/",
    # Logging & SIEM
    "fluent-bit": "https://github.com/fluent/fluent-bit",
    "grafana": "https://github.com/grafana/grafana",
    "vector": "https://github.com/vectordotdev/vector",
    "loki": "https://github.com/grafana/loki",
    "splunk-universal-forwarder": "https://www.splunk.com/en_us/download/universal-forwarder.html",
    "elastic-kibana": "https://github.com/elastic/kibana",
    "opensearch-dashboards": "https://github.com/opensearch-project/OpenSearch",
    "wazuh": "https://github.com/wazuh/wazuh-docker",
    "graylog": "https://github.com/Graylog2/graylog2-server",
    "arkime": "https://github.com/arkime/arkime",
    # Network Security
    "zeek": "https://github.com/zeek/zeek",
    "suricata-et-open-rules": "https://github.com/OISF/suricata",
    "wireshark-tshark-tcpdump": "https://www.wireshark.org/",
    "brim-zui": "https://github.com/brimdata/zui",
    "maltrail": "https://github.com/stamparm/maltrail",
    # Malware & Forensics
    "capa": "https://github.com/mandiant/capa",
    "floss": "https://github.com/mandiant/flare-floss",
    "detect-it-easy-die": "https://github.com/horsicq/Detect-It-Easy",
    "pestudio": "https://www.winitor.com/",
    "cyberchef": "https://github.com/gchq/CyberChef",
    "binwalk": "https://github.com/ReFirmLabs/binwalk",
    "autopsy-sleuth-kit": "https://github.com/sleuthkit/autopsy",
    # AD & Enterprise Security
    "impacket": "https://github.com/fortra/impacket",
    "certipy": "https://github.com/ly4k/Certipy",
    "bloodhound-ce": "https://github.com/SpecterOps/BloodHound",
    "mimikatz": "https://github.com/gentilkiwi/mimikatz",
    "pingcastle": "https://github.com/vletoux/PingCastle",
    "ad-explorer": "https://learn.microsoft.com/en-us/sysinternals/downloads/adexplorer",
    # Cloud & Kubernetes Security
    "scoutsuite": "https://github.com/nccgroup/ScoutSuite",
    "prowler": "https://github.com/prowler-cloud/prowler",
    "cloudsplaining": "https://github.com/salesforce/cloudsplaining",
    "kube-hunter": "https://github.com/aquasecurity/kube-hunter",
    "trivy": "https://github.com/aquasecurity/trivy",
    "kube-bench": "https://github.com/aquasecurity/kube-bench",
    "whoami-scanner": "https://github.com/DataDog/whoAMI-scanner",
    "eksholmes": "https://github.com/RedCloudOS/EKSHolmes",
    "azurehound": "https://github.com/SpecterOps/AzureHound",
    "cloudfox": "https://github.com/BishopFox/cloudfox",
    "cloudbrute": "https://github.com/0xsha/CloudBrute",
    "peirates": "https://github.com/inguardians/peirates",
    "gitleaks": "https://github.com/gitleaks/gitleaks",
    "pacu": "https://github.com/RhinoSecurityLabs/pacu",
    "roadtx": "https://github.com/dirkjanm/ROADtools",
    "cartography": "https://github.com/cartography-cncf/cartography",
    "pmapper": "https://github.com/RedCloudOS/PMapper",
    "heimdall": "https://github.com/RedCloudOS/heimdall",
    "gcpbucketbrute": "https://github.com/RedCloudOS/GCPBucketBrute",
    "gcptokenreuse": "https://github.com/RedCloudOS/GCPTokenReuse",
    "gcp-scanner": "https://github.com/RedCloudOS/gcp_scanner",
    "kubiscan": "https://github.com/RedCloudOS/KubiScan",
    "awesomeuserfinder": "https://github.com/RedCloudOS/AWeSomeUserFinder",
    "oh365userfinder": "https://github.com/RedCloudOS/Oh365UserFinder",
    "cloud-enum": "https://github.com/RedCloudOS/cloud_enum",
    # Dev / Scripting Toolchain
    "python-3": "https://www.python.org/",
    "powershell-7": "https://github.com/PowerShell/PowerShell",
    "go": "https://go.dev/",
    "rust-cargo": "https://www.rust-lang.org/",
    "docker-docker-compose-podman": "https://docs.docker.com/",
    "git-github-cli": "https://cli.github.com/",
    "visual-studio-code": "https://github.com/microsoft/vscode",
    "jq-yq": "https://github.com/mikefarah/yq",
    # Security Utilities
    "nmap-masscan": "https://nmap.org/",
    "gobuster-dirb-ffuf": "https://github.com/OJ/gobuster",
    "sqlmap-nikto": "https://github.com/sqlmapproject/sqlmap",
    "john-the-ripper-hashcat": "https://github.com/openwall/john",
    "hydra": "https://github.com/vanhauser-thc/thc-hydra",
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

    ref_url = REFERENCE_URLS.get(entry["slug"])
    if ref_url:
        lines += ["## Reference", "", f'[{ref_url}]({ref_url})', ""]
    else:
        print(f'WARNING: no REFERENCE_URLS entry for slug "{entry["slug"]}" ({entry["name"]})')

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
