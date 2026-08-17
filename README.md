<p align="center">
  <img src=".github/banner.png" alt="DetectOps OS — Know the Attack Before You Face It." width="100%" />
</p>

<h3 align="center">Know the Attack Before You Face It.</h3>

<p align="center"><b>A Debian 12 (bookworm) live-build Detection Engineering OS — 94 tools across 10 categories, fully offline-capable once installed.</b></p>

<p align="center"><a href="https://docs.rusecure.in/"><b>📖 Read the full documentation →</b></a></p>

---

## What is DetectOps-OS?

**DetectOps-OS** is a purpose-built Linux distribution for detection
engineers, threat hunters, and blue teams. Instead of spending hours
installing, configuring, and patching together dozens of separate tools
across attack simulation, detection engineering, threat hunting, logging,
network security, forensics, and cloud security — boot one ISO and every
tool is already there, already configured, and ready to run.

It's built by [RuSecure](https://docs.rusecure.in/) on top of Debian 12
(bookworm) using `live-build`, so it's a real, general-purpose Linux system
underneath — not a locked-down appliance. Everything is baked directly into
the image at build time, which means the whole point of the project holds
even with no internet connection: **install it once, and it works fully
offline from then on.**

### Why detection engineers use it

- **The full attack → detect → validate loop, in one place.** Simulate an
  attack technique (CALDERA, Atomic Red Team, Stratus Red Team), generate
  the telemetry it produces, write and test a detection for it (Sigma,
  YARA, osquery), and hunt through the result (Velociraptor, Hayabusa,
  Chainsaw, Zircolite) — without switching machines or reinstalling
  anything in between.
- **Nothing to configure before you can start working.** Tool installs,
  API keys where applicable, PATH entries, Python venvs, and desktop
  launchers are already set up. Every tool's documentation page shows the
  exact command to run and a real screenshot of its output.
- **Fully offline after install.** No tool silently phones home for an
  update mid-engagement, and nothing breaks because a build host had a bad
  network day — the entire toolset ships inside the ISO.
- **Broad, current coverage.** Includes the official
  [RedCloudOS](https://github.com/RedCloudOS/vm-packages) cloud/Kubernetes
  offensive tooling suite alongside the standard detection-engineering
  stack — every RedCloudOS-sourced tool is clearly flagged with a
  <img src="https://img.shields.io/badge/-NEW-1E8E3E" height="16" align="top"/>
  badge in the docs.

## What's inside

| # | Category | Tools | Covers |
|---|---|---|---|
| 01 | **Attack Simulation** | 14 | Adversary emulation & BAS — CALDERA, Atomic Red Team, Stratus Red Team, Metasploit |
| 02 | **Detection Engineering** | 6 | Sigma, YARA, osquery |
| 03 | **Threat Hunting & Endpoint Analysis** | 8 | Velociraptor, Hayabusa, Chainsaw, Zircolite, Volatility3 |
| 04 | **Logging & SIEM** | 10 | Fluent Bit, Grafana, Vector, Loki, plus staged Elastic/OpenSearch/Wazuh/Graylog/Arkime stacks |
| 05 | **Network Security** | 5 | Zeek, Suricata, Wireshark/tshark, Brim/Zui |
| 06 | **Malware & Forensics** | 7 | CAPA, FLOSS, Detect It Easy, CyberChef, Autopsy |
| 07 | **AD & Enterprise Security** | 6 | Impacket, Certipy, BloodHound CE, Mimikatz, PingCastle |
| 08 | **Cloud & Kubernetes Security** | 25 | ScoutSuite, Prowler, Trivy, kube-bench, plus the full RedCloudOS AWS/Azure/GCP/K8s suite |
| 09 | **Dev / Scripting Toolchain** | 8 | Python, PowerShell 7, Go, Rust, Docker, Git |
| 10 | **Security Utilities** | 5 | Nmap/Masscan, Gobuster/ffuf, SQLMap, John/Hashcat, Hydra |

Every single tool has its own documentation page with what it is, where it
lives on disk, the exact command to run it, a real terminal screenshot
captured from a running VM, and any manual setup step it needs (an account
signup, your own cloud credentials, etc.) called out clearly.

**[→ Browse the full tool catalog](https://docs.rusecure.in/tools/attack-simulation/)**

## Quick start

**[Download the ISO →](https://github.com/offsec-ttps/DetectOps-OS/releases/tag/v1.0.0)** (split into 5 parts + checksum — see the release page for reassembly steps)


| | |
|---|---|
| **Login** | `detectops` / `detectops` — passwordless `sudo` |
| **Desktop** | XFCE — launch **DetectOps Menu** from the applications list |
| **Everything lives under** | `/opt/detectops/` |

See **[Getting Started](https://docs.rusecure.in/getting-started/)** in the
docs for the full walkthrough, and
**[Limitations & Manual Steps](https://docs.rusecure.in/limitations/)** for
the handful of tools that need a one-time account signup or your own cloud
credentials before they'll run.

---

## About this repository

This repository holds the **source for DetectOps-OS's published
documentation site** (built with [MkDocs](https://www.mkdocs.org/) +
[Material](https://squidfunk.github.io/mkdocs-material/)), live at
**[docs.rusecure.in](https://docs.rusecure.in/)**. If you're looking for
how to *use* DetectOps-OS, the tool catalog, or how any specific tool works,
head to the live site above — that's the primary resource, not this README.

The sections below are for anyone maintaining or contributing to the
documentation itself.

<details>
<summary><strong>For maintainers: local development, regenerating tool pages, and hosting</strong></summary>

### Local development

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Then open <http://127.0.0.1:8000>. Pages hot-reload on save.

### Regenerating the tool pages

`docs/tools/**` is generated, not hand-written — it's built from
`../detectops-manifest.html` (the build manifest) plus the screenshots at
`~/detectops-shots/`. After a manifest update or a fresh screenshot sweep,
regenerate it with:

```bash
python3 generate.py
```

This rewrites every file under `docs/tools/` and copies any new screenshots
into `docs/assets/screenshots/`. It also prints an updated `nav:` block for
`mkdocs.yml` if the tool list itself changed (new tool added/removed, not
just content edits) — paste that over the existing `Tools:` section.

Hand-written pages (`index.md`, `getting-started.md`, `limitations.md`,
`stylesheets/extra.css`) are never touched by the generator.

### Publishing to GitHub Pages (free, with your own domain)

1. **Create a new GitHub repo** and push this `docs-site/` directory to it
   as the repo root:
   ```bash
   cd docs-site
   git init
   git add .
   git commit -m "Initial DetectOps documentation site"
   git branch -M main
   git remote add origin https://github.com/offsec-ttps/DetectOps-OS.git
   git push -u origin main
   ```
2. In the repo's **Settings → Pages**, set the source to the `gh-pages`
   branch (created automatically the first time the workflow in
   `.github/workflows/deploy.yml` runs — it fires on every push to `main`).
3. Update `site_url:` and `repo_url:` at the top of `mkdocs.yml` to your real
   values before the first deploy.

### Using your own domain

1. Add a file `docs/CNAME` containing just your domain, e.g.:
   ```
   docs.yourdomain.com
   ```
   (`mkdocs gh-deploy` copies it into the published site automatically, and
   GitHub Pages reads it from there on every deploy — you only need to add it
   once, it isn't regenerated by `generate.py`.)
2. At your DNS provider, add a `CNAME` record:
   ```
   docs.yourdomain.com  →  <you>.github.io
   ```
   (Apex/root domains like `yourdomain.com` instead need 4 `A` records
   pointing at GitHub Pages' IPs — see
   [GitHub's docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
   for the current IP list.)
3. Back in **Settings → Pages**, enter the same domain in the "Custom domain"
   field and enable "Enforce HTTPS" once the certificate provisions (can take
   up to ~24h after DNS propagates).

</details>
