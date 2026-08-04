# Splunk Attack Range — Cloud

<span class="cat-badge" style="background:#D9724C">lab / aws</span>

Same lab concept as the Local variant, provisioned as real AWS infrastructure via Terraform instead. Added via the local-tools pipeline.

![Splunk Attack Range — Cloud screenshot](../../assets/screenshots/003-attack-range-cloud.png)

## Location

`/opt/detectops/attack-simulation/attack-range-cloud`

## How to run

```bash
source venv/bin/activate
aws configure   # your own AWS credentials — none are bundled
python cloud_attack_range.py configure && python cloud_attack_range.py build
```

!!! warning "Manual step required"
    provisions real, billable AWS resources (EC2, EKS) — always run `python cloud_attack_range.py destroy` when finished


---

*Part of the **Attack Simulation** toolset in DetectOps.*
