---
title: DetectOps
hide:
  - navigation
  - toc
---

<div class="hero" markdown>

# DetectOps

A Debian 12 (bookworm) live-build Detection Engineering OS — every tool
baked into the ISO at build time, fully offline-capable once installed.

<div class="stat-row">
  <div class="stat"><span class="n">94</span><span class="l">Tools</span></div>
  <div class="stat"><span class="n">10</span><span class="l">Categories</span></div>
  <div class="stat"><span class="n">7.2 GB</span><span class="l">ISO</span></div>
  <div class="stat"><span class="n">bookworm</span><span class="l">Debian amd64</span></div>
</div>

[Get started](getting-started.md){ .md-button .md-button--primary }
[Browse the tools](tools/attack-simulation/index.md){ .md-button }

</div>

---

## Categories

<div class="cat-grid" markdown="0">

<div class="cat-tile" style="--tile-color:#D9724C">
  <div class="num">01</div>
  <div class="name">Attack Simulation</div>
  <div class="count">14 tools · adversary emulation &amp; BAS</div>
  <a class="stretched-link" href="tools/attack-simulation/"></a>
</div>

<div class="cat-tile" style="--tile-color:#4CA593">
  <div class="num">02</div>
  <div class="name">Detection Engineering</div>
  <div class="count">6 tools · Sigma, YARA, osquery</div>
  <a class="stretched-link" href="tools/detection-engineering/"></a>
</div>

<div class="cat-tile" style="--tile-color:#9689D6">
  <div class="num">03</div>
  <div class="name">Threat Hunting &amp; Endpoint Analysis</div>
  <div class="count">8 tools · triage &amp; forensic timelines</div>
  <a class="stretched-link" href="tools/threat-hunting-endpoint-analysis/"></a>
</div>

<div class="cat-tile" style="--tile-color:#5B9BD5">
  <div class="num">04</div>
  <div class="name">Logging &amp; SIEM</div>
  <div class="count">10 tools · forwarders &amp; staged SIEM stacks</div>
  <a class="stretched-link" href="tools/logging-siem/"></a>
</div>

<div class="cat-tile" style="--tile-color:#7CAE72">
  <div class="num">05</div>
  <div class="name">Network Security</div>
  <div class="count">5 tools · IDS, capture &amp; analysis</div>
  <a class="stretched-link" href="tools/network-security/"></a>
</div>

<div class="cat-tile" style="--tile-color:#B478A6">
  <div class="num">06</div>
  <div class="name">Malware &amp; Forensics</div>
  <div class="count">7 tools · static/dynamic triage</div>
  <a class="stretched-link" href="tools/malware-forensics/"></a>
</div>

<div class="cat-tile" style="--tile-color:#8291B8">
  <div class="num">07</div>
  <div class="name">AD &amp; Enterprise Security</div>
  <div class="count">6 tools · Active Directory attack/defense</div>
  <a class="stretched-link" href="tools/ad-enterprise-security/"></a>
</div>

<div class="cat-tile" style="--tile-color:#4FB4BE">
  <div class="num">08</div>
  <div class="name">Cloud &amp; Kubernetes Security</div>
  <div class="count">25 tools · AWS/Azure/GCP/K8s, incl. RedCloudOS</div>
  <a class="stretched-link" href="tools/cloud-kubernetes-security/"></a>
</div>

<div class="cat-tile" style="--tile-color:#C2A544">
  <div class="num">09</div>
  <div class="name">Dev / Scripting Toolchain</div>
  <div class="count">8 tools · the daily-driver toolchain</div>
  <a class="stretched-link" href="tools/dev-scripting-toolchain/"></a>
</div>

<div class="cat-tile" style="--tile-color:#C6768E">
  <div class="num">10</div>
  <div class="name">Security Utilities</div>
  <div class="count">5 tools · recon &amp; password auditing</div>
  <a class="stretched-link" href="tools/security-utilities/"></a>
</div>

</div>

---

## What's on every page

Every tool page in this documentation includes:

- **What it is** — a one-line description of the tool and why it's here
- **Where it lives** — the absolute path inside the installed system
- **How to run it** — the exact command to type, copy-paste ready
- **A real screenshot** — captured live from a running DetectOps VM, not a
  vendor marketing image
- **Notes** — anything that needs a manual step first (credentials, an
  internet connection, a `.NET` SDK, etc.)

A green **NEW** badge marks tools sourced from
[RedCloudOS/vm-packages](https://github.com/RedCloudOS/vm-packages).

[:octicons-arrow-right-24: See what's staged vs. baked-in](limitations.md)
