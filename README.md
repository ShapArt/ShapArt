<p align="center">
  <img src="./assets/masthead.svg" alt="ShapArt / Artyom Shapovalov" width="100%">
</p>

# Artyom Shapovalov

**Security automation · SIEM/SOC · backend · internal tools**

I work on the awkward boundary between enterprise systems, security controls and manual operations. Most of my projects start with the same question: **what is taking people too long, and how do I automate it without hiding what the tool is about to change?**

I am a 5th-year Computer Security student at **BMSTU IU8** and currently work with **OpenText/TESSA at Cherkizovo**. My main languages are Python, JavaScript and SQL; day to day I also work with Linux, Windows, databases, REST APIs, logs and automation around existing systems.

I am looking at junior roles and internships around **SIEM/SOC engineering, security automation, AppSec and security-minded backend work**.

[Portfolio](PORTFOLIO.md) · [Resume](RESUME.md) · [Certificates](CERTIFICATES.md) · [HH / RU master profile](HH_RU_PROFILE.txt) · [Telegram](https://t.me/shapart) · [Email](mailto:artem.shapovalov2003@gmail.com)

**hours → ~10 min** OpenText bulk workflows · **#45** Alfa CTF 2026 · **3+ years** systems / automation before the current role

---

## Selected work

<table>
<tr>
<td width="50%" valign="top">

<a href="https://github.com/ShapArt/Matrtix-Cleaner">
  <img src="./assets/projects/matrix-cleaner.svg" alt="OpenText Toolkit / Matrix Cleaner" width="100%">
</a>

### [OpenText Toolkit / Matrix Cleaner](https://github.com/ShapArt/Matrtix-Cleaner)

An operator layer for approval matrices and support requests. It parses scope, builds an explicit change plan, shows affected rows and applies only reviewed operations.

Typical covered bulk changes went from hours of repetitive UI work to roughly **10 minutes**.

`JavaScript · Tampermonkey · Playwright`

</td>
<td width="50%" valign="top">

<a href="https://github.com/ShapArt/tessa-matrix-studio">
  <img src="./assets/projects/tessa-matrix-studio.svg" alt="TESSA Matrix Studio" width="100%">
</a>

### [TESSA Matrix Studio](https://github.com/ShapArt/tessa-matrix-studio)

An XLSX round-trip editor for TESSA approval matrices: export, edit, exact diff, review, controlled apply.

The interesting constraint is identity: the tool preserves baseline data and checks the live matrix before it writes anything.

`JavaScript · XLSX · CI / release tooling`

</td>
</tr>
<tr>
<td width="50%" valign="top">

<a href="https://github.com/ShapArt/eyegate-l-luckfox-scud">
  <img src="./assets/projects/eyegate-l.svg" alt="EyeGate-L" width="100%">
</a>

### [EyeGate-L](https://github.com/ShapArt/eyegate-l-luckfox-scud)

Edge computer-vision access-control prototype for LuckFox-class hardware. Local inference, GPIO integration and a deliberate boundary between recognition logic and the physical lock action.

`Python · OpenCV · edge / local-first`

</td>
<td width="50%" valign="top">

<a href="https://github.com/ShapArt/vpn-bot-stars-hiddify">
  <img src="./assets/projects/sh4part-vpn.svg" alt="SH4PART VPN" width="100%">
</a>

### [SH4PART VPN](https://github.com/ShapArt/vpn-bot-stars-hiddify)

Telegram-first backend that connects payment / entitlement state with provisioning, profile delivery and lifecycle reminders.

`Python · FastAPI · SQLite · Hiddify/Xray · nginx · systemd`

</td>
</tr>
</table>

More shipped work and quantified cases: [cases-and-achievements](https://github.com/ShapArt/cases-and-achievements)

---

## Recently shipped

<!-- RECENTLY-SHIPPED:START -->
- **[Matrix Cleaner](https://github.com/ShapArt/Matrtix-Cleaner/releases/tag/v12.4.0)** — `v12.4.0` · 2026-09-02 — 12.4.0 — панель, которая закрывается, и заявка, которая разбирается
- **[TESSA Matrix Studio](https://github.com/ShapArt/tessa-matrix-studio/releases/tag/v1.9.51)** — `v1.9.51` · 2026-09-02 — TESSA Matrix Studio v1.9.51
- **[SH4PART VPN](https://github.com/ShapArt/vpn-bot-stars-hiddify/commit/533797d074e51592141899f002f429651667dfc6)** — `533797d` · 2026-04-28 — Upgrade README to senior-level portfolio version
- **[EyeGate-L](https://github.com/ShapArt/eyegate-l-luckfox-scud/commit/2d2698d1c388a0071b5705756e9068193019ec5c)** — `2d2698d` · 2026-04-27 — Refine README for edge CV prototype
<!-- RECENTLY-SHIPPED:END -->

This block is refreshed from public releases / commits by GitHub Actions.

---

## Experience

### Cherkizovo Group — document workflow automation
**February 2026 — present**

I support OpenText/TESSA approval workflows: matrices, routes, signers, legal entities, categories, document types, sites, limits and the odd cases where the route does not behave the way the requester expected.

Alongside support work I build tools around repetitive and risky operations. **Matrix Cleaner** and **TESSA Matrix Studio** both came from that work: preview the exact change, keep scope visible, refuse ambiguous cases, then verify what actually happened.

### NAOS Vostok — systems administrator
**November 2022 — February 2026**

Windows workplaces, Microsoft 365, Intune, device policies, access, Windows Server tasks and day-to-day support. I also automated Outlook / Excel / browser routines, built Power Automate / Power BI reporting flows and an SLA tracker around Outlook/Graph → SQLite → Excel → deadline reminders.

---

## Security / systems

**SIEM & telemetry:** MaxPatrol SIEM, Windows Event Logs, authentication / RDP events, Sysmon concepts, NetFlow, log parsing, source diagnostics, Linux logs, auditd / syslog-style pipelines.

**Programming & backend:** Python, JavaScript, SQL, FastAPI, REST APIs, PostgreSQL, SQLite, pandas, openpyxl.

**Systems & automation:** Linux, Windows, Docker, nginx, systemd, Git, Microsoft 365, Intune, Tampermonkey, Playwright, pywin32, Power Automate.

**Security mindset:** authentication / authorization, secret handling, explicit scope, preview / dry-run, auditability, safe failure modes and post-action verification.

---

## Education / evidence

**BMSTU IU8** — 10.05.01 Computer Security · 5th year  
**VK Education** — Application Security / AppSec · 2025  
**BMSTU Digital Department** — Web Developer · 2024  
**Alfa CTF 2026** — 45th place

<details>
<summary><strong>Selected certificates</strong></summary>
<br>

- [DevOps простым языком](https://stepik.org/cert/3328074)
- [Доверенный искусственный интеллект](https://stepik.org/cert/3328089)
- [Специалист по противодействию кибератакам](https://stepik.org/cert/3328110)
- [Введение в SQL](https://stepik.org/cert/2937373)
- [Введение в информационную безопасность аппаратных решений](https://stepik.org/cert/2945060)
- [Теория вероятностей](https://stepik.org/cert/2945135)

Full list: [CERTIFICATES.md](CERTIFICATES.md)

</details>

---

## Activity

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ShapArt/ShapArt/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/ShapArt/ShapArt/output/github-contribution-grid-snake.svg">
    <img alt="ShapArt contribution activity" src="https://raw.githubusercontent.com/ShapArt/ShapArt/output/github-contribution-grid-snake.svg">
  </picture>
</p>

<details>
<summary><strong>По-русски</strong></summary>
<br>

Я Артём Шаповалов, студент 5 курса ИУ8 МГТУ им. Н. Э. Баумана по специальности «Компьютерная безопасность».

С февраля 2026 работаю в Черкизово с OpenText/TESSA: сопровождаю процессы согласования документов, разбираю матрицы и маршруты, пользовательские заявки и нетиповые случаи. Параллельно пишу внутренние инструменты на JavaScript, Python и SQL. OpenText Toolkit / Matrix Cleaner сократил типовые массовые операции с часов ручной работы примерно до 10 минут.

До этого больше трёх лет работал системным администратором с Windows, Microsoft 365, Intune, Windows Server и автоматизацией Outlook / Excel-процессов.

Сейчас двигаюсь в сторону SIEM/SOC, security automation и AppSec. Есть практический опыт с MaxPatrol SIEM, журналами Windows/Linux, NetFlow и диагностикой источников.

</details>
