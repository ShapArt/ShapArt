# Artyom Shapovalov — Portfolio

Backend, automation, operator tooling, and security-minded engineering.

I build practical software for workflows that are usually repetitive, fragile, or hidden inside manual operations: document workflow automation, browser-side operator tools, Telegram bots, Outlook/Excel exports, self-hosted services, and infrastructure-adjacent utilities.

## Current profile

- **Name:** Artyom Shapovalov
- **GitHub:** [ShapArt](https://github.com/ShapArt)
- **Education:** BMSTU, IU8, Computer Security
- **Current work:** document workflow automation at Cherkizovo, since February 2026
- **Main direction:** applied backend and automation tools with security and reliability awareness

## Case-study portfolio

Detailed case studies live in [`cases-and-achievements`](https://github.com/ShapArt/cases-and-achievements):

| Case | Area | What it shows |
|---|---|---|
| [EyeGate-L / Luckfox SCUD](https://github.com/ShapArt/cases-and-achievements/blob/main/cases/01-eyegate-l-luckfox-scud.md) | Computer vision / edge / access control | Technical depth, constrained hardware thinking, security-sensitive system boundaries |
| [SLA / Outlook Tracker](https://github.com/ShapArt/cases-and-achievements/blob/main/cases/02-sla-outlook-tracker.md) | Office automation / reporting | Business-facing automation, Outlook/Excel data workflows, status visibility |
| [Matrtix-Cleaner](https://github.com/ShapArt/cases-and-achievements/blob/main/cases/03-matrtix-cleaner.md) | Browser automation / OpenText | Guarded enterprise automation with preview, audit, ambiguity handling, and operator control |
| [OpenText Operator Bridge](https://github.com/ShapArt/cases-and-achievements/blob/main/cases/04-opentext-operator-bridge.md) | Backend / workflow tooling | Intake, triage, bounded action planning, and integration-heavy backend design |
| [Sh4pArt VPN](https://github.com/ShapArt/cases-and-achievements/blob/main/cases/05-sh4part-vpn.md) | Backend / Telegram bot / infra | Full service lifecycle from payment to provisioning, profile delivery, and reminders |

## What I focus on

### Document workflow automation

I work with operational processes where manual actions, approvals, documents, matrices, and status tracking create hidden complexity.

My focus is to turn that complexity into tools that are easier to inspect, repeat, and maintain:

- browser-side helpers for existing enterprise systems;
- scripts for reducing repetitive document workflow operations;
- exports and reporting flows around Outlook / Excel-style work;
- safer operator tooling with preview, dry-run, and review steps;
- small backend services for intake, triage, and workflow control.

### Backend and integration-heavy tools

I like projects where backend code connects real systems rather than existing as an isolated demo.

Typical project shapes:

- Telegram bot backends;
- webhook-driven services;
- provisioning flows;
- SQLite / SQLAlchemy-backed state;
- API integrations;
- environment-driven deployment;
- Linux service setup.

### Security-minded engineering

My education is in computer security, so I try to look at automation through risk, boundaries, and failure modes.

That means paying attention to:

- where secrets live;
- what should be automated and what should stay operator-controlled;
- how destructive actions are previewed;
- what happens when an external dependency breaks;
- how to keep public repositories free from sensitive internal details.

## Selected project summaries

### EyeGate-L / Luckfox SCUD prototype

**Repository:** [`eyegate-l-luckfox-scud`](https://github.com/ShapArt/eyegate-l-luckfox-scud)

Edge-focused computer vision and access-control prototype aimed at constrained hardware.

**Why it matters:** the project shows interest in deployment constraints, local inference, hardware-adjacent thinking, and security-oriented system design.

### SLA / Outlook Tracker

**Repository:** [`outlook-exporter`](https://github.com/ShapArt/outlook-exporter)

Windows-first Outlook export and spreadsheet processing workspace for turning mailbox-derived information into structured operational data.

**Why it matters:** a lot of business process truth lives in email. Exporting, transforming, and reviewing that information without manual copy-paste is a practical automation problem.

### Matrtix-Cleaner

**Repository:** [`Matrtix-Cleaner`](https://github.com/ShapArt/Matrtix-Cleaner)

Tampermonkey-based operator tool for previewing, auditing, and applying guarded bulk changes in OpenText approval matrices.

**Why it matters:** approval matrices are risky to edit manually because small mistakes can affect routing, signers, legal entities, and document rules. The project focuses on controlled browser-side automation with preview and operator review instead of blind mass mutation.

### OpenText Operator Bridge

**Repository:** [`opentext-operator-bridge`](https://github.com/ShapArt/opentext-operator-bridge)

Private backend/operator workflow layer for intake, triage, and bounded action planning around OpenText-related support scenarios.

**Why it matters:** real operational requests often arrive through emails, files, portals, and incomplete context. This project is about turning fragmented inputs into a reviewable workflow.

### vpn-bot-stars-hiddify

**Repository:** [`vpn-bot-stars-hiddify`](https://github.com/ShapArt/vpn-bot-stars-hiddify)

Telegram-first VPN subscription backend built around payment, provisioning, profile delivery, and reminder logic.

**Why it matters:** the interesting part is not only the bot interface; it is the full delivery path between payment, user state, provisioning, onboarding links, and support reduction.

## Skills map

### Core

- Python
- JavaScript
- SQL
- Linux CLI
- Git
- Docker / Compose basics

### Backend and automation

- FastAPI
- Telegram Bot API
- SQLite
- SQLAlchemy
- Playwright
- pywin32
- pandas
- openpyxl
- Tampermonkey userscripts

### Security and systems

- Computer security foundations
- OWASP Top 10 awareness
- Recon / OSINT basics
- Linux services and nginx basics
- TLS / Let's Encrypt basics
- iptables basics
- log parsing and triage foundations

### Academic foundation

- Computer networks
- Databases
- Embedded systems
- Electronics simulation
- Digital signal processing
- Applied ML / CV / NLP coursework

## How to read this GitHub

This profile is intentionally structured into several layers:

1. **Selected projects** — the best public repositories for a quick technical review.
2. **Case studies** — deeper explanation of problem, solution, stack, result, and lessons learned.
3. **Supporting tools** — small utilities and bots that show practical automation instincts.
4. **Academic repositories** — coursework archives from BMSTU showing technical foundation.
5. **Private/internal work** — summarized carefully without exposing sensitive systems.

Not every repository is meant to look like a startup product. Some are utilities, some are experiments, and some are academic archives. The common thread is practical engineering: reduce routine, make workflows clearer, and build tools around real constraints.

## RU

Я Шаповалов Артём, студент 4 курса ИУ8 МГТУ им. Н. Э. Баумана по направлению компьютерной безопасности.

С февраля 2026 работаю в Черкизово в направлении автоматизации документооборота. Основной интерес — backend, automation, operator tooling, безопасность процессов и практические инструменты, которые уменьшают ручную рутину.

Подробные кейсы вынесены в отдельный репозиторий [`cases-and-achievements`](https://github.com/ShapArt/cases-and-achievements), чтобы работодатель мог быстро увидеть не только стек, но и инженерное мышление: проблема, решение, результат и выводы.
