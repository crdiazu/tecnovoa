# AGENTS.md — Web_y_Landing

## Objective
Create and maintain TECNOVOA's marketing website assets (static HTML/CSS/JS + WordPress embeds) without build tools, keeping the folder compact and agent-friendly.

## Important Details
- This is a **static site** (no package.json, no build step). Source lives in `website/`; WordPress embeds are `*-wp-embed.html` files.
- Design tokens: `--bg-deep`, `--bg-surface`, `--accent-blue`, `--accent-cyan`, `--accent-gradient`, `--border-hairline`, `--text-primary/secondary`, `--radius-md/lg`, `--shadow-soft`.
- Business units: Telecom, Datacenter/Cloud, AV, Cybersecurity, Backup, EndUser, Energy, Virtualization.
- `md_to_wp.py` converts a Markdown file (with SEO frontmatter) into separate `.html`, `.css`, `.js` using the TECNOVOA WP component template.
- Dashboard: `dashboard-renovacion-digital.md` tracks a 4-week renovation; currently Week 3 (launch/QA).
- Root `AGENTS.md` conventions apply (TECNOVOA CRM, daily notes, folder naming).
- Avoid Copilot Plus skills; use native tools.

## Work State
### Completed
- Created this AGENTS.md after inspecting the folder structure and root guidance.

### Active
- (none)

### Blocked
- (none)

## Next Move
1. Review `website/index.html` and the WP embed files to confirm the current canonical content before editing.
2. If changes are needed, update source files and regenerate embeds via `md_to_wp.py` only when a Markdown source exists.

## Relevant Files
- `website/` — static site source (HTML/CSS/JS/images).
- `website/index.html` — full site entry point.
- `*-wp-embed.html` — WordPress block embeds (no navbar/footer/breadcrumb).
- `md_to_wp.py` — Markdown-to-WordPress converter.
- `dashboard-renovacion-digital.md` — 4-week renovation timeline.
- `INICIO - TECNOVOA.md` — main content source.
