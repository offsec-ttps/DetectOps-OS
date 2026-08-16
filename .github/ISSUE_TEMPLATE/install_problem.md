---
name: Install / boot problem
about: The ISO didn't boot, install, or start correctly
title: "[Install] "
labels: install
assignees: ''
---

**What did you try to boot/install on?**
(VirtualBox / VMware / bare metal / other — include version)

**Host allocation given to the VM (or bare-metal specs)**
- RAM:
- CPU cores:
- Disk:
- Boot mode (BIOS/Legacy or UEFI):

**Where in the process did it fail?**
- [ ] Boot menu didn't appear
- [ ] Live session booted but installer crashed/hung
- [ ] Installer completed, but the installed system didn't boot
- [ ] Installed system booted, but no GUI/desktop
- [ ] Something else (describe below)

**Checksum check**
Did `sha256sum` on your downloaded ISO match the value published with the release?
- [ ] Yes, matched
- [ ] No, mismatched
- [ ] Didn't check

**What happened**
Paste the exact error text or describe what you saw. A screenshot or photo of the screen is fine if there's no way to copy text.

**Login used (if you got that far)**
`detectops` / `detectops` is the default — note if you changed it.

**Anything else**
Console output, `journalctl` excerpts, or anything else that seems relevant.
