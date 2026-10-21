# Devlog

Newest entries first. One entry every day while the honeypot collects (Day 1 to Day 30), then one for every day I work on the project.

## Day 6 – Wed 21 Oct 2026

- Honeypot: live, day 6
- Numbers (00:00 to about 22:05 UTC): 82 connections, 55 unique IPs, 4 logins, 0 commands, 0 files
- 77.239.124.x logged in twice more as root with random 8 letter passwords (QSJRjOdY, nIsasMUc). That's 4 out of the last 5 days for this IP, always root, always a new random password, never runs anything after. Looks like a slow brute force bot that just keeps going (T1110.001).
- Other logins: admin/admin and root with an empty password. No commands at all today.
- Learned: not every bot is fast and noisy. This one comes back a couple of times a day for days, which would be easy to miss if you only looked for big spikes.
- Next: check what the 4 files saved late on Monday were (hashes only), then start the Stage 3 sign-ups

## Day 5 – Tue 20 Oct 2026 (written up Wed 21 Oct from the logs)

- Honeypot: live, day 5
- Numbers: 87 connections, 51 unique IPs, 2 logins, 1 command, 0 files
- 138.68.30.x logged in as firedancer/firedancer. Firedancer is software for running Solana crypto nodes, so this bot is looking for crypto servers specifically.
- After logging in it ran "/bin/./uname -s -v -n -r -m", the same odd command as the 4 IPs on Sunday. That's 5 different IPs now with the exact same signature. Going to check in Stage 3 whether they all belong to the same hosting company.
- 77.239.124.x came back again: root with another random 8 letter password (KGRcmSqP).
- Busiest IP was 47.116.108.x with 6 connections but it never tried to log in, just scanning.
- Learned: the usernames tell you what the bot is hunting for. pi = Raspberry Pi, nvidia = Jetson boards, firedancer = Solana nodes.
- Next: today's numbers

## Day 4 – Mon 19 Oct 2026

- Honeypot: live, day 4
- Numbers (00:00 to about 21:50 UTC): 79 connections, 49 unique IPs, 1 login, 0 commands. A lot quieter on logins than Sunday even though the connections stayed high, so mostly scanners today.
- Caught up on Sat and Sun from the old log files. Cowrie keeps each day in its own file (cowrie.json.2026-10-18 etc.), so nothing was lost while I was busy.
- Built hpday, a script that prints one day's summary (counts, busiest IPs, logins, commands, saved files) and masks the last part of every IP automatically so it's safe to screenshot.
- Problems:
  - First paste of the script came out jumbled in Windows Terminal (half lines, "EOFo"). Pasted it again in one go and it worked.
  - I'd typed `bash` on its own first, which opened a shell inside my shell. Means I need to type exit twice to log off.
  - Script couldn't find Sunday's log because I used 2026_10_18 and the real name is 2026-10-18. ls showed the right name.
- Used Claude (AI) to help me understand Sunday's activity, especially the long recon script and the chmod/nohup "sshd" command. I then ran the checks myself to confirm it, e.g. that the same filter file hash (af77b643...) showed up from two different IPs, and that no file was saved for the IP that tried to run "sshd".
- Learned: sed -i to fix a line in a file, grep -h to search all the log files at once, and that file uploads (scp/sftp) are logged as a different event (file_upload) from downloads.
- Next: finish checking the "sshd" upload, then start Stage 3 (Python pipeline)

## Day 3 – Sun 18 Oct 2026 (written up Mon 19 Oct from the logs)

- Honeypot: live, day 3. Busiest day so far, the log was nearly double Saturday's size
- Numbers: 53 unique IPs, 17 logins, 17 commands, 2 files saved
- First malware attempt: 144.225.8.x logged in as root/ubuntu and ran chmod +x then nohup on a file called "sshd" in a folder with a random number name. Naming it sshd is to hide it as the real SSH service (T1036.005). No file was actually saved for that IP so the payload never arrived.
- Same bot from 4 IPs: user/1 login then "/bin/./uname -s -v -n -r -m". The weird /bin/./ path is basically a signature, noting it for a Sigma rule in Project 2.
- 195.178.110.x ran the same recon script as yesterday's 92.118.39.x and the "filter" file had the exact same SHA256 (af77b643...). Different IP, same tool.
- 77.239.124.x came back for a second day with another random 8 character password.
- Device default logins tried: pi/raspberry, nvidia/nvidia, gpadmin/gpadmin123, nginx/nginx, esroot/esroot, admin/admin. 79.175.176.x went through 5 of them in about a minute (T1110).
- Problem: the hpday script said "No log called ...2026_10_18". Cowrie names old logs with dashes (2026-10-18), not underscores. Checked with ls and fixed.
- Learned: matching file hashes across different IPs links them to the same tool. Also bots go after default logins for specific devices, not just root.
- Next: check if the "sshd" was ever uploaded (file_upload events), then today's numbers

## Day 2 – Sat 17 Oct 2026

- Honeypot: live, day 2
- Numbers (00:00 to about 19:00 UTC): 64 connections, 38 unique IPs (more than double yesterday), 5 logins, 5 commands, 1 file saved
- First real logins today. Passwords tried: a random one (QIjLZKhA), qwe123!@, 000000, an empty password, and vagrant/vagrant. The vagrant one is a default account people leave on test VMs, so bots try defaults as well as guessing (T1078.001).
- 47.84.20.x logged in twice, an hour apart with different creds, and ran `uname -s -v -n -r -m` both times (T1082)
- 92.118.39.x ran one long recon script: CPU type, core count, CPU model, NVIDIA GPU check, uptime and `last`. It also wrote a tiny script called "filter", ran it and deleted it. Looks like it was checking if the box is good for mining and whether it's a honeypot before sending anything else.
- Learned: jq `select(.eventid=="...")` to pull out one event type. Also how to read someone else's bash script line by line.
- Next: check what the saved file is (hash only, not opening it), then write my first LinkedIn post

## Day 1 – Fri 16 Oct 2026 (went live)

- Honeypot: LIVE since late morning. Port 22 is open to the internet and everything that hits it goes into Cowrie.
- Built today:
  - Installed Cowrie under its own user called cowrie, with no password and no sudo. If anyone ever got out of the fake shell, they'd only be that user and couldn't touch the rest of the server.
  - Gave Cowrie its own Python virtual environment so its packages don't mix with the system ones.
  - Made it a systemd service so it starts on boot and restarts itself if it crashes. Rebooted to check, and it came back on its own.
  - Added a firewall rule in ufw that quietly redirects port 22 to Cowrie's port, so attackers think they're hitting normal SSH. My real login is on a different port that only my home IP can reach.
  - Wrote a small Bash script called hpstats that counts today's connections, unique IPs, login attempts and commands, and leaves out my own visits.
- Tested it: logged in to the fake shell from inside the server, then from my laptop over the internet. It shows a fake Debian box called "svr04" and logged every command I typed. When I connected from my laptop, the fingerprint matched the one Cowrie showed inside the server, which proved the redirect was working. Only after all that did I change port 22 in AWS from my IP to anywhere.
- First visitors: 3 different outside IPs and 5 connections in roughly the first hour. No password guesses yet, just scanners knocking on the door.
- Problems and how I fixed them:
  - My first login to the fake shell kept getting "Permission denied". Cowrie refuses a few obvious passwords like 123456 on purpose so it looks more like a real server. A different password worked.
  - Got kicked out after 3 wrong tries and then ran whoami without noticing. It said "cowrie", so I was on the real server, not in the honeypot. The prompt is the giveaway: the fake one says root@svr04.
  - Typed a command while tail -f was still running and nothing happened. tail -f takes over the terminal until you press Ctrl+C.
  - My laptop remembered the real server's fingerprint from port 22, so I cleared it with ssh-keygen -R before testing. Otherwise SSH would have warned me the host had changed, which is exactly the man-in-the-middle check doing its job.
- Learned: Cowrie logs exactly what people type, even mistakes. I accidentally pasted a whole command into the password box and it saved it as the password. I need to filter out my own IP so my tests don't count as attacks.
- Next: run hpstats every day, write my first LinkedIn post after 24 hours, and start the Python pipeline in Stage 3.

## Setup – Fri 16 Oct 2026

- Honeypot: not live yet (Stage 1 done, Cowrie next)
- Built today: finished locking down the server. Moved my real SSH login off port 22 onto a high port, so port 22 is free for the honeypot later. Turned off password login and root login, and set it to drop a connection after 3 failed tries. Turned on ufw so the server has its own firewall as well as the AWS security group, and closed port 22 in both.
- How I did it without locking myself out: opened the new port in both firewalls first, set SSH to listen on both ports, then tested the new port in a second terminal while keeping the first one open. Only once that worked did I remove port 22.
- Tested it: password login gets "Permission denied (publickey)", root login gets refused even with my key, and port 22 times out. Rebooted the server and could still log in, so the settings survive a restart.
- Problem and how I fixed it: ran a PowerShell command while I was still logged in to the server, so bash threw a syntax error. Realised from the prompt (ubuntu@... vs PS C:\) that I was in the wrong place, and ran it again on my laptop.
- Learned: the order matters when changing SSH. Open first, test, then close. Also always check the prompt to see which machine you're actually typing into.
- Next: put this repo on GitHub, then install Cowrie and go live.

## Setup – Thu 15 Oct 2026

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
