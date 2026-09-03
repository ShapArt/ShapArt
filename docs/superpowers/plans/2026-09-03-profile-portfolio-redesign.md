# ShapArt Profile Portfolio Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an authored editorial GitHub profile with local project artwork and a self-updating "Recently shipped" section, while keeping the profile readable, truthful and recruiter-friendly.

**Architecture:** Static profile content and local SVG identity assets live in the profile repository. A small standard-library Python updater queries GitHub's API for four selected public repositories and rewrites only one marker-bounded section of `README.md`; a scheduled GitHub Action runs it and commits only real changes. Existing snake generation remains independent.

**Tech Stack:** GitHub Markdown/HTML, SVG, Python 3 standard library, GitHub REST API, GitHub Actions, `unittest`.

**Spec:** `docs/superpowers/specs/2026-09-03-profile-portfolio-redesign-design.md`

## Global Constraints

- No fake terminal/CLI visual language.
- No typing SVG, trophy wall, visitor counter, streak score, Spotify/random quote widgets or giant UI screenshots.
- All core portfolio artwork is local SVG committed to `ShapArt/ShapArt`.
- Dynamic data is sourced only from public GitHub repositories listed in the spec.
- The updater modifies only the bytes between `<!-- RECENTLY-SHIPPED:START -->` and `<!-- RECENTLY-SHIPPED:END -->`.
- No private URLs, employee names, credentials or sensitive matrix data may be added.
- Existing contribution snake stays at the bottom and remains independently generated.

---

### Task 1: Editorial masthead and project artwork

**Files:**
- Create: `assets/masthead.svg`
- Create: `assets/projects/matrix-cleaner.svg`
- Create: `assets/projects/tessa-matrix-studio.svg`
- Create: `assets/projects/eyegate-l.svg`
- Create: `assets/projects/sh4part-vpn.svg`

**Interfaces:**
- Consumes: the visual rules in the design spec.
- Produces: five local SVG paths referenced directly by the final README.

- [ ] **Step 1: Create the masthead SVG**

Use a `viewBox="0 0 1200 220"`, a graphite base, restrained warm-white typography, one cool accent, and abstract routing/matrix lines. Text content must be limited to:

```text
SHAPART / ARTYOM SHAPOVALOV
security automation · systems · backend
PROFILE / 2026
```

No fake window controls, prompt characters, command output, progress indicators or fake metrics.

- [ ] **Step 2: Create the Matrix Cleaner project cover**

Use a `viewBox="0 0 560 250"` and depict repeated matrix rows with one bounded before/after route. Include only the project name and small descriptor `reviewable bulk changes`.

- [ ] **Step 3: Create the TESSA Matrix Studio project cover**

Use the same dimensions and type grid. Depict spreadsheet-cell geometry transitioning into route nodes. Include only the project name and descriptor `XLSX → diff → reviewed apply`.

- [ ] **Step 4: Create the EyeGate-L project cover**

Use the same dimensions and type grid. Depict a simplified iris/camera geometry intersecting an access boundary. Include only the project name and descriptor `edge vision / access control`.

- [ ] **Step 5: Create the SH4PART VPN project cover**

Use the same dimensions and type grid. Depict a restrained node/tunnel topology. Include only the project name and descriptor `provisioning / delivery / lifecycle`.

- [ ] **Step 6: Validate SVG structure**

Run a parser check against all five files:

```bash
python - <<'PY'
from pathlib import Path
import xml.etree.ElementTree as ET
for path in [Path('assets/masthead.svg'), *Path('assets/projects').glob('*.svg')]:
    ET.parse(path)
    print('OK', path)
PY
```

Expected: five `OK` lines and exit code 0.

- [ ] **Step 7: Commit**

```bash
git add assets/masthead.svg assets/projects/*.svg
git commit -m "design: add editorial profile artwork"
```

---

### Task 2: Recently shipped updater with tests

**Files:**
- Create: `scripts/update_recently_shipped.py`
- Create: `tests/test_update_recently_shipped.py`

**Interfaces:**
- Consumes: `README.md`, environment variable `GITHUB_TOKEN` (optional for local public API calls), and the four fixed public repo names.
- Produces: marker-bounded Markdown and exit code 0; writes README only when content differs.

- [ ] **Step 1: Write tests for marker replacement**

Create `tests/test_update_recently_shipped.py` with `unittest` tests covering exact preservation outside the markers, a missing-marker error, release parsing, commit fallback parsing and newest-first sorting.

Required fixture shape:

```python
SAMPLE = """before\n<!-- RECENTLY-SHIPPED:START -->\nold\n<!-- RECENTLY-SHIPPED:END -->\nafter\n"""
```

Required assertion for preservation:

```python
updated = replace_block(SAMPLE, "new")
self.assertEqual(
    updated,
    "before\n<!-- RECENTLY-SHIPPED:START -->\nnew\n<!-- RECENTLY-SHIPPED:END -->\nafter\n",
)
```

- [ ] **Step 2: Run tests and verify failure**

```bash
python -m unittest -v tests.test_update_recently_shipped
```

Expected: import failure because `scripts.update_recently_shipped` does not exist yet.

- [ ] **Step 3: Implement the updater**

Create `scripts/update_recently_shipped.py` with these public functions:

```python
def replace_block(readme: str, generated: str) -> str: ...
def item_from_release(repo: str, data: dict) -> dict: ...
def item_from_commit(repo: str, data: dict) -> dict: ...
def render_items(items: list[dict]) -> str: ...
def fetch_item(repo: str, token: str | None = None) -> dict: ...
def update_readme(path: str = "README.md", token: str | None = None) -> bool: ...
```

Use only `json`, `os`, `pathlib`, `urllib.request`, `urllib.error`, `datetime` and `typing` from the standard library.

Fixed repository list:

```python
REPOSITORIES = [
    "ShapArt/Matrtix-Cleaner",
    "ShapArt/tessa-matrix-studio",
    "ShapArt/eyegate-l-luckfox-scud",
    "ShapArt/vpn-bot-stars-hiddify",
]
```

Release endpoint: `https://api.github.com/repos/{repo}/releases/latest`. On HTTP 404, fall back to `https://api.github.com/repos/{repo}/commits?per_page=1`.

Rendered item format:

```markdown
- **[Matrix Cleaner](URL)** — `v12.4.0` · 2026-09-02 — release title
```

For fallback commits use a seven-character SHA instead of a tag. Strip release/commit titles to the first line and cap them at 90 visible characters.

- [ ] **Step 4: Run unit tests**

```bash
python -m unittest -v tests.test_update_recently_shipped
```

Expected: all tests pass.

- [ ] **Step 5: Add an idempotence test**

The test must call `replace_block` twice with the same generated block and assert the second output equals the first.

- [ ] **Step 6: Run the full test module again**

```bash
python -m unittest -v tests.test_update_recently_shipped
```

Expected: all tests pass.

- [ ] **Step 7: Commit**

```bash
git add scripts/update_recently_shipped.py tests/test_update_recently_shipped.py
git commit -m "feat: generate recently shipped profile section"
```

---

### Task 3: Rebuild README around editorial hierarchy

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: all SVG paths from Task 1 and marker contract from Task 2.
- Produces: the public GitHub profile landing page.

- [ ] **Step 1: Replace the first viewport**

Start README with the local masthead:

```html
<p align="center">
  <img src="./assets/masthead.svg" alt="ShapArt / Artyom Shapovalov" width="100%">
</p>
```

Follow with a short first-person introduction, one target-role sentence and text links to Portfolio, Resume, Certificates, HH RU profile, Telegram and email.

- [ ] **Step 2: Add the proof line**

Use one plain Markdown line, not a table or badges:

```markdown
**hours → ~10 min** OpenText bulk workflows · **#45** Alfa CTF 2026 · **3+ years** systems / automation before the current role
```

- [ ] **Step 3: Build the 2×2 selected-work grid**

Use a two-column HTML table with local project cover images. Each cell contains one image link, project title, two concise sentences and a compact stack line. Do not include the TESSA UI screenshot.

- [ ] **Step 4: Add the dynamic markers**

Insert exactly once:

```html
<!-- RECENTLY-SHIPPED:START -->
_Current release data is generated by GitHub Actions._
<!-- RECENTLY-SHIPPED:END -->
```

- [ ] **Step 5: Compress experience/security/education**

Keep Cherkizovo and NAOS outcome-driven. Keep security as grouped text. Move the long certificate list behind a `<details>` block or link to `CERTIFICATES.md`.

- [ ] **Step 6: Keep activity last**

Retain the existing contribution snake only near the bottom of README.

- [ ] **Step 7: Verify anti-patterns are absent**

Run:

```bash
python - <<'PY'
from pathlib import Path
text = Path('README.md').read_text(encoding='utf-8')
for banned in ['profile-hero.svg', 'studio-panel.webp', 'readme-typing-svg', 'github-profile-trophy', 'profile views']:
    assert banned.lower() not in text.lower(), banned
assert text.count('<!-- RECENTLY-SHIPPED:START -->') == 1
assert text.count('<!-- RECENTLY-SHIPPED:END -->') == 1
print('README structure OK')
PY
```

Expected: `README structure OK`.

- [ ] **Step 8: Generate the first live Recently shipped block**

```bash
python scripts/update_recently_shipped.py
```

Expected: README contains up to four current public items, newest first.

- [ ] **Step 9: Run updater a second time**

```bash
python scripts/update_recently_shipped.py
git diff --exit-code README.md
```

Expected: exit code 0 from `git diff --exit-code`, proving idempotence after the first generated state is committed/staged as appropriate.

- [ ] **Step 10: Commit**

```bash
git add README.md
git commit -m "docs: rebuild profile as editorial engineering portfolio"
```

---

### Task 4: Scheduled GitHub Action

**Files:**
- Create: `.github/workflows/recently-shipped.yml`
- Modify: `.github/workflows/ci.yml`

**Interfaces:**
- Consumes: `scripts/update_recently_shipped.py`.
- Produces: daily/manual README refreshes and CI coverage for updater tests.

- [ ] **Step 1: Add the scheduled workflow**

Create `.github/workflows/recently-shipped.yml`:

```yaml
name: Update Recently Shipped

on:
  schedule:
    - cron: "23 5 * * *"
  workflow_dispatch:

concurrency:
  group: recently-shipped
  cancel-in-progress: true

jobs:
  update:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Update profile releases
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: python scripts/update_recently_shipped.py
      - name: Commit changes
        run: |
          if git diff --quiet -- README.md; then
            echo "No profile update"
            exit 0
          fi
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add README.md
          git commit -m "docs: refresh recently shipped"
          git push
```

- [ ] **Step 2: Extend existing CI**

Add Python setup and this step after checkout in `.github/workflows/ci.yml`:

```yaml
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Test profile updater
        run: python -m unittest -v tests.test_update_recently_shipped
```

Keep the existing markdown link-check step.

- [ ] **Step 3: Validate YAML shape locally where available**

At minimum inspect both workflow files and confirm they each contain one `jobs:` block and the new workflow has `permissions: contents: write` only.

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/recently-shipped.yml .github/workflows/ci.yml
git commit -m "ci: keep profile releases current"
```

---

### Task 5: Final verification

**Files:**
- Verify: `README.md`
- Verify: `assets/masthead.svg`
- Verify: `assets/projects/*.svg`
- Verify: `scripts/update_recently_shipped.py`
- Verify: `.github/workflows/recently-shipped.yml`
- Verify: `.github/workflows/ci.yml`

**Interfaces:**
- Produces: evidence that the redesign renders, updates and validates without hidden dependencies.

- [ ] **Step 1: Run updater tests**

```bash
python -m unittest -v tests.test_update_recently_shipped
```

Expected: zero failures/errors.

- [ ] **Step 2: Parse every local SVG**

```bash
python - <<'PY'
from pathlib import Path
import xml.etree.ElementTree as ET
paths = [Path('assets/masthead.svg'), *sorted(Path('assets/projects').glob('*.svg'))]
assert len(paths) == 5, paths
for path in paths:
    ET.parse(path)
print('SVG OK:', len(paths))
PY
```

Expected: `SVG OK: 5`.

- [ ] **Step 3: Verify README structure and privacy-safe links**

Run the Task 3 anti-pattern check and inspect the generated Recently shipped links. All dynamic links must point to public `github.com/ShapArt/...` resources.

- [ ] **Step 4: Verify GitHub Actions**

After push, inspect the newest `CI` run and manually dispatch `Update Recently Shipped`. Require both to conclude `success` before claiming completion.

- [ ] **Step 5: Inspect rendered GitHub profile**

Open the public profile and verify the masthead is compact, the four project images appear in a two-column grid where viewport width permits, no TESSA screenshot appears, and contribution snake remains near the bottom.

- [ ] **Step 6: Final commit only if verification required fixes**

```bash
git add README.md assets scripts tests .github/workflows
 git commit -m "fix: polish profile portfolio verification issues"
```
