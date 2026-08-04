# Cloud & Kubernetes Security

Audit cloud accounts, IAM policy, container images, and clusters.

<div class="tool-grid" markdown="1">

<div class="tool-card" markdown="1">

### [ScoutSuite](scoutsuite.md)

<span class="cat-badge" style="background:#4FB4BE">venv</span>

Multi-cloud security-posture auditing (AWS/Azure/GCP/…) with an HTML report.

</div>

<div class="tool-card" markdown="1">

### [Prowler](prowler.md)

<span class="cat-badge" style="background:#4FB4BE">venv</span>

AWS/Azure/GCP/K8s CIS-benchmark and best-practice auditing.

</div>

<div class="tool-card" markdown="1">

### [Cloudsplaining](cloudsplaining.md)

<span class="cat-badge" style="background:#4FB4BE">venv</span>

Flags risky AWS IAM policies (privilege escalation, wildcard actions).

</div>

<div class="tool-card" markdown="1">

### [kube-hunter](kube-hunter.md)

<span class="cat-badge" style="background:#4FB4BE">venv</span>

Hunts for exploitable weaknesses in a Kubernetes cluster.

</div>

<div class="tool-card" markdown="1">

### [Trivy](trivy.md)

<span class="cat-badge" style="background:#4FB4BE">system</span>

Vulnerability/misconfig scanner for images, filesystems, and IaC.

</div>

<div class="tool-card" markdown="1">

### [kube-bench](kube-bench.md)

<span class="cat-badge" style="background:#4FB4BE">binary</span>

Checks a cluster against the CIS Kubernetes Benchmark.

</div>

<div class="tool-card" markdown="1">

### [whoAMI-scanner](whoami-scanner.md)

<span class="cat-badge" style="background:#4FB4BE">binary</span> <span class="new-badge">NEW</span>

Scans an AWS account for the "whoAMI" AMI name-confusion attack (Datadog).

</div>

<div class="tool-card" markdown="1">

### [EKSHolmes](eksholmes.md)

<span class="cat-badge" style="background:#4FB4BE">redcloudos</span> <span class="new-badge">NEW</span>

Enumerates AWS EKS clusters (RedCloudOS's own tool). No upstream release exists — built from Go source at ISO build time.

</div>

<div class="tool-card" markdown="1">

### [AzureHound](azurehound.md)

<span class="cat-badge" style="background:#4FB4BE">binary</span> <span class="new-badge">NEW</span>

BloodHound-style attack-path data collector for Entra ID/Azure (SpecterOps).

</div>

<div class="tool-card" markdown="1">

### [cloudfox](cloudfox.md)

<span class="cat-badge" style="background:#4FB4BE">binary</span> <span class="new-badge">NEW</span>

Situational-awareness enumeration for cloud penetration tests (BishopFox).

</div>

<div class="tool-card" markdown="1">

### [CloudBrute](cloudbrute.md)

<span class="cat-badge" style="background:#4FB4BE">binary</span> <span class="new-badge">NEW</span>

Cloud infrastructure/asset enumerator across AWS/Azure/GCP/DigitalOcean/etc.

</div>

<div class="tool-card" markdown="1">

### [peirates](peirates.md)

<span class="cat-badge" style="background:#4FB4BE">binary</span> <span class="new-badge">NEW</span>

Kubernetes penetration-testing tool for privilege escalation inside a cluster.

</div>

<div class="tool-card" markdown="1">

### [gitleaks](gitleaks.md)

<span class="cat-badge" style="background:#4FB4BE">binary</span> <span class="new-badge">NEW</span>

Scans git history/filesystems for hardcoded secrets and credentials.

</div>

<div class="tool-card" markdown="1">

### [Pacu](pacu.md)

<span class="cat-badge" style="background:#4FB4BE">venv</span> <span class="new-badge">NEW</span>

Rhino Security Labs' AWS exploitation framework — post-compromise enumeration and attack modules.

</div>

<div class="tool-card" markdown="1">

### [roadtx](roadtx.md)

<span class="cat-badge" style="background:#4FB4BE">venv</span> <span class="new-badge">NEW</span>

ROADtools' Entra ID/Azure AD token-exchange and authentication toolkit.

</div>

<div class="tool-card" markdown="1">

### [Cartography](cartography.md)

<span class="cat-badge" style="background:#4FB4BE">venv</span> <span class="new-badge">NEW</span>

Lyft's infrastructure asset-graph tool — ingests AWS/Azure/GCP/K8s state into Neo4j for attack-path queries.

</div>

<div class="tool-card" markdown="1">

### [PMapper](pmapper.md)

<span class="cat-badge" style="background:#4FB4BE">redcloudos</span> <span class="new-badge">NEW</span>

Evaluates AWS IAM permissions to find privilege-escalation paths (NCC Group original, RedCloudOS fork).

</div>

<div class="tool-card" markdown="1">

### [heimdall](heimdall.md)

<span class="cat-badge" style="background:#4FB4BE">redcloudos</span> <span class="new-badge">NEW</span>

AWS attack-path scanner covering privilege escalation across 10+ services.

</div>

<div class="tool-card" markdown="1">

### [GCPBucketBrute](gcpbucketbrute.md)

<span class="cat-badge" style="background:#4FB4BE">redcloudos</span> <span class="new-badge">NEW</span>

Enumerates GCS bucket names and checks/privesc's your access to each.

</div>

<div class="tool-card" markdown="1">

### [GCPTokenReuse](gcptokenreuse.md)

<span class="cat-badge" style="background:#4FB4BE">redcloudos</span> <span class="new-badge">NEW</span>

Single-script tool that reuses a compromised GCP OAuth token across scopes/services.

</div>

<div class="tool-card" markdown="1">

### [gcp_scanner](gcp-scanner.md)

<span class="cat-badge" style="background:#4FB4BE">redcloudos</span> <span class="new-badge">NEW</span>

Comprehensive scanner for exposed/misconfigured Google Cloud resources.

</div>

<div class="tool-card" markdown="1">

### [KubiScan](kubiscan.md)

<span class="cat-badge" style="background:#4FB4BE">redcloudos</span> <span class="new-badge">NEW</span>

Scans a Kubernetes cluster for risky RBAC roles/bindings and risky pods.

</div>

<div class="tool-card" markdown="1">

### [AWeSomeUserFinder](awesomeuserfinder.md)

<span class="cat-badge" style="background:#4FB4BE">redcloudos</span> <span class="new-badge">NEW</span>

AWS IAM username enumeration and password-spraying tool.

</div>

<div class="tool-card" markdown="1">

### [Oh365UserFinder](oh365userfinder.md)

<span class="cat-badge" style="background:#4FB4BE">redcloudos</span> <span class="new-badge">NEW</span>

Office 365 / Entra ID username enumeration tool.

</div>

<div class="tool-card" markdown="1">

### [cloud_enum](cloud-enum.md)

<span class="cat-badge" style="background:#4FB4BE">redcloudos</span> <span class="new-badge">NEW</span>

Multi-cloud OSINT enumeration of public resources across AWS/Azure/GCP.

</div>

</div>
