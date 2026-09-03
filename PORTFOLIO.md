# Artyom Shapovalov — Portfolio

**Security automation · SIEM/SOC · backend · internal tools**

I build tools around real operational work: approval routes, large matrices, Outlook/Excel workflows, event pipelines and backend services. The common theme is simple — automate the repetitive part without hiding scope, state or failure modes.

**BMSTU IU8, 5th year · Cherkizovo Group since February 2026 · Python / JavaScript / SQL · Alfa CTF 2026 #45**

[GitHub profile](README.md) · [Resume](RESUME.md) · [Certificates](CERTIFICATES.md) · [HH / RU profile](HH_RU_PROFILE.txt)

---

## OpenText Toolkit / Matrix Cleaner

[Repository](https://github.com/ShapArt/Matrtix-Cleaner)

OpenText approval matrices contain routing policy: approvers, signers, legal entities, categories, document types, sites, limits and other conditions. Large changes used to mean opening rows one by one and repeating the same edit for hours.

I started Matrix Cleaner as a Tampermonkey helper and kept extending it around real support requests. It now parses request scope, inspects the matrix, builds a concrete preview, shows affected rows, flags ambiguity and applies only reviewed operations.

```text
request → scope → inspect → preview → review → apply → verify
```

The important part is not the click automation. Similar rows can mean different things, so the tool keeps scope visible and refuses to guess when a request is ambiguous.

**Result:** typical covered bulk changes went from hours of repetitive UI work to roughly **10 minutes**. The tool is used in day-to-day OpenText work by me and a senior specialist.

`JavaScript · Tampermonkey · Playwright · browser automation · parsing · regression tests`

---

## TESSA Matrix Studio

[Repository](https://github.com/ShapArt/tessa-matrix-studio)

Editing a large matrix is much easier in Excel than through dozens of individual UI forms. The problem is that a naive export/import flow loses confidence that the row being written is still the row that was reviewed.

TESSA Matrix Studio uses an XLSX round trip:

```text
TESSA → export → Excel edits → exact diff → review → live-state check → apply
```

The export carries identity and baseline data. The preview turns spreadsheet changes into explicit operations. Before writing, the tool checks the current matrix again instead of treating the XLSX as absolute truth.

The repository is maintained with releases, CI, installable artifacts and operator documentation rather than as a one-off script.

`JavaScript · XLSX · diff planning · CI / releases · controlled writes`

---

## SLA / Outlook Toolkit

[Repository](https://github.com/ShapArt/outlook-exporter)

At NAOS, part of the support workflow lived across Outlook, Excel and manual reminders. Requests were easy to lose, repeated exports took time and SLA status depended too much on people remembering to check it.

I built a small operational pipeline around Outlook / Microsoft Graph, SQLite and Excel: structured extraction, saved state, reporting, deadline reminders and supporting Power Automate / Power BI flows.

```text
Outlook / Graph → SQLite → Excel / reports → deadline reminders
```

**Result:** roughly an hour of repetitive work per day was removed in covered workflows, with clearer visibility into overdue requests.

`Python · pywin32 · Microsoft Graph · SQLite · pandas · openpyxl`

---

## EyeGate-L

[Repository](https://github.com/ShapArt/eyegate-l-luckfox-scud)

Edge computer-vision access-control prototype for LuckFox-class hardware. Recognition stays local, the CV path is designed around constrained hardware, and the recognition/decision logic is separated from the physical lock action.

The project was useful for thinking about security at the boundary between software and a real physical action: what happens when inference fails, when a dependency disappears, or when a decision should not automatically become an unlock command.

`Python · OpenCV · edge / local-first · GPIO-oriented integration`

---

## SH4PART VPN

[Repository](https://github.com/ShapArt/vpn-bot-stars-hiddify)

Telegram-first backend for the subscription lifecycle rather than just a bot UI: user/payment state, entitlement, provisioning, profile delivery, reminders and Linux deployment.

```text
Telegram → payment / entitlement → backend → provisioning → delivery
```

`Python · FastAPI · SQLite · Telegram Bot API · Hiddify/Xray · nginx · systemd`

---

## Work

### Cherkizovo Group — document workflow automation
**February 2026 — present**

I support OpenText/TESSA approval processes: matrices, routes, approvers, signers, legal entities, categories, document types, sites and limits. A large part of the job is diagnosing why a route behaved the way it did and checking data across cards, approval sheets and matrix conditions.

I also write JavaScript, Python and SQL tooling around recurring work. Matrix Cleaner and TESSA Matrix Studio both came directly from these tasks.

### NAOS Vostok — systems administrator
**November 2022 — February 2026**

Windows workplaces, Microsoft 365, Intune, device policies, access, Windows Server tasks, services, remote access and support. I also automated Outlook/Excel/browser routines and built reporting/SLA workflows with Power Automate and Power BI.

---

## Security track

My current security practice is mostly around systems and telemetry rather than isolated lab-only exercises.

- MaxPatrol SIEM: event delivery, source diagnostics, parsing and investigation.
- Windows: Event Logs, authentication/RDP events, Sysmon concepts, WEF/WEC-style collection work.
- Linux: logs, auditd / syslog-style pipelines, service-side troubleshooting.
- Network/event data: NetFlow, log parsing and correlation thinking.
- AppSec habits in tooling: authentication/authorization boundaries, secrets, explicit scope, preview/dry-run, auditability and predictable failure behaviour.

---

## Education & evidence

**BMSTU IU8** — 10.05.01 Computer Security · specialist degree · 5th year  
**VK Education** — Application Security / AppSec · 2025  
**BMSTU Digital Department** — Web Developer · 2024  
**Alfa CTF 2026** — 45th place

Selected Stepik courses: DevOps, Trusted AI, Countering Cyberattacks, SQL, Hardware Security and Probability Theory.

[Full certificates & achievements](CERTIFICATES.md)

---

## Stack

**Python · JavaScript · SQL · FastAPI · PostgreSQL · SQLite · Linux · Windows · Docker · nginx · systemd · Git · Playwright · Tampermonkey · pandas · openpyxl · pywin32 · OpenCV · MaxPatrol SIEM · OpenText · TESSA**

---

## Contact

[GitHub](https://github.com/ShapArt) · [Telegram @shapart](https://t.me/shapart) · [artem.shapovalov2003@gmail.com](mailto:artem.shapovalov2003@gmail.com)
