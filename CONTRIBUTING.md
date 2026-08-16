# Contributing to DetectOps-OS docs

This repository is the source for the **published documentation site**
(docs.rusecure.in) — the tool catalog, getting-started guide, and reference
pages. It is not the build source for the OS image itself (the `live-build`
config, hooks, and package lists live in RuSecure's internal build
environment and aren't public yet), so contributions here are scoped to
**documentation and the testing/issue process**, not the OS build.

## Ways to contribute right now

1. **Report install/boot friction.** If you tested the ISO on hardware or a
   hypervisor and hit anything — boot menu, installer, first login, GUI not
   appearing — open an [install problem
   report](.github/ISSUE_TEMPLATE/install_problem.md). This is the single
   most valuable contribution during launch: it's exactly what turns release
   friction into a fixable list.
2. **Fix a docs bug.** Wrong command, broken link, outdated screenshot,
   unclear step — open a PR or an issue using the
   [bug report template](.github/ISSUE_TEMPLATE/bug_report.md).
3. **Request a tool or doc improvement.** Use the [feature
   request template](.github/ISSUE_TEMPLATE/feature_request.md).

## Local development

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Open <http://127.0.0.1:8000> — pages hot-reload on save.

Most pages under `docs/tools/**` are generated from the build manifest, not
hand-written — see the README's "For maintainers" section before editing
those directly. Hand-written pages (`index.md`, `getting-started.md`,
`limitations.md`, `troubleshooting.md`) are safe to edit normally.

## Submitting changes

1. Fork the repo and create a branch.
2. Make your change and verify it locally with `mkdocs serve`.
3. Open a PR against `main` with a short description of what changed and why.
4. Docs PRs that touch install/boot instructions, tool commands, or anything
   presented as a verified technical claim get a technical-accuracy review
   before merge — expect a review pass, not an instant merge.

## Code of conduct

Be direct, be specific, and back claims with reproduction steps. This is a
technical project for people doing detection-engineering work — the fastest
way to get a fix shipped is a precise repro, not a vague complaint.
