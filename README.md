<h1 align="center">ShapArt</h1>
<p align="center"><strong>Backend, automation, and operator tooling</strong></p>

I build practical software for workflows that are usually painful, repetitive, or easy to break: Telegram bots, internal operator tools, browser automation, data export utilities, and systems that sit between infrastructure and day-to-day operations.

A meaningful part of my applied work lives in private repositories because it is tied to internal environments, coursework materials, or non-public assets. The public repositories below show the kind of engineering problems I like to work on: delivery flows, operator UX, guarded automation, and tools that reduce manual effort instead of adding ceremony.

## Focus areas

- **Backend systems** for API-driven flows, integrations, and operational logic
- **Automation & workflow tooling** for repetitive business processes and internal support scenarios
- **Telegram bots & operator UX** where onboarding, delivery, and support all have to work together
- **Browser-side operator tools** for improving workflows inside existing systems
- **Infrastructure-minded delivery** with attention to configuration, failure modes, and maintainability
- **Academic foundations** across networks, databases, embedded systems, electronics, and applied ML coursework

## Selected projects

| Project | What it does | Stack | Why it is interesting |
|---|---|---|---|
| [`vpn-bot-stars-hiddify`](https://github.com/ShapArt/vpn-bot-stars-hiddify) | Telegram-first VPN subscription backend with webhook handling, plan management, Hiddify provisioning, deeplink/QR delivery, and reminder logic | Python, FastAPI, Telegram Bot API, SQLite, APScheduler | Ties billing, provisioning, and client onboarding into one operator-facing flow |
| [`Matrtix-Cleaner`](https://github.com/ShapArt/Matrtix-Cleaner) | Tampermonkey operator tool for previewing and applying guarded bulk changes in OpenText approval matrices | JavaScript, Tampermonkey, jQuery, OpenText DOM integration | Browser-side automation with safety rails, dry-run logic, and domain-specific operations |
| [`opentext-operator-bridge`](https://github.com/ShapArt/opentext-operator-bridge) | Private guarded intake, triage, and operator workflow layer for OpenText-related support scenarios | Python, FastAPI, SQLAlchemy, Playwright, pywin32 | Shows workflow thinking around fragmented inputs, diagnostics, and bounded automation |
| [`outlook-exporter`](https://github.com/ShapArt/outlook-exporter) | Windows-first Outlook export and spreadsheet processing workspace for turning mailbox data into structured operational artifacts | Python, pywin32, pandas, openpyxl, PySide6 | Sits at the intersection of office automation, desktop tooling, and data handling |
| [`tampermonkey-ozon-tickets-export`](https://github.com/ShapArt/tampermonkey-ozon-tickets-export) | Browser helper for ticket export and operator-side review inside an existing workflow | JavaScript, Tampermonkey | Small but practical example of reducing manual browser work |
| [`eyegate-l-luckfox-scud`](https://github.com/ShapArt/eyegate-l-luckfox-scud) | Edge-focused computer vision prototype aimed at constrained hardware | Python / CV-oriented tooling | Shows deployment-aware thinking beyond notebook-only model experiments |

## Supporting work

| Area | Repositories | What they show |
|---|---|---|
| Telegram bots | `kino-bot`, `qotd-telegram-bot`, `tg-media-downloader-bot`, `bmstu-practice-2024-telegram-bot` | Small user-facing automation flows and bot UX practice |
| Media utilities | `compress-photos-cli`, `image-cover-cropper`, `media-compressor-web` | Focused tools for repeated image/media preparation tasks |
| Academic foundations | `8-sem-network-labs`, `ASVT`, `labs`, `kursovaia-coursework`, `db-music-store`, `dsp-labs`, `tsosi-course-projects` | Networks, embedded systems, electronics simulation, databases, DSP, and applied ML coursework |
| Portfolio/context | `cases-and-achievements`, `selfhost-cloud`, `private-messenger`, `Jornal` | Supporting notes, infrastructure experiments, and early-stage prototypes |

## Engineering approach

I like systems that turn fragile manual steps into repeatable workflows.

That usually means being careful about boundaries: what should be automated, what should stay operator-controlled, what needs a preview or dry-run first, and what has to fail closed instead of failing creatively.

I care more about clear behavior and usable interfaces than about over-abstracting a codebase for its own sake.

## Stack snapshot

**Languages & runtime**

Python, JavaScript, SQL, shell tooling

**Typical building blocks**

FastAPI, Telegram Bot API, SQLite, SQLAlchemy, pandas, openpyxl, PySide6, Playwright, browser userscripts, environment-driven configuration

**Common problem shapes**

- intake and triage flows
- guarded automation
- export and transformation pipelines
- operator-facing utilities
- browser-side workflow augmentation
- integration-heavy scripts and services

## Notes on repository scope

Not every repository here is meant to look like a startup product. Some are intentionally small utilities, course archives, or experiments. I prefer to document them honestly rather than pretending every repo is a platform.

The strongest portfolio direction is applied automation: small systems that connect real workflows, reduce manual effort, and keep risky operations inspectable.

## Contact / navigation

- GitHub: [@ShapArt](https://github.com/ShapArt)
- Start with the selected projects above
- Some applied workflow tooling and academic materials remain private by design

## RU

Делаю прикладные backend- и automation-инструменты: боты, операторские утилиты, экспортёры, браузерную автоматизацию и сервисы на стыке инфраструктуры и повседневных процессов.

Для меня важны не громкие слова, а понятная инженерная ценность: меньше рутины, меньше хрупких ручных действий, больше предсказуемости в работе системы.
