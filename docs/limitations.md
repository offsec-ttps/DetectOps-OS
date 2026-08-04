# Limitations & Manual Steps

Almost everything in DetectOps runs out of the box with zero setup. A small
number of tools need a manual step first — usually because the item is
multi-gigabyte, requires an account DetectOps can't create on your behalf, or
only makes sense on a target you provide.

!!! warning "Heavy SIEM servers aren't pre-pulled"
    Elastic, OpenSearch, Wazuh, Graylog, Arkime, and BloodHound CE ship as
    staged `docker-compose.yml` files instead of baked-in multi-GB images —
    the build host only had ~14GB free at the time, and the VM is meant to
    run offline day-to-day. Run `docker-compose up -d` the first time you
    have internet; it's cached locally after that.

!!! warning "Splunk Universal Forwarder needs a splunk.com account"
    Download the `.deb` yourself and drop it at
    `config/packages.chroot/splunkforwarder_amd64.deb`, then add its exact
    package name to `config/package-lists/thirdparty-repo-tools.list.chroot`
    before building, if you want it baked in. (Not `includes.chroot` — a
    package installed that way gets silently purged by Debian Installer's
    own post-install cleanup.)

!!! info "Prelude Operator is commercial software"
    It requires your own free-tier signup at [prelude.org](https://prelude.org)
    — it can't legally be pre-bundled.

!!! info "Windows-only tools are staged as zip files"
    Mimikatz, PingCastle, AD Explorer, PEStudio, and the Sysinternals suite
    (Autoruns, Process Monitor, Process Explorer, TCPView) live under
    `/opt/detectops/windows-tools/` for deployment onto Windows targets —
    they don't run on the Linux desktop itself.

!!! info "PurpleSharp is source-only"
    It's a .NET tool traditionally compiled per engagement — bring your own
    .NET SDK when you need a fresh build.

---

*See the individual tool pages for anything with its own manual-step note —
most are one line (e.g. "needs your own AWS credentials").*
