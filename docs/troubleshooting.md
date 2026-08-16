# Troubleshooting

This page covers installing and booting DetectOps OS. If a tool itself is
misbehaving after you're up and running, check that tool's own doc page
first — most have a manual-step note in [Limitations](limitations.md).

Hit something not covered here? [Open an install
problem](https://github.com/offsec-ttps/DetectOps-OS/issues/new?template=install_problem.md)
— reports from real installs are what turn this page from three tested
scenarios into a real compatibility list.

## Verify your download before installing

Always check the ISO's checksum before booting it — a corrupted download is
the single most common cause of installer failures that look like something
else entirely.

```bash
sha256sum detectops-os-<version>.iso
```

Compare the output against the `SHA256SUMS` file published alongside the
release. If it doesn't match, re-download rather than debugging further —
almost everything downstream of a bad ISO looks like a different bug.

## Supported / verified environments

| Environment | Status |
|---|---|
| VirtualBox — 8GB RAM / 4 cores / 100GB disk / bridged adapter, **install mode** (not live session) | ✅ Verified by the DetectOps team |
| VMware Workstation/Fusion | ⚠️ Not yet verified — please test and report back |
| Bare metal | ⚠️ Not yet verified — please test and report back |
| UEFI boot | ⚠️ Not yet verified — the tested path is legacy/BIOS boot in VirtualBox |
| Less than 8GB RAM / 4 cores / 100GB disk | ⚠️ Not tested; the OS bundles 94 tools and several staged multi-GB stacks, so undersizing disk is the most likely early failure |

We deliberately label this table honestly rather than claim broad
compatibility we haven't tested. If you run DetectOps OS somewhere not
listed above, [tell us what happened](https://github.com/offsec-ttps/DetectOps-OS/issues/new?template=install_problem.md)
either way — a clean run is just as useful to know about as a failure.

## Install mode vs. live session

Boot into **install mode**, not the live/try-it session. The live session is
fine for a quick look, but tools, PATH entries, and desktop launchers are set
up for the installed system — don't file a "tool X isn't there" bug against
the live session.

## No GUI / desktop after install

If you land at a text login with no XFCE desktop after install, this is a
known failure class in Debian `live-build` images (a hook removing NVIDIA
driver packages can cascade into removing the generic Mesa/X11 stack via
`apt-get autoremove`, or Debian Installer's own post-install cleanup can
silently purge packages that weren't installed through the build's package-list
manifest). Both of these were hit and fixed during DetectOps OS's own build
process. If you see this on a current build, it's a regression — please
[report it](https://github.com/offsec-ttps/DetectOps-OS/issues/new?template=install_problem.md)
with your exact environment rather than assuming it's expected.

## Login problems

Default credentials are `detectops` / `detectops` with passwordless `sudo`.
If that doesn't work, double check you're logging into the **installed**
system, not still sitting at the live-session boot menu.
