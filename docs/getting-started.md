# Getting Started

DetectOps ships as a bootable Debian 12 (bookworm) live ISO. Boot it, install
it, or run it as a VM — every tool listed under [Tools](tools/attack-simulation/index.md)
is already baked in.

Installing for the first time, or hit something unexpected? See
[Troubleshooting](troubleshooting.md) for verified environments, checksum
verification, and known install issues.

## Quick start

| | |
|---|---|
| **Login** | `detectops` / `detectops` — passwordless `sudo` |
| **Desktop** | XFCE — launch **DetectOps Menu** from the applications list, or run `detectops-menu` |
| **Find the VM's IP** | `ip -4 addr show scope global` |
| **Everything lives under** | `/opt/detectops/` |

## SSH access

Once you know the VM's IP, connect over SSH the same way you would to any
Debian box:

```bash
ssh detectops@<vm-ip>
```

Key-based auth works too — copy your public key over with `ssh-copy-id` once
you've logged in with the password once.

## Finding a tool

Tools are grouped into 10 categories, matching the left-hand navigation:

1. **Attack Simulation** — adversary emulation and BAS
2. **Detection Engineering** — Sigma, YARA, osquery
3. **Threat Hunting & Endpoint Analysis** — triage and forensic timelines
4. **Logging & SIEM** — forwarders and staged SIEM stacks
5. **Network Security** — IDS, capture and analysis
6. **Malware & Forensics** — static/dynamic triage
7. **AD & Enterprise Security** — Active Directory attack/defense
8. **Cloud & Kubernetes Security** — AWS/Azure/GCP/K8s, including the RedCloudOS suite
9. **Dev / Scripting Toolchain** — the daily-driver toolchain
10. **Security Utilities** — recon and password auditing

Each tool's page has its install path, the exact run command, and a live
screenshot. Paths are absolute inside the installed system; commands are
exactly what to type — copy-paste ready.

## Offline by design

Nothing in DetectOps needs internet access to run, unless a tool's page says
otherwise. A handful of items are intentionally **staged, not pre-pulled** —
heavy SIEM servers (Elastic, OpenSearch, Wazuh, Graylog, Arkime) ship as
`docker-compose.yml` files instead of multi-GB images, and a couple of tools
need a one-time account signup (Splunk, Prelude Operator) that can't legally
or technically be bundled. See [Limitations & Manual Steps](limitations.md)
for the full list.
