# Vulnerable cloud/K8s/CI-CD labs (RedCloudOS "goat" set)

<span class="cat-badge" style="background:#D9724C">lab / billable</span> <span class="new-badge">NEW</span>

11 intentionally-vulnerable environments cloned as editable source: AzureGoat, AWSGoat, GCPGoat, EntraGoat, CloudGoat, CloudFoxable, Kubernetes Goat, EKS Goat, TerraGoat, CI/CD Goat, GitHub Actions Goat.

![Vulnerable cloud/K8s/CI-CD labs (RedCloudOS "goat" set) screenshot](../../assets/screenshots/014-redcloudos-goats.png)

## Location

`/opt/detectops/attack-simulation/redcloudos/goats/<name>`

!!! warning "Manual step required"
    none are deployed at build time — each provisions real, billable cloud infra (or, for Kubernetes Goat / CI/CD Goat, local Docker) via its own script using your own credentials; always run its teardown step when done. See goats/README.txt


---

*Part of the **Attack Simulation** toolset in DetectOps.*
