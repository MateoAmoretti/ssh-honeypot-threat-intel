# SSH Honeypot and Threat Intelligence Dashboard

**Status:** In progress. Stage 1 of 5 (cloud server hardening), started 14 Oct 2026. Daily progress is in [DEVLOG.md](DEVLOG.md).

## What this is

A Cowrie SSH honeypot on a hardened cloud server that records real SSH attacks for 30 days. A Python pipeline enriches the data with geolocation, AbuseIPDB reputation scores, VirusTotal hash lookups and MITRE ATT&CK technique tags, and a Streamlit dashboard shows the results. A short report sums up what the attacks show and how to defend against them.

## Why I built it

To practise the core of SOC analyst work on real attacker data: collect logs, add context, investigate, map behaviour to MITRE ATT&CK and report the findings.

## Progress

- [ ] Stage 1: cloud server hardened (key-only SSH on a private port, two firewalls)
- [ ] Stage 2: Cowrie live on port 22, collecting for 30 days
- [ ] Stage 3: Python pipeline (SQLite, geolocation, AbuseIPDB, VirusTotal, ATT&CK)
- [ ] Stage 4: Streamlit dashboard
- [ ] Stage 5: "30 days of attacks" report

## How it works

Architecture diagram coming in Stage 5.

## How to run it

Instructions coming with the pipeline in Stage 3.

## Safety and ethics

- The honeypot runs only on an isolated cloud server, never on a home network or personal machine.
- Files that attackers download are never opened or run; only their hashes are kept.
- No attacker is ever probed, scanned or attacked back.
- No secrets are committed: API keys live in a local `.env` file that git ignores.
- Attacker IP addresses are masked in everything published.
- I checked the cloud provider's acceptable use policy before deploying: see [docs/provider-policy.md](docs/provider-policy.md).

## What I learned

Filled in as I go; the day-by-day version is in [DEVLOG.md](DEVLOG.md).
