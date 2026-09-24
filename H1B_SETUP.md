# Read-only H-1B monitor setup

This monitor reads the public qmq.app availability grid and sends an ntfy push. It never logs into usvisascheduling/CGI and cannot book or reschedule anything.

## Repository Variables

Set these at **Settings → Secrets and variables → Actions → Variables**:

| Name | Value |
|---|---|
| `VISA_CITIES` | `广州,武汉,上海` |
| `VISA_TYPE` | `H-1B` |
| `VISA_DESC` | *(empty)* |
| `VISA_START` | `2026-11-01` |
| `VISA_CUTOFF` | `2026-12-15` |
| `VISA_INCLUDE_EMERGENCY` | `0` |

## Required Secret

Create `VISA_NTFY_TOPIC` at **Settings → Secrets and variables → Actions → Secrets**. Its value must be a private, unguessable ntfy topic you subscribe to in the ntfy app. Do not put the topic in a Variable, code, or a commit.

## Manual test

Open **Actions → visaMonitor → Run workflow**. Select `status` for a single, non-urgent snapshot of the three cities; then select `monitor` to exercise the normal alert-only path. A log line beginning `STATUS: OK` means the public query succeeded. `SCRAPE_FAILED (cloudflare)` means GitHub’s shared IP was blocked; use the repo’s optional local watcher instead.
