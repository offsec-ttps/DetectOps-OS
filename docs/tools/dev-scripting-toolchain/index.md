# Dev / Scripting Toolchain

The languages and glue everything above is written in or automated with.

<div class="tool-grid" markdown="1">

<div class="tool-card" markdown="1">

### [Python 3](python-3.md)

<span class="cat-badge" style="background:#C2A544">system</span>

pip, venv, and dev headers all included.

</div>

<div class="tool-card" markdown="1">

### [PowerShell 7](powershell-7.md)

<span class="cat-badge" style="background:#C2A544">system</span>

Cross-platform pwsh, pre-loaded with the Atomic Red Team profile.

</div>

<div class="tool-card" markdown="1">

### [Go](go.md)

<span class="cat-badge" style="background:#C2A544">system</span>

For building any of the Go-based tools from source.

</div>

<div class="tool-card" markdown="1">

### [Rust / Cargo](rust-cargo.md)

<span class="cat-badge" style="background:#C2A544">system</span>

For the Rust-based tools (Chainsaw, Hayabusa, YARA-X all began here).

</div>

<div class="tool-card" markdown="1">

### [Docker + docker-compose + Podman](docker-docker-compose-podman.md)

<span class="cat-badge" style="background:#C2A544">system</span>

Every compose-based stack above runs on the hyphenated v1 `docker-compose` — the v2 plugin isn't in Debian's own repos.

</div>

<div class="tool-card" markdown="1">

### [Git + GitHub CLI](git-github-cli.md)

<span class="cat-badge" style="background:#C2A544">system</span>

Version control, plus `gh` for working with GitHub directly.

</div>

<div class="tool-card" markdown="1">

### [Visual Studio Code](visual-studio-code.md)

<span class="cat-badge" style="background:#C2A544">system</span>

For editing Sigma rules, hooks, and everything else in this manifest.

</div>

<div class="tool-card" markdown="1">

### [jq / yq](jq-yq.md)

<span class="cat-badge" style="background:#C2A544">system</span>

Command-line JSON and YAML processors, for scripting Detection-as-Code pipelines.

</div>

</div>
