<div align="center">

# Artyom Shapovalov · `ShapArt`

### Cybersecurity · Security Automation · Backend · Enterprise Tooling

**5th-year Computer Security student @ BMSTU IU8** · **Cherkizovo Infotech since February 2026**

[![BMSTU](https://img.shields.io/badge/BMSTU_IU8-Computer_Security-111111?style=flat-square)](https://bmstu.ru/)
![Work](https://img.shields.io/badge/Cherkizovo_Infotech-since_Feb_2026-111111?style=flat-square)
[![CTF](https://img.shields.io/badge/Alpha_CTF_2026-Top_10%25-111111?style=flat-square)](#achievements--education)
[![VK Education](https://img.shields.io/badge/VK_Education-AppSec_2025-111111?style=flat-square)](#achievements--education)

[Portfolio](PORTFOLIO.md) · [Resume](RESUME.md) · [Cases](https://github.com/ShapArt/cases-and-achievements) · [Telegram](https://t.me/shapart) · [Email](mailto:sh4part@gmail.com)

</div>

---

I build tools for places where **real systems, manual operations, security boundaries, and messy data meet**.

Right now I work with OpenText/TESSA document workflows at **Cherkizovo Infotech**: approval matrices, routing, signers, categories, legal entities, user incidents, diagnostics, exports, and safe bulk changes. I like getting into unfamiliar systems, finding the awkward manual parts, and pushing a solution until it is useful every day — not just good enough for a demo.

My core stack is **Python · JavaScript · SQL**, with regular Linux work and practical experience around REST APIs, databases, containers, Windows/Linux event pipelines, logs, and SIEM-oriented diagnostics.

> **Open to:** junior / internship roles around **security automation, backend, AppSec, SOC engineering, internal tooling, and infrastructure-minded development**.

## Flagship work

### 01 · OpenText Toolkit / Matrix Cleaner

**Enterprise browser automation for approval matrices and operator workflows.**

[![Repository](https://img.shields.io/badge/repo-Matrtix--Cleaner-24292f?style=flat-square&logo=github)](https://github.com/ShapArt/Matrtix-Cleaner)
[![JavaScript](https://img.shields.io/badge/JavaScript-Tampermonkey-24292f?style=flat-square&logo=javascript)](https://github.com/ShapArt/Matrtix-Cleaner)

What started as a helper for repetitive matrix changes grew into an operator layer around OpenText: request parsing, matrix inspection, preview plans, guarded apply, row fingerprint checks, ambiguity handling, reconciliation, knowledge-base assistance, and test-heavy regression control.

The important part is not “editing rows faster”. It is **making risky enterprise changes inspectable before anything is written**.

`request / ticket → understand scope → preview exact plan → operator review → guarded apply → log / verify`

**Why I feature it first:** this is the project that best represents how I work — understand a complicated existing system, measure the failure modes, automate the boring parts, and keep the dangerous parts bounded.

---

### 02 · TESSA Matrix Studio

**Excel round-trip editor for TESSA approval matrices.**

[![Version](https://img.shields.io/github/v/release/ShapArt/tessa-matrix-studio?style=flat-square&label=release)](https://github.com/ShapArt/tessa-matrix-studio/releases/latest)
[![Quality](https://github.com/ShapArt/tessa-matrix-studio/actions/workflows/quality.yml/badge.svg)](https://github.com/ShapArt/tessa-matrix-studio/actions/workflows/quality.yml)
[![Repository](https://img.shields.io/badge/repo-tessa--matrix--studio-24292f?style=flat-square&logo=github)](https://github.com/ShapArt/tessa-matrix-studio)

`TESSA → XLSX export → bulk edit → exact diff → review → safe apply`

The Studio turns a matrix into an editable `.xlsx`, preserves row identity, builds a reviewable change plan, performs fresh checks before writing, and blocks unsafe/ambiguous operations instead of guessing.

<div align="center">
  <a href="https://github.com/ShapArt/tessa-matrix-studio">
    <img src="https://raw.githubusercontent.com/ShapArt/tessa-matrix-studio/main/docs/assets/studio-panel.webp" alt="TESSA Matrix Studio interface" width="720">
  </a>
  <br><sub>Real TESSA Matrix Studio operator panel</sub>
</div>

---

### 03 · EyeGate-L

**Edge computer-vision access-control prototype for LuckFox hardware.**

[![Repository](https://img.shields.io/badge/repo-eyegate--l--luckfox--scud-24292f?style=flat-square&logo=github)](https://github.com/ShapArt/eyegate-l-luckfox-scud)

Local CV/access-control prototype focused on constrained hardware, local processing, GPIO integration and security-sensitive boundaries. The design keeps the recognition/decision path separated from the physical lock action and avoids making cloud availability part of the access decision.

---

### 04 · SH4PART VPN

**Telegram-first backend around subscription provisioning and delivery.**

[![Repository](https://img.shields.io/badge/repo-vpn--bot--stars--hiddify-24292f?style=flat-square&logo=github)](https://github.com/ShapArt/vpn-bot-stars-hiddify)

Python/FastAPI service connecting Telegram UX with payment state, HMAC-backed subscription links, SQLite state, Hiddify/Xray provisioning, reminders, nginx and systemd deployment.

---

### 05 · SLA / Outlook Toolkit

**Windows/Office automation for mailbox-driven operational work.**

[![Repository](https://img.shields.io/badge/repo-outlook--exporter-24292f?style=flat-square&logo=github)](https://github.com/ShapArt/outlook-exporter)

`pywin32 · pandas · openpyxl · PySide6 · Tampermonkey`

Turns Outlook/Excel-heavy work into structured exports, status tracking and repeatable reporting instead of copy-paste operations.

## Experience

### Cherkizovo Infotech · Document Workflow Automation
**February 2026 — Present**

- Support OpenText/TESSA document approval processes and investigate non-standard user incidents.
- Configure and analyse approval matrices and routes: signers, functions, categories, legal entities, sites and other routing conditions.
- Build internal JavaScript/Python/Excel tools for validation, exports, preparation and controlled application of changes.
- Developed **OpenText Toolkit / Matrix Cleaner** and **TESSA Matrix Studio** from real operator pain points.
- Automation around recurring workflow operations removes **up to ~4 hours of manual work per day** in the tasks it covers.
- Work with a **preview-before-action** mindset: explicit scope, conflict checks, reviewable diffs, logs and predictable failure behaviour.

### NAOS Vostok · Systems Administration / Support / Automation
**November 2022 — January 2026**

- Windows workstations, services, networking, user support and operational troubleshooting.
- Microsoft 365 and day-to-day workplace administration.
- Automated Outlook/Excel exports, ticket/status reporting and repetitive CMS/seller-interface tasks.
- Built small Windows/browser helpers instead of leaving recurring manual procedures undocumented.

## Security practice

My degree is in computer security, but I try to keep the security part practical rather than badge-only.

- **SIEM / logs:** hands-on event/source diagnostics, Windows Event Logs, Sysmon, syslog, NetFlow and event normalization/correlation concepts.
- **MaxPatrol SIEM:** practical work with event collection/source diagnostics and log analysis concepts.
- **Windows telemetry:** WEF/WEC, Security/EventLog channels, authentication/RDP/PowerShell events.
- **Linux telemetry:** auditd, rsyslog/syslog pipelines and source-side troubleshooting.
- **AppSec mindset:** secrets, permissions, safe defaults, dry-run/preview, bounded mutation, failure modes and auditability.
- **CTF practice:** web, crypto, reverse and general security problem solving.

## Stack

**Core:** Python · JavaScript · SQL · Git · Linux  
**Backend:** FastAPI · REST APIs · SQLAlchemy · PostgreSQL · SQLite · Telegram Bot API  
**Automation/data:** Playwright · Tampermonkey · pywin32 · pandas · openpyxl · PySide6  
**Infra:** Docker / Compose · nginx · systemd · Windows administration · Microsoft 365  
**Security:** logs / SIEM foundations · WEF/WEC · Sysmon · auditd · syslog · OWASP/AppSec foundations  
**Domain:** OpenText · TESSA · approval/routing systems · operator tooling

## Achievements & education

- 🎓 **BMSTU, IU8** — 10.05.01 Computer Security, specialist degree, **5th year**.
- 🌐 **BMSTU Digital Department** — Web Developer, **2024**.
- 🛡️ **VK Education** — Application Security / AppSec, **2025**.
- 🚩 **Alpha CTF 2026** — **top 10% among 2000+ teams**.
- 🧊 **Arctic Probe 2020 / Skolkovo** — winner of an engineering-project competition with an Arctic buoy prototype.
- 🧠 **ICCETT / Quantoriada** — finalist with a Python-based psycho-emotional training project.

### Selected Stepik coursework

- Introduction to Information Security of Hardware Solutions
- Introduction to SQL
- Probability Theory
- Specialist in Countering Cyberattacks
- AI Threat Team: Security of AI Systems
- Trusted Artificial Intelligence

## How I work

I use AI tools heavily — ChatGPT, Codex, Cursor, Claude — but as an **engineering workflow**, not as a substitute for verification:

`understand → plan → diff → test → inspect → run → verify`

That pattern is also how I approach automation in general. If an action is risky, I would rather expose the uncertainty and ask for review than make a fast silent guess.

## GitHub activity

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ShapArt/ShapArt/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/ShapArt/ShapArt/output/github-contribution-grid-snake.svg">
    <img alt="ShapArt contribution animation" src="https://raw.githubusercontent.com/ShapArt/ShapArt/output/github-contribution-grid-snake.svg">
  </picture>
</p>

<details>
<summary><strong>Коротко по-русски</strong></summary>
<br>

Я Артём Шаповалов, студент 5 курса ИУ8 МГТУ им. Н. Э. Баумана по специальности «Компьютерная безопасность».

С февраля 2026 работаю в «Черкизово Инфотех» с OpenText/TESSA: сопровождаю процессы согласования документов, настраиваю и анализирую матрицы и маршруты, разбираю пользовательские обращения и пишу внутренние инструменты на JavaScript/Python/Excel. Главные публичные проекты сейчас — **OpenText Toolkit / Matrix Cleaner**, **TESSA Matrix Studio**, **EyeGate-L**, **SH4PART VPN** и **SLA / Outlook Toolkit**.

Больше всего мне нравится разбираться в незнакомых системах, находить ручные и неудобные участки и доводить автоматизацию до состояния, когда ей можно пользоваться каждый день. Ищу junior / internship возможности в security automation, backend, AppSec/SOC engineering и internal tooling.

</details>

---

<div align="center">

**[github.com/ShapArt](https://github.com/ShapArt) · [@shapart](https://t.me/shapart) · [sh4part@gmail.com](mailto:sh4part@gmail.com)**

</div>
