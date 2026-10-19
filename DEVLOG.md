# Devlog

Newest entries first. One entry every day while the honeypot collects (Day 1 to Day 30), then one for every day I work on the project.

## Setup – Fri 16 Oct 2026

- Honeypot: not live yet (Stage 1 done, Cowrie next)
- Built today: finished locking down the server. Moved my real SSH login off port 22 onto a high port, so port 22 is free for the honeypot later. Turned off password login and root login, and set it to drop a connection after 3 failed tries. Turned on ufw so the server has its own firewall as well as the AWS security group, and closed port 22 in both.
- How I did it without locking myself out: opened the new port in both firewalls first, set SSH to listen on both ports, then tested the new port in a second terminal while keeping the first one open. Only once that worked did I remove port 22.
- Tested it: password login gets "Permission denied (publickey)", root login gets refused even with my key, and port 22 times out. Rebooted the server and could still log in, so the settings survive a restart.
- Problem and how I fixed it: ran a PowerShell command while I was still logged in to the server, so bash threw a syntax error. Realised from the prompt (ubuntu@... vs PS C:\) that I was in the wrong place, and ran it again on my laptop.
- Learned: the order matters when changing SSH. Open first, test, then close. Also always check the prompt to see which machine you're actually typing into.
- Next: put this repo on GitHub, then install Cowrie and go live.

## Setup – Fri 15 Oct 2026

- Honeypot: not live yet (Stage 1: locking down the server)
- Built today: launched a t3.micro Ubuntu 24.04 server on AWS. Imported my own public key instead of letting AWS generate one, so the private key never left my laptop. The security group only allows SSH from my home IP. Logged in for the first time and installed all updates. Started the lockdown: turned on ufw and wrote an SSH config file that turns off password and root login and adds a second, higher port.
- Problem and how I fixed it: the free plan locks the account to one region, so I couldn't use London like I planned. I switched to Stockholm instead of upgrading to a paid plan. Second problem: `sshd -t` failed with "Missing privilege separation directory: /run/sshd". It wasn't my config. On Ubuntu 24.04 SSH only starts when someone connects, so that folder doesn't exist yet. Creating it with `sudo mkdir -p /run/sshd` and running the test again fixed it.
- Learned: always open a new port in the firewall before moving SSH onto it, or you lock yourself out. Keep the old session open as a lifeline until the new one works.
- Next: finish the lockdown (close the old port, test password and root login are refused, reboot test), then push this repo to GitHub.

## Day 0 – Wed 14 Oct 2026

- Honeypot: not live yet (Stage 1: server setup)
- Built today:
- Problem and how I fixed it:
- Learned:
- Next: lock down SSH (key-only, private port, firewalls), then push this repo to GitHub
