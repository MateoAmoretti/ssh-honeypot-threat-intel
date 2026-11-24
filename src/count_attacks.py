"""
count_attacks.py
Reads Cowrie's JSON log files and prints summary numbers for the honeypot.

Usage (run from the project folder):
    python src/count_attacks.py <folder containing the cowrie.json files>
"""

import json                      # turns each line of text into a Python dictionary
import sys                       # lets us read the folder path typed after the script name
from collections import Counter  # a dictionary that counts things for us
from pathlib import Path         # handles file paths on both Windows and Linux

# The official 30-day window: Day 1 (16 Oct) to Day 30 (14 Nov), inclusive.
# Cowrie timestamps are UTC text like "2026-10-16T09:12:44.123456Z".
# Because they're written biggest unit first (year, month, day...),
# comparing them as plain text puts them in the right time order.
WINDOW_START = "2026-10-16"
WINDOW_END = "2026-11-15"   # anything before midnight on 15 Nov counts


def new_stats():
    """Make an empty set of counters. We keep one for the 30 days and one for everything."""
    return {
        "connections": 0,
        "ips": set(),            # a set only keeps ONE copy of each IP, so no duplicates
        "login_attempts": 0,
        "logins_success": 0,
        "commands": 0,
        "usernames": Counter(),
        "passwords": Counter(),
    }


def add_event(stats, event):
    """Update one set of counters using a single log event."""
    eventid = event.get("eventid", "")

    if eventid == "cowrie.session.connect":
        # Every attacker session starts with a "connect" event
        stats["connections"] += 1
        # TODO (your turn): add this event's source IP to stats["ips"]
        # Hint: the IP is stored under the key "src_ip", and sets use .add()
        stats["ips"].add(event.get("src_ip", ""))

    elif eventid in ("cowrie.login.failed", "cowrie.login.success"):
        # A username + password guess
        stats["login_attempts"] += 1
        stats["usernames"][event.get("username", "")] += 1
        stats["passwords"][event.get("password", "")] += 1
        if eventid == "cowrie.login.success":
            # Cowrie lets some guesses "succeed" on purpose, to see what attackers do next
            stats["logins_success"] += 1

    elif eventid == "cowrie.command.input":
        # A command typed (or sent by a script) after getting in
        stats["commands"] += 1


def print_stats(title, stats):
    """Print one set of counters in a readable way."""
    print(f"\n=== {title} ===")
    print(f"Connections:          {stats['connections']:,}")
    print(f"Unique attacker IPs:  {len(stats['ips']):,}")
    print(f"Login attempts:       {stats['login_attempts']:,}")
    print(f"Successful logins:    {stats['logins_success']:,}")
    print(f"Commands run:         {stats['commands']:,}")

    print("Top 10 usernames tried:")
    for name, count in stats["usernames"].most_common(10):
        print(f"  {count:>6,}  {name!r}")   # !r shows quotes, so blank names are visible

    print("Top 10 passwords tried:")
    for password, count in stats["passwords"].most_common(10):
        print(f"  {count:>6,}  {password!r}")


def main():
    # sys.argv is the list of words typed in the terminal: [script name, folder]
    if len(sys.argv) != 2:
        print("Usage: python src/count_attacks.py <folder with cowrie.json files>")
        sys.exit(1)

    log_folder = Path(sys.argv[1])
    files = sorted(log_folder.glob("cowrie.json*"))   # today's file + every dated one
    if not files:
        print(f"No cowrie.json files found in {log_folder}")
        sys.exit(1)

    window = new_stats()       # just the 30 days
    everything = new_stats()   # the whole run
    bad_lines = 0

    for file in files:
        # errors="replace" stops one weird character in an attacker's input crashing the script
        with open(file, encoding="utf-8", errors="replace") as f:
            for line in f:                     # Cowrie writes one JSON event per line
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    bad_lines += 1             # count broken lines instead of crashing
                    continue

                add_event(everything, event)
                timestamp = event.get("timestamp", "")
                if WINDOW_START <= timestamp < WINDOW_END:
                    add_event(window, event)

    print(f"Read {len(files)} files ({bad_lines} broken lines skipped)")
    print_stats("30-day dataset: 16 Oct - 14 Nov 2026", window)
    print_stats("Full run: 16 Oct - 24 Nov 2026", everything)


# Only run main() when the file is run directly, not when another script imports it
if __name__ == "__main__":
    main()