# Artyom Shapovalov — Engineering Portfolio

**Security Automation · SIEM/SOC · Backend · Enterprise Tooling**

This document is the deeper version of my GitHub profile: less badge wall, more **problem → engineering decision → result**.

## Snapshot

- **BMSTU IU8** — 10.05.01 Computer Security, 5th year
- **Cherkizovo Group** — document workflow automation, February 2026 → present
- **Previous:** 3+ years systems administration / support / automation
- **Main languages:** Python, JavaScript, SQL
- **Security focus:** SIEM/SOC, AppSec, logs/event pipelines, safe automation
- **CTF:** Alfa CTF 2026 — **45th place**

---

# Case 01 — OpenText Toolkit / Matrix Cleaner

**Repository:** [ShapArt/Matrtix-Cleaner](https://github.com/ShapArt/Matrtix-Cleaner)

## Context

OpenText approval matrices encode real routing policy: who approves, who signs, for which legal entity, category, document type, site, amount range and other conditions.

The painful part is not the number of clicks. The painful part is that many rows look similar while carrying different meaning. A “fast” bulk edit without a review layer can create a routing problem that only appears later on a real document.

## Problem

Typical requests included things like:

- replace a signer across a defined scope;
- add a legal entity without changing adjacent rules;
- move a site or function between people;
- change a limit while preserving the rest of a row;
- understand why a route behaved differently from what the requester expected.

Historically, large changes were performed row by row through the interface and could take **hours of repetitive work**.

## What I built

A Tampermonkey-based operator toolkit that sits on top of OpenText and turns a dangerous free-form operation into a controlled workflow.

```text
request / ticket
      ↓
parse intent and scope
      ↓
inspect the actual matrix
      ↓
build an explicit change plan
      ↓
show affected rows + ambiguity
      ↓
operator review
      ↓
re-check target state
      ↓
guarded apply
      ↓
verify / log
```

The toolkit supports matrix inspection, request parsing, preview plans, signer/role operations, row splitting, scoped replacement, reconciliation and HelpDesk-oriented diagnostics.

## Safety decisions

- **Preview first:** no bulk write without a visible plan.
- **Ambiguity is a state:** unclear input becomes a question, not a guess.
- **Scope is explicit:** legal entity / site / category / role boundaries stay visible.
- **Fresh checks:** the write path validates target state before mutation.
- **Regression from reality:** real tickets and historical failure cases are turned into repeatable tests.

## Result

For typical covered bulk scenarios, work that previously took **hours** can now be prepared and completed in roughly **10 minutes**.

The tool is used in daily OpenText work by me and a senior specialist, while the recovered time goes into non-standard incidents, route diagnostics and process improvements.

## What this project demonstrates

`JavaScript` · `Tampermonkey` · `Playwright` · browser automation · parsing · domain modelling · safe mutation · operator UX · regression engineering

---

# Case 02 — TESSA Matrix Studio

**Repository:** [ShapArt/tessa-matrix-studio](https://github.com/ShapArt/tessa-matrix-studio)

## Problem

Editing large TESSA matrices directly in the UI is slow. Excel is excellent for structured bulk editing — but naive “export/edit/import” loses the most important thing: **identity and confidence that the live row is still the same row you reviewed**.

## What I built

An XLSX round-trip workflow:

```text
TESSA
  ↓
structured export
  ↓
Excel bulk edit
  ↓
exact diff / plan
  ↓
operator review
  ↓
fresh live-state validation
  ↓
controlled apply
```

The export preserves hidden identity/baseline information. The preview converts spreadsheet differences into concrete operations. The apply path validates the current matrix instead of treating the XLSX as absolute truth.

## Why it matters

This is the same engineering principle as Matrix Cleaner expressed through a different interface: **make the easy editing surface convenient without making the dangerous action blind**.

## Product layer

The repository is maintained like a small internal product: releases, CI, installable artifact, documentation and production-oriented checks rather than a single one-off script.

## What this project demonstrates

`JavaScript` · XLSX workflows · identity preservation · diff planning · controlled writes · CI/release engineering · productization

---

# Case 03 — SLA / Outlook Operations Toolkit

**Repository:** [ShapArt/outlook-exporter](https://github.com/ShapArt/outlook-exporter)

## Context

At NAOS, many operational tasks lived in Outlook, Excel and people’s heads: statuses, deadlines, repeated exports and reminders.

## What I built

- Outlook / Microsoft Graph data extraction;
- SQLite storage for structured operational state;
- Excel reporting and exports;
- automated deadline reminders;
- supporting Power Automate / Power BI flows;
- browser/Windows helpers for recurring support operations.

## Result

The tooling removed repeated copy-paste work, saved roughly **an hour per day** in covered tasks and gave clearer visibility into SLA deadlines and overdue items.

## What this project demonstrates

`Python` · `pywin32` · `Microsoft Graph` · `SQLite` · `pandas` · `openpyxl` · operations automation

---

# Case 04 — EyeGate-L

**Repository:** [ShapArt/eyegate-l-luckfox-scud](https://github.com/ShapArt/eyegate-l-luckfox-scud)

## Goal

Prototype an edge computer-vision access-control system on LuckFox-class constrained hardware.

## Engineering focus

- local processing rather than a cloud dependency in the decision path;
- CV pipeline under hardware constraints;
- separation between recognition/decision and the physical lock action;
- GPIO-oriented integration;
- thinking through what should happen when a dependency fails.

## What this project demonstrates

`Python` · `OpenCV` · edge AI · embedded-style constraints · security boundaries

---

# Case 05 — SH4PART VPN

**Repository:** [ShapArt/vpn-bot-stars-hiddify](https://github.com/ShapArt/vpn-bot-stars-hiddify)

## Goal

Build more than a Telegram bot UI: create the backend path from user/payment state to access provisioning and subscription delivery.

```text
Telegram user
    ↓
payment / entitlement state
    ↓
backend
    ↓
provisioning
    ↓
signed/profile delivery
    ↓
reminders / lifecycle
```

## Stack

`Python` · `FastAPI` · `SQLite` · `Telegram Bot API` · `Hiddify/Xray` · `nginx` · `systemd`

## What this project demonstrates

Backend state, integrations, token/secret boundaries and Linux deployment outside a local development environment.

---

# Professional Experience

## Cherkizovo Group — Document Workflow Automation
**February 2026 — present**

I support OpenText/TESSA document approval processes and investigate why routes behave the way they do.

Day-to-day work includes:

- configuring matrices and routes;
- approvers, signers and approval stages;
- legal entities, categories, document types and limits;
- investigating routing errors and non-standard user cases;
- comparing document cards and approval sheets;
- SQL/data checks and operational reports;
- JavaScript/Python tooling around repetitive work;
- turning recurring support patterns into diagnostics or operator automation.

The work made **OpenText Toolkit / Matrix Cleaner** and **TESSA Matrix Studio** possible: both came from real recurring operations rather than invented portfolio requirements.

## NAOS Vostok — Systems Administrator
**November 2022 — February 2026**

Worked with Windows workplaces, Microsoft 365, Intune, device policies, user access, Windows Server tasks, services, remote access and workplace integrations.

Also supported Bitrix/1C operational workflows, published prepared content to `naos.ru`, interacted with contractors and automated Outlook/Excel/support operations.

---

# Security Track

## SIEM / event analysis

Practical experience and exercises around:

- MaxPatrol SIEM;
- event delivery and source diagnostics;
- Windows Event Logs;
- authentication/RDP events and Sysmon concepts;
- NetFlow and traffic/log analysis;
- parsing and correlation thinking;
- Linux logs and service-side troubleshooting.

## AppSec / safe engineering

My automation work has made several security principles very practical:

- permissions and authentication/authorization boundaries;
- secrets/token handling;
- input validation;
- safe defaults;
- explicit scope;
- dry-run / preview before mutation;
- auditability;
- predictable failure behaviour;
- refusing to infer destructive intent when evidence is weak.

---

# Education & Evidence

## BMSTU IU8

**10.05.01 Computer Security · specialist degree · 5th year**

## Additional education

- **VK Education — Application Security / AppSec**, 2025
- **BMSTU Digital Department — Web Developer**, 2024

## Certificates

### 2026
- [DevOps простым языком](https://stepik.org/cert/3328074)
- [Доверенный искусственный интеллект](https://stepik.org/cert/3328089)
- [Специалист по противодействию кибератакам](https://stepik.org/cert/3328110)

### 2025
- [Введение в SQL](https://stepik.org/cert/2937373)
- [Введение в информационную безопасность аппаратных решений](https://stepik.org/cert/2945060)
- [Теория вероятностей](https://stepik.org/cert/2945135)

## Competitions / engineering achievements

- **Alfa CTF 2026 — 45th place** ([standings](https://clist.by/standings/alfa-ctf-2026-66930397/))
- **Skolkovo / Arctic Probe 2020 — winner**, Arctic buoy engineering prototype
- **ICCETT / Quantoriada — finalist**, Python-based psycho-emotional training project

→ [Certificates & achievements index](CERTIFICATES.md)

---

# Technical Map

| Area | Tools / technologies |
|---|---|
| Programming | Python, JavaScript, SQL, C++, Shell |
| Backend | FastAPI, REST APIs, PostgreSQL, SQLite |
| Automation | Tampermonkey, Playwright, pywin32, Power Automate, pandas, openpyxl |
| Systems | Linux, Windows, Microsoft 365, Intune, Git, Docker, nginx, systemd |
| Security | MaxPatrol SIEM, Windows Event Logs, NetFlow, log parsing, AAA, RDP, iptables, OSINT |
| CV | OpenCV, edge/local processing |
| Enterprise domain | OpenText, TESSA, approval matrices and routing workflows |

---

# Engineering Principle

The common pattern across the best projects is not a framework or language.

It is this:

> **Make the operator faster without making the system less understandable.**

I prefer reviewable automation over magic buttons, explicit uncertainty over confident guessing and production verification over “it worked on my machine”.

---

[← GitHub profile](README.md) · [Resume](RESUME.md) · [Certificates](CERTIFICATES.md) · [Cases repository](https://github.com/ShapArt/cases-and-achievements)
