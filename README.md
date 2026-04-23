<h1 align="center">ShapArt</h1>
<p align="center"><strong>Backend, automation, and operator tooling</strong></p>

![Social Preview](https://raw.githubusercontent.com/ShapArt/ShapArt/main/.github/social-preview.png)

I build practical software for workflows that are usually painful, repetitive, or easy to break: Telegram bots, internal operator tools, browser automation, data export utilities, and systems that sit between infrastructure and day-to-day operations.

A meaningful part of my applied work lives in private repositories because it is tied to internal environments or non-public assets. The public repositories below show the kind of engineering problems I like to work on: delivery flows, operator UX, guarded automation, and tools that reduce manual effort instead of adding ceremony.

## Focus areas

- **Backend systems** for API-driven flows, integrations, and operational logic
- **Automation & workflow tooling** for repetitive business processes and internal support scenarios
- **Telegram bots & operator UX** where onboarding, delivery, and support all have to work together
- **Infrastructure-minded delivery** with attention to configuration, failure modes, and maintainability
- **Practical internal tools** that make messy manual work more repeatable and safer

## Selected public projects

| Project | What it does | Stack | Why it is interesting |
|---|---|---|---|
| [`vpn-bot-stars-hiddify`](https://github.com/ShapArt/vpn-bot-stars-hiddify) | Telegram-based VPN subscription backend with webhook handling, plan management, Hiddify provisioning, deeplink/QR delivery, and reminder logic | Python, FastAPI, Telegram Bot API, SQLite, APScheduler | Ties billing, provisioning, and client onboarding into one operator-facing flow |
| [`Matrtix-Cleaner`](https://github.com/ShapArt/Matrtix-Cleaner) | Tampermonkey operator tool for previewing and applying guarded bulk changes in OpenText approval matrices | JavaScript, Tampermonkey, jQuery, OpenText DOM integration | Useful example of browser-side automation with safety rails, dry-run logic, and domain-specific operations |
| [`outlook-exporter`](https://github.com/ShapArt/outlook-exporter) | Windows-first Outlook export and spreadsheet processing workspace for turning mailbox data into structured operational artifacts | Python, pywin32, pandas, openpyxl, PySide6 | Sits at the intersection of office automation, desktop tooling, and data handling |
| [`eyegate-l-luckfox-scud`](https://github.com/ShapArt/eyegate-l-luckfox-scud) | Edge-focused computer vision prototype aimed at constrained hardware | Python / CV-oriented tooling on embedded-style hardware | Shows interest in deployment constraints, not just model code in isolation |
| [`8-sem-network-labs`](https://github.com/ShapArt/8-sem-network-labs) | Structured Cisco Packet Tracer lab archive for computer networks coursework | Cisco Packet Tracer | Academic repository, but useful as evidence of systematic networking work rather than random one-off files |

## Engineering approach

I like systems that turn fragile manual steps into repeatable workflows.

That usually means being careful about boundaries: what should be automated, what should stay operator-controlled, what needs a preview or dry-run first, and what has to fail closed instead of failing creatively.

I care more about clear behavior and usable interfaces than about over-abstracting a codebase for its own sake.

## Stack snapshot

**Languages & runtime**

Python, JavaScript, SQL, shell tooling

**Typical building blocks**

FastAPI, Telegram Bot API, SQLite, pandas, openpyxl, PySide6, Playwright, browser userscripts, environment-driven configuration

**Common problem shapes**

- intake and triage flows
- guarded automation
- export / transformation pipelines
- operator-facing utilities
- integration-heavy scripts and services

## Notes on repository scope

Not every repository here is meant to look like a startup product. Some are intentionally small utilities, course archives, or experiments. I prefer to document them honestly rather than pretending every repo is a platform.

## Contact / navigation

- GitHub: [@ShapArt](https://github.com/ShapArt)
- Main public repositories: see the table above
- Some applied workflow tooling and internal automation remain private by design

## RU

Делаю прикладные backend- и automation-инструменты: боты, операторские утилиты, экспортёры, браузерную автоматизацию и сервисы на стыке инфраструктуры и повседневных процессов.

Для меня важны не громкие слова, а понятная инженерная ценность: меньше рутины, меньше хрупких ручных действий, больше предсказуемости в работе системы.
