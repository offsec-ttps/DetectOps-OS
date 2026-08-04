# Attack Simulation

Adversary emulation and BAS — generate the telemetry your detections are supposed to catch.

<div class="tool-grid" markdown="1">

<div class="tool-card" markdown="1">

### [CALDERA](caldera.md)

<span class="cat-badge" style="background:#D9724C">C2 / BAS</span>

MITRE's automated adversary emulation platform. Full offline pip cache, so it never needs the internet.

</div>

<div class="tool-card" markdown="1">

### [Splunk Attack Range — Local](splunk-attack-range-local.md)

<span class="cat-badge" style="background:#D9724C">lab</span>

Vagrant+Ansible lab builder — Windows DC/Server, Splunk Server, Kali, CALDERA/Phantom servers, on VirtualBox. Added via the local-tools pipeline.

</div>

<div class="tool-card" markdown="1">

### [Splunk Attack Range — Cloud](splunk-attack-range-cloud.md)

<span class="cat-badge" style="background:#D9724C">lab / aws</span>

Same lab concept as the Local variant, provisioned as real AWS infrastructure via Terraform instead. Added via the local-tools pipeline.

</div>

<div class="tool-card" markdown="1">

### [Atomic Red Team](atomic-red-team.md)

<span class="cat-badge" style="background:#D9724C">tests</span>

RedCanary's library of small, atomic ATT&CK technique tests.

</div>

<div class="tool-card" markdown="1">

### [Invoke-AtomicRedTeam](invoke-atomicredteam.md)

<span class="cat-badge" style="background:#D9724C">module</span>

The PowerShell runner for Atomic Red Team. Auto-imported in every pwsh session.

</div>

<div class="tool-card" markdown="1">

### [powershell-yaml](powershell-yaml.md)

<span class="cat-badge" style="background:#D9724C">module</span>

YAML parser module Invoke-AtomicRedTeam depends on to read atomic test definitions.

</div>

<div class="tool-card" markdown="1">

### [PurpleSharp](purplesharp.md)

<span class="cat-badge" style="background:#D9724C">.net src</span>

C#/PowerShell adversary simulation, normally compiled fresh per engagement.

</div>

<div class="tool-card" markdown="1">

### [Infection Monkey](infection-monkey.md)

<span class="cat-badge" style="background:#D9724C">manual</span>

Guardicore's automated breach-and-attack-simulation platform.

</div>

<div class="tool-card" markdown="1">

### [Stratus Red Team](stratus-red-team.md)

<span class="cat-badge" style="background:#D9724C">binary</span>

DataDog's granular attack-technique emulation for AWS/Azure/GCP/K8s.

</div>

<div class="tool-card" markdown="1">

### [Metasploit Framework](metasploit-framework.md)

<span class="cat-badge" style="background:#D9724C">system</span>

Installed system-wide via Rapid7's own installer, fully baked in.

</div>

<div class="tool-card" markdown="1">

### [Prelude Operator](prelude-operator.md)

<span class="cat-badge" style="background:#D9724C">n/a</span>

Commercial BAS tool — free tier requires a Prelude account, so it isn't pre-bundled.

</div>

<div class="tool-card" markdown="1">

### [Leonidas](leonidas.md)

<span class="cat-badge" style="background:#D9724C">redcloudos</span> <span class="new-badge">NEW</span>

Automated cloud attack simulation with matching detection use cases, deployed as an AWS Lambda pipeline.

</div>

<div class="tool-card" markdown="1">

### [msInvader](msinvader.md)

<span class="cat-badge" style="background:#D9724C">redcloudos</span> <span class="new-badge">NEW</span>

Simulates post-compromise M365/Entra ID adversary techniques (mailbox rules, forwarding, delegation) via Graph/EWS/REST.

</div>

<div class="tool-card" markdown="1">

### [Vulnerable cloud/K8s/CI-CD labs (RedCloudOS "goat" set)](vulnerable-cloudk8sci-cd-labs-redcloudos-goat-set.md)

<span class="cat-badge" style="background:#D9724C">lab / billable</span> <span class="new-badge">NEW</span>

11 intentionally-vulnerable environments cloned as editable source: AzureGoat, AWSGoat, GCPGoat, EntraGoat, CloudGoat, CloudFoxable, Kubernetes Goat, EKS Goat, TerraGoat, CI/CD Goat, GitHub Actions Goat.

</div>

</div>
