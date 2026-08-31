# Artyom Shapovalov

**Information Security · Security Automation · SIEM/SOC · Backend**

Moscow · [GitHub](https://github.com/ShapArt) · [Telegram @shapart](https://t.me/shapart) · [artem.shapovalov2003@gmail.com](mailto:artem.shapovalov2003@gmail.com)

## Summary

5th-year **Computer Security** student at BMSTU IU8 with almost four years of professional IT experience across systems administration, operational automation and enterprise document workflows.

Currently working with **OpenText/TESSA at Cherkizovo**: approval matrices and routes, user incidents, data validation and internal automation. Main languages are **Python, JavaScript and SQL**. I regularly work with Linux and understand backend services, REST APIs, relational databases and container deployment.

I also have practical SIEM/log-analysis experience with **MaxPatrol SIEM**, Windows event sources, source diagnostics, NetFlow and event parsing. I am looking for a junior position or internship in **SIEM/SOC, security automation or AppSec**.

### Selected proof points

- OpenText bulk operations: **hours of manual UI work → ~10 minutes** for typical covered scenarios.
- Built and introduced an internal OpenText operator toolkit used in day-to-day work by **two specialists**.
- **Alfa CTF 2026 — 45th place**.
- 3+ years of Windows / Microsoft 365 / workplace systems administration before moving into enterprise automation.

## Experience

### Cherkizovo Group — Document Workflow Automation Specialist
**February 2026 — present**

Support **OpenText/TESSA** and document approval processes.

- Configure approval matrices and routes: approvers, signers, stage conditions, legal entities, categories, document types and limits.
- Investigate user requests, routing errors and non-standard document cases.
- Compare document cards and approval sheets, prepare reports and validate data.
- Write service scripts and exports in **JavaScript, Python and SQL**.
- Developed and introduced **OpenText Toolkit / Matrix Cleaner**, a Tampermonkey operator tool for recurring and bulk matrix changes.
- The toolkit generates an explicit plan, shows affected rows and applies only confirmed operations instead of blindly mutating the matrix.
- Typical covered bulk changes that previously took hours of repetitive UI work can now be completed in about **10 minutes**.
- Also develop **TESSA Matrix Studio**, an XLSX round-trip workflow for reviewing and safely applying matrix changes.

### NAOS Vostok — Systems Administrator
**November 2022 — February 2026**

- Issued and configured computers, peripherals and accounts.
- Worked with **Windows, Microsoft 365, Intune, device policies, access management and basic inventory**.
- Performed day-to-day Windows Server tasks, service maintenance, remote access and workplace integrations.
- Supported Bitrix and 1C content/operational workflows and coordinated with colleagues and contractors.
- Published `naos.ru` pages from prepared layouts: promotions, magazine articles and banners.
- Automated repetitive tasks with Tampermonkey and Windows scripts, saving roughly an hour of manual work per day in covered workflows.
- Built reporting processes with **Power Automate, Excel and Power BI**.
- Developed an **SLA tracker**: Outlook/Graph data → SQLite → Excel → automated deadline reminders and SLA visibility.

## Selected Projects

### [OpenText Toolkit / Matrix Cleaner](https://github.com/ShapArt/Matrtix-Cleaner)
Tampermonkey-based operator layer for OpenText approval matrices and support workflows. Request parsing, scoped preview plans, ambiguity handling, guarded apply, reconciliation and regression checks.

**Stack:** JavaScript, Tampermonkey, Playwright, browser/DOM automation.

### [TESSA Matrix Studio](https://github.com/ShapArt/tessa-matrix-studio)
Excel round-trip editor for TESSA matrices: export, edit, exact diff, review and controlled apply with identity/live-state checks.

**Stack:** JavaScript, XLSX workflows, CI/release automation.

### [EyeGate-L](https://github.com/ShapArt/eyegate-l-luckfox-scud)
Edge computer-vision access-control prototype for LuckFox-class hardware.

**Stack:** Python, OpenCV, local inference, GPIO-oriented integration.

### [SH4PART VPN](https://github.com/ShapArt/vpn-bot-stars-hiddify)
Telegram-first subscription backend connecting payment/user state with provisioning and profile delivery.

**Stack:** Python, FastAPI, SQLite, Hiddify/Xray, nginx, systemd.

### [SLA / Outlook Toolkit](https://github.com/ShapArt/outlook-exporter)
Outlook/Graph extraction and operational reporting automation.

**Stack:** Python, pywin32, Microsoft Graph, SQLite, pandas, openpyxl.

## Information Security Practice

- **MaxPatrol SIEM:** event delivery, source diagnostics, parsing and event investigation.
- **Windows telemetry:** Windows Event Logs, authentication/RDP events, Sysmon concepts.
- **Network/log analysis:** NetFlow, syslog and traffic-analysis exercises.
- **Linux:** CLI, permissions, services, networking and logs.
- **AppSec:** authentication/authorization, secrets, safe defaults, OWASP-oriented thinking and failure modes.
- **Security automation:** dry-run/preview, explicit scope, bounded mutation, auditability and post-action verification.
- **CTF:** web, crypto, reverse and general security tasks.

## Skills

**Programming:** Python, JavaScript, SQL, C++, Shell, HTML/CSS  
**Backend:** FastAPI, REST APIs, PostgreSQL, SQLite  
**Infrastructure:** Linux, Docker, nginx, systemd, Git, Windows, Microsoft 365, Intune  
**Security:** MaxPatrol SIEM, Windows Event Logs, NetFlow, log parsing, AAA, RDP, iptables, OSINT  
**Automation:** Tampermonkey, Playwright, pywin32, Power Automate, pandas, openpyxl  
**Computer Vision:** OpenCV

## Education

### BMSTU — IU8
**10.05.01 Computer Security · Specialist degree · 5th year**

### BMSTU Digital Department
**Web Developer · 2024**

### VK Education
**Application Security / AppSec · 2025**

## Certificates & Achievements

### 2026
- [DevOps простым языком — Stepik](https://stepik.org/cert/3328074)
- [Доверенный искусственный интеллект — Stepik](https://stepik.org/cert/3328089)
- [Специалист по противодействию кибератакам — Stepik](https://stepik.org/cert/3328110)
- **Alfa CTF 2026 — 45th place** ([standings](https://clist.by/standings/alfa-ctf-2026-66930397/))

### 2025
- [Введение в SQL — Stepik](https://stepik.org/cert/2937373)
- [Введение в информационную безопасность аппаратных решений — Stepik](https://stepik.org/cert/2945060)
- [Теория вероятностей — Stepik](https://stepik.org/cert/2945135)
- **VK Education — Application Security / AppSec**

### Earlier
- **Skolkovo / Arctic Probe 2020** — engineering-project winner, Arctic buoy prototype.

→ [Full certificates and achievements](CERTIFICATES.md)

---

## RU — кратко

Учусь на 5 курсе ИУ8 МГТУ им. Н. Э. Баумана по специальности «Компьютерная безопасность». С февраля 2026 работаю с OpenText/TESSA в Черкизово: настраиваю маршруты и матрицы согласования, разбираю сложные заявки и пишу внутренние инструменты на Python, JavaScript и SQL.

Разработал OpenText Toolkit / Matrix Cleaner: для типовых массовых изменений инструмент строит план, показывает затрагиваемые строки и применяет только подтверждённые операции. В покрытых сценариях работа сократилась с нескольких часов ручного редактирования примерно до 10 минут.

До Черкизово больше трёх лет работал системным администратором: Windows, Microsoft 365, Intune, серверные задачи, Outlook/Graph, Power Automate, Excel/Power BI и автоматизация SLA.

Есть практический опыт с MaxPatrol SIEM, журналами Windows, NetFlow и диагностикой источников. Ищу junior-позицию или стажировку в SIEM/SOC, security automation или AppSec.
