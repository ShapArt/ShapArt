# Artyom Shapovalov — Engineering Portfolio

**Cybersecurity · Security Automation · Backend · Enterprise Tooling**

I build practical software around workflows that are repetitive, fragile, security-sensitive or buried inside existing enterprise interfaces.

My strongest work is not isolated demo code. It is tooling around real systems: OpenText/TESSA approval matrices, browser-side operator workflows, Excel round-trips, Outlook automation, backend services, event/log pipelines and edge/CV prototypes.

## Current profile

- **Education:** BMSTU, IU8, 10.05.01 Computer Security — 5th year
- **Current work:** Cherkizovo Infotech, document workflow automation — since February 2026
- **Core languages:** Python, JavaScript, SQL
- **Main direction:** security-minded automation, backend, internal tools and operator tooling
- **Open to:** junior / internship roles in security automation, backend, AppSec, SOC engineering and internal tooling

## Portfolio map

### Tier 1 — flagship work

| Project | Area | What it demonstrates |
|---|---|---|
| [OpenText Toolkit / Matrix Cleaner](https://github.com/ShapArt/Matrtix-Cleaner) | Enterprise browser automation | Understanding a risky legacy workflow, request parsing, preview-before-apply, guarded mutation, ambiguity handling, regression control |
| [TESSA Matrix Studio](https://github.com/ShapArt/tessa-matrix-studio) | TESSA / Excel round-trip | Product-like operator UX, exact diff planning, preserved row identity, safe apply, releases and CI |
| [EyeGate-L / LuckFox SCUD](https://github.com/ShapArt/eyegate-l-luckfox-scud) | Edge / CV / access control | Constrained hardware, local processing, physical-system boundaries and security-oriented design |
| [SH4PART VPN](https://github.com/ShapArt/vpn-bot-stars-hiddify) | Backend / Telegram / infrastructure | Payment/user state, provisioning, subscription delivery and Linux deployment |
| [SLA / Outlook Toolkit](https://github.com/ShapArt/outlook-exporter) | Windows / Office automation | pywin32, Outlook/Excel data pipelines, reporting and recurring operational automation |

### Tier 2 — supporting public work

The rest of the profile includes smaller utilities, bots, academic repositories and experiments. They are useful evidence of range, but the five projects above are the best starting point for a technical review.

## 01 · OpenText Toolkit / Matrix Cleaner

**Repository:** [ShapArt/Matrtix-Cleaner](https://github.com/ShapArt/Matrtix-Cleaner)

### Problem

Approval matrices are large, repetitive and deceptively risky. Similar rows can differ in legal entities, sites, categories, document types, signer roles or amount limits. A fast but incorrect mass edit can create routing failures that surface much later.

### Solution

A Tampermonkey-based operator layer around OpenText that adds a controlled workflow instead of blind automation:

1. inspect context;
2. parse the request;
3. resolve scope and ambiguity;
4. build a concrete preview plan;
5. let the operator review it;
6. re-check the target before writing;
7. apply only the approved scope;
8. log and verify the result.

The current toolkit also covers ticket/request assistance, route roles, signers, matrix reconciliation, knowledge-base support and regression tests built from real failure cases.

### Why it matters

This is the strongest example of my engineering approach: **automation should reduce routine without hiding operational risk**.

## 02 · TESSA Matrix Studio

**Repository:** [ShapArt/tessa-matrix-studio](https://github.com/ShapArt/tessa-matrix-studio)

### Problem

Large TESSA approval matrices are much easier to edit as structured tabular data than through many individual UI operations — but an Excel workflow becomes dangerous if row identity and the live state of the matrix are lost.

### Solution

A round-trip workflow:

`TESSA → XLSX → edits → exact diff → operator review → fresh validation → apply`

The export carries hidden identity/baseline data, the preview translates spreadsheet changes into explicit operations, and the write path re-checks the live matrix before applying the approved plan.

### Product layer

The project is maintained with versioned releases, quality/security CI, installable Tampermonkey artifacts, documentation and a production runbook. It is intentionally closer to a small internal product than a one-off script.

## 03 · EyeGate-L / LuckFox SCUD

**Repository:** [ShapArt/eyegate-l-luckfox-scud](https://github.com/ShapArt/eyegate-l-luckfox-scud)

Edge-focused access-control prototype for constrained LuckFox hardware.

The project combines computer vision, local processing, GPIO/hardware interaction and security-sensitive separation between recognition/decision logic and the physical lock action.

**What it demonstrates:** embedded-style constraints, CV, local-first architecture and thinking about what should happen when dependencies fail.

## 04 · SH4PART VPN

**Repository:** [ShapArt/vpn-bot-stars-hiddify](https://github.com/ShapArt/vpn-bot-stars-hiddify)

Telegram-first backend around a complete subscription delivery path rather than only a chatbot UI.

Typical path:

`payment / user state → entitlement → provisioning → signed profile delivery → reminders / support`

**Stack:** Python, FastAPI, Telegram Bot API, SQLite, Hiddify/Xray, nginx, systemd.

**What it demonstrates:** backend state, integration-heavy delivery, secret/token boundaries and deployment outside a local development machine.

## 05 · SLA / Outlook Toolkit

**Repository:** [ShapArt/outlook-exporter](https://github.com/ShapArt/outlook-exporter)

Windows-first automation around Outlook/Excel operational data.

**Stack:** Python, pywin32, pandas, openpyxl, PySide6, Tampermonkey.

The project represents an older but important part of my portfolio: noticing repetitive office operations, extracting the real data model from them and turning copy-paste work into repeatable tooling.

## Professional experience

### Cherkizovo Infotech — Document Workflow Automation
**February 2026 — Present**

I support OpenText/TESSA document approval processes and work with matrices, routes, signers, categories, legal entities, sites, card data and user incidents.

Typical engineering work includes:

- tracing why a document received an unexpected route;
- checking how matrix conditions interact;
- preparing large signer/site/category changes;
- comparing planned and actual matrix state;
- building JavaScript/Python/Excel utilities around repetitive work;
- turning recurring support patterns into diagnostics or operator tools;
- keeping changes reviewable when a mistake would affect later documents.

The automation built around these tasks removes **up to ~4 hours of manual work per day** in the workflows it covers.

### NAOS Vostok — Systems Administration / Support / Automation
**November 2022 — January 2026**

Worked with Windows workplaces, user support, services/network troubleshooting and Microsoft 365. Repetitive Outlook/Excel reporting, CMS and seller-interface operations became small scripts and browser helpers rather than permanent manual procedures.

## Security practice

Security is both my academic direction and a layer I apply to engineering work.

### Logs / SIEM

- MaxPatrol SIEM: event collection/source diagnostics and event-analysis concepts;
- Windows Event Logs and Sysmon;
- WEF/WEC event forwarding;
- authentication, RDP and PowerShell event investigation;
- Linux auditd and rsyslog/syslog pipelines;
- NetFlow, syslog and PCAP exercises;
- normalization/correlation and source-side troubleshooting.

### AppSec / safe automation

- secrets and token handling;
- permission boundaries;
- input validation;
- safe defaults and fail-closed behaviour where appropriate;
- dry-run / preview before mutation;
- explicit operator confirmation for destructive or ambiguous operations;
- logs, reproducibility and post-action verification.

## Education & achievements

### BMSTU IU8

**10.05.01 Computer Security — specialist degree, 5th year**

Academic base includes computer networks, databases, embedded systems, cryptography/security disciplines, DSP and applied ML/CV/NLP coursework.

### Additional education

- **BMSTU Digital Department — Web Developer**, 2024
- **VK Education — Application Security / AppSec**, 2025
- Selected Stepik coursework:
  - Introduction to Information Security of Hardware Solutions
  - Introduction to SQL
  - Probability Theory
  - Specialist in Countering Cyberattacks
  - AI Threat Team: Security of AI Systems
  - Trusted Artificial Intelligence

### Achievements

- **Alpha CTF 2026 — top 10% among 2000+ teams**
- **Arctic Probe 2020 / Skolkovo — winner**, engineering prototype of an Arctic buoy
- **ICCETT / Quantoriada — finalist**, Python-based psycho-emotional training project

## Stack map

### Core
Python · JavaScript · SQL · Git · Linux

### Backend
FastAPI · REST APIs · SQLAlchemy · PostgreSQL · SQLite · Telegram Bot API

### Automation / data
Playwright · Tampermonkey · pywin32 · pandas · openpyxl · PySide6

### Infrastructure
Docker / Compose · nginx · systemd · Windows administration · Microsoft 365

### Security
SIEM/log analysis foundations · MaxPatrol SIEM · WEF/WEC · Sysmon · auditd · syslog · AppSec/OWASP foundations

### Enterprise domain
OpenText · TESSA · approval/routing matrices · document workflows · operator tooling

## Engineering approach

I like systems where the difficult part is not writing a function, but understanding **what must not break**.

My preferred pattern is:

`understand → measure → model scope → preview → review → apply → verify`

I use AI coding tools in the same way: useful for exploration and implementation speed, but changes still go through diffs, tests, manual review and verification.

## Notes on confidentiality

Some work touches internal enterprise processes. Public repositories and case studies intentionally describe the engineering shape without publishing credentials, private URLs, employee data or sensitive business configuration.

## RU

Я Артём Шаповалов, студент 5 курса ИУ8 МГТУ им. Н. Э. Баумана по специальности «Компьютерная безопасность».

С февраля 2026 работаю в «Черкизово Инфотех» с OpenText/TESSA. Сопровождаю процессы согласования документов, разбираю маршруты и матрицы, пользовательские обращения и нетипичные случаи. Параллельно пишу инструменты на JavaScript/Python/Excel, которые убирают ручную рутину и делают массовые изменения проверяемыми.

Главные проекты: **OpenText Toolkit / Matrix Cleaner**, **TESSA Matrix Studio**, **EyeGate-L**, **SH4PART VPN** и **SLA / Outlook Toolkit**.
