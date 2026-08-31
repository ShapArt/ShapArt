# Artyom Shapovalov

**Security Automation · SIEM/SOC · Backend · Enterprise Tooling**

5th-year Computer Security student at **BMSTU IU8**. Since February 2026 I have been working with **OpenText/TESSA** document workflows at Cherkizovo Group: approval matrices, routing, signers, legal entities, categories, limits, diagnostics and internal automation.

My main languages are **Python, JavaScript and SQL**. I work regularly with Linux, Windows, REST APIs, databases, Docker and event/log pipelines. I am most interested in systems where the hard part is understanding what can break, reducing manual work and making automation reviewable instead of opaque.

**Open to junior / internship roles in SIEM/SOC engineering, security automation, AppSec and security-minded backend development.**

[Portfolio](PORTFOLIO.md) · [Resume](RESUME.md) · [Certificates](CERTIFICATES.md) · [Telegram](https://t.me/shapart) · [Email](mailto:artem.shapovalov2003@gmail.com)

---

## Selected projects

### [OpenText Toolkit / Matrix Cleaner](https://github.com/ShapArt/Matrtix-Cleaner)

A Tampermonkey operator toolkit for real OpenText approval matrices, tickets and change requests.

It grew from a small helper into a safety-oriented automation layer: it understands request scope, inspects matrix context, builds a concrete change plan, shows which rows will be affected, blocks ambiguous cases and applies only reviewed operations.

Typical covered bulk changes that previously required hours of repetitive row-by-row work can now be prepared and completed in roughly **10 minutes**. The tool is used in daily OpenText work by me and a senior specialist.

`JavaScript · Tampermonkey · Playwright · browser automation · regression testing`

### [TESSA Matrix Studio](https://github.com/ShapArt/tessa-matrix-studio)

Excel round-trip editor for TESSA approval matrices.

`TESSA → XLSX → edit → exact diff → review → safe apply`

The project preserves row identity and baseline data, translates Excel changes into an explicit plan and re-checks live state before applying anything. The point is to make bulk editing convenient without turning it into blind mutation.

`JavaScript · XLSX workflows · diff planning · CI/release engineering`

### [EyeGate-L](https://github.com/ShapArt/eyegate-l-luckfox-scud)

Edge computer-vision access-control prototype for LuckFox-class hardware with local processing, GPIO integration and separation between recognition/decision logic and the physical lock action.

`Python · OpenCV · edge AI · local-first processing`

### [SH4PART VPN](https://github.com/ShapArt/vpn-bot-stars-hiddify)

Telegram-first backend that connects payment/user state with access provisioning and profile delivery.

`Python · FastAPI · SQLite · Telegram Bot API · Hiddify/Xray · nginx · systemd`

### [SLA / Outlook Toolkit](https://github.com/ShapArt/outlook-exporter)

Windows/Office automation for Outlook/Graph data, SQLite storage, Excel reporting and deadline tracking. Built from recurring operational work during my systems-administration role.

`Python · pywin32 · Microsoft Graph · SQLite · pandas · openpyxl`

More shipped work and quantified cases: [cases-and-achievements](https://github.com/ShapArt/cases-and-achievements)

---

## Experience

### Cherkizovo Group — Document Workflow Automation
**February 2026 — present**

I support OpenText/TESSA document approval workflows and investigate non-standard cases: why a route was built a certain way, why a signer appeared or did not appear, and how matrix conditions interact.

My work includes:

- configuring approval matrices and routes;
- approvers, signers and approval stages;
- legal entities, categories, document types, sites and limits;
- user incidents and routing diagnostics;
- comparing document cards and approval sheets;
- SQL/data checks, exports and operational reports;
- JavaScript/Python automation around repetitive work;
- development of OpenText Toolkit / Matrix Cleaner and TESSA Matrix Studio.

### NAOS Vostok — Systems Administrator
**November 2022 — February 2026**

Worked with Windows workplaces, Microsoft 365, Intune, device policies, user access, Windows Server tasks, services and remote access.

Alongside administration I automated recurring operations: Outlook/Excel exports, reporting, browser workflows, Power Automate flows and SLA tracking. One of the internal trackers stored Outlook/Graph data in SQLite, exported it to Excel and used it for deadline reminders.

---

## Security practice

My degree is in computer security, and I try to keep that part practical.

- **MaxPatrol SIEM** — event delivery, source diagnostics, event parsing and investigation;
- **Windows telemetry** — Event Logs, authentication/RDP events, Sysmon concepts;
- **Linux** — services, permissions, networking, logs, auditd/syslog-style pipelines;
- **network data** — NetFlow and traffic/log-analysis exercises;
- **AppSec** — authentication/authorization, secrets, safe defaults, failure modes and OWASP-oriented thinking;
- **automation safety** — preview/dry-run, explicit scope, auditability, bounded changes and verification;
- **CTF** — web, crypto, reverse and general security problem solving.

**Alfa CTF 2026 — 45th place.**

---

## Stack

**Programming:** Python, JavaScript, SQL, C++, Shell, HTML/CSS  
**Backend & data:** FastAPI, REST APIs, PostgreSQL, SQLite, pandas, openpyxl  
**Systems:** Linux, Docker, nginx, systemd, Git, Windows, Microsoft 365, Intune  
**Security:** MaxPatrol SIEM, Windows Event Logs, NetFlow, log parsing, AAA, RDP, iptables, OSINT  
**Automation & CV:** Tampermonkey, Playwright, pywin32, Power Automate, OpenCV

---

## Education and certificates

**BMSTU IU8** — Computer Security, 10.05.01, 5th year  
**BMSTU Digital Department** — Web Developer, 2024  
**VK Education** — Application Security / AppSec, 2025

Selected certificates:

- [DevOps простым языком](https://stepik.org/cert/3328074)
- [Доверенный искусственный интеллект](https://stepik.org/cert/3328089)
- [Специалист по противодействию кибератакам](https://stepik.org/cert/3328110)
- [Введение в SQL](https://stepik.org/cert/2937373)
- [Введение в информационную безопасность аппаратных решений](https://stepik.org/cert/2945060)
- [Теория вероятностей](https://stepik.org/cert/2945135)

Full list: [CERTIFICATES.md](CERTIFICATES.md)

---

## How I work

I prefer automation that is understandable before it is fast.

`understand → define scope → preview → review/test → apply → verify`

I use ChatGPT, Codex, Cursor and Claude as engineering tools, but changes still go through diffs, tests, manual review and verification.

---

## GitHub activity

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ShapArt/ShapArt/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/ShapArt/ShapArt/output/github-contribution-grid-snake.svg">
    <img alt="ShapArt contribution activity" src="https://raw.githubusercontent.com/ShapArt/ShapArt/output/github-contribution-grid-snake.svg" />
  </picture>
</p>

---

## По-русски

Я Артём Шаповалов, студент 5 курса ИУ8 МГТУ им. Н. Э. Баумана по специальности «Компьютерная безопасность».

С февраля 2026 работаю в Черкизово с OpenText/TESSA: сопровождаю согласование документов, настраиваю матрицы и маршруты, разбираю сложные заявки и пишу внутренние инструменты на JavaScript, Python и SQL. Разработал OpenText Toolkit / Matrix Cleaner — инструмент для контролируемых массовых изменений, который сократил типовые операции с часов ручной работы примерно до 10 минут.

До этого больше трёх лет работал системным администратором: Windows, Microsoft 365, Intune, Windows Server, автоматизация Outlook/Excel, Power Automate и SLA-трекинг.

Сейчас развиваюсь в SIEM/SOC, security automation и AppSec. Есть практический опыт с MaxPatrol SIEM, журналами Windows/Linux, NetFlow и диагностикой источников.
