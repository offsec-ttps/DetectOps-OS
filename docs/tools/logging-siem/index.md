# Logging & SIEM

Forwarders and dashboards are fully offline. The multi-GB SIEM servers ship as compose files you pull once, by design — see limitations.

<div class="tool-grid" markdown="1">

<div class="tool-card" markdown="1">

### [Fluent Bit](fluent-bit.md)

<span class="cat-badge" style="background:#5B9BD5">service</span>

Lightweight log/metrics forwarder — the workhorse shipping side.

</div>

<div class="tool-card" markdown="1">

### [Grafana](grafana.md)

<span class="cat-badge" style="background:#5B9BD5">service</span>

Dashboards for anything with a datasource — Loki included.

</div>

<div class="tool-card" markdown="1">

### [Vector](vector.md)

<span class="cat-badge" style="background:#5B9BD5">system</span>

Observability data pipeline — route logs/metrics between anything.

</div>

<div class="tool-card" markdown="1">

### [Loki](loki.md)

<span class="cat-badge" style="background:#5B9BD5">binary</span>

Grafana's log-aggregation backend, indexed by label not full text.

</div>

<div class="tool-card" markdown="1">

### [Splunk Universal Forwarder](splunk-universal-forwarder.md)

<span class="cat-badge" style="background:#5B9BD5">manual</span>

Requires a splunk.com login, so it can't be fetched during the build.

</div>

<div class="tool-card" markdown="1">

### [Elastic + Kibana](elastic-kibana.md)

<span class="cat-badge" style="background:#5B9BD5">compose</span>

Not pre-pulled (multi-GB images) — a ready compose file is staged instead.

</div>

<div class="tool-card" markdown="1">

### [OpenSearch + Dashboards](opensearch-dashboards.md)

<span class="cat-badge" style="background:#5B9BD5">compose</span>

Same policy as Elastic — staged compose, pulled on demand.

</div>

<div class="tool-card" markdown="1">

### [Wazuh](wazuh.md)

<span class="cat-badge" style="background:#5B9BD5">compose</span>

Open-source XDR/SIEM. Upstream's own compose changes per release, so it's fetched fresh rather than pinned stale.

</div>

<div class="tool-card" markdown="1">

### [Graylog](graylog.md)

<span class="cat-badge" style="background:#5B9BD5">compose</span>

Log management on Mongo + OpenSearch — staged compose, pulled on demand.

</div>

<div class="tool-card" markdown="1">

### [Arkime](arkime.md)

<span class="cat-badge" style="background:#5B9BD5">compose</span>

Full packet-capture search-and-analysis system.

</div>

</div>
