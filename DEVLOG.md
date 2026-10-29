# Devlog

Newest entries first. One entry every day while the honeypot collects (Day 1 to Day 30), then one for every day I work on the project.

## Day 14 – Thu 29 Oct 2026

- Honeypot: live, day 14
- Numbers (so far today): 63 connections, 41 unique IPs, 6 logins, 4 commands, 0 files
- 107.170.58.x logged in as lighthouse/123456 then ran "/bin/./uname -s -v -n -r -m". That signature is now up to 7 different IPs. Lighthouse looks like the name of a cloud server product, so the bot is guessing its default login.
- 183.30.219.x: root/ubuntu then the fake "sshd" again, same as most days this week
- 164.30.17.x ran "echo xsec". Just checking the shell actually runs commands, probably a honeypot test.
- 195.3.220.x (busiest IP on Monday) came back, logged in as root/Admin123! and ran whoami
- Learned: some bots run a tiny harmless command first just to see if they get a real answer back
- Next: Sunday LinkedIn post (2 weeks of data), then start Stage 3

## Day 13 – Wed 28 Oct 2026 (written up Thu 29 Oct from the logs)

- Honeypot: live, day 13
- Numbers: 113 connections, 69 unique IPs (most so far), 3 logins, 0 commands, 0 files
- Busiest day for connections but the quietest for actual activity. Logins were admin/admin, 0/0 and root/linux, and none of them ran anything.
- Learned: more connections doesn't mean more danger. Most of it is scanning.

## Day 12 – Tue 27 Oct 2026 (written up Thu 29 Oct from the logs)

- Honeypot: live, day 12
- Numbers: 83 connections, 47 unique IPs, 1 login, 1 command, 0 files
- The only login was 218.51.197.x (root/ubuntu), the same IP that did the fake "sshd" on Friday. Came back 4 days later and did exactly the same thing again.

## Day 11 – Mon 26 Oct 2026 (written up Thu 29 Oct from the logs)

- Honeypot: live, day 11
- Numbers: 82 connections, 53 unique IPs, 2 logins, 1 command, 0 files
- 193.95.2.x: root/ubuntu then the fake "sshd". One of the IPs it passed to the program was 103.180.163.x, which attacked me itself on Saturday with the same "sshd" trick. So the infected machines seem to share each other's addresses, which looks like a botnet passing round a peer list.

## Day 10 – Sun 25 Oct 2026

- Honeypot: live, day 10
- Numbers (full day): 105 connections, 66 unique IPs, 4 logins, 7 failed, 7 commands, 1 file saved
- First real malware sample. 60.205.183.x logged in as root/password and ran an automated install:
  - `cat /bin/echo` to work out the CPU type so it sends the right build (T1082)
  - opened a raw TCP connection with bash's /dev/tcp to 39.106.149.x port 60122 and sent "GET /linux" to download a file. No wget or curl needed (T1105)
  - saved exactly 1,458,464 bytes to a random name in /tmp
  - bits of the binary leaked into the log: "ELF" (a Linux program) and "UPX!" (packed to hide it from antivirus, T1027.002)
- Cowrie saved it as 2111d820...25200d46. Not opening it or copying it anywhere. VirusTotal hash check still to do.
- Other logins: admin/admin, root/abcd1234 (ran uname -a), root with an empty password
- Learned: you can download files with nothing but bash using /dev/tcp. A rule that only watches for wget/curl would miss this completely. Good idea for a Sigma rule in Project 2.

## Day 9 – Sat 24 Oct 2026 (written up Thu 29 Oct from the logs)

- Honeypot: live, day 9
- Numbers: 99 connections, 54 unique IPs, 6 logins, 10 failed, 12 commands, 3 files saved
- Three different IPs (4.4.66.x, 103.180.163.x, 217.218.10.x) all logged in as root/ubuntu and ran the fake "sshd" within 6 hours. The folder name starts with a dot so a normal ls won't show it (T1564.001).
- 92.118.39.x came back (it was here on day 2) and ran the "filter" recon script 3 times. Same hash as every other time (af77b643...).

## Day 8 – Fri 23 Oct 2026 (written up Thu 29 Oct from the logs)

- Honeypot: live, day 8
- Numbers: 94 connections, 57 unique IPs, 9 logins, 15 commands, 3 files saved
- 218.51.197.x: root/ubuntu then the fake "sshd", this time passing it a list of other IP addresses
- 159.65.99.x did user/1 then nvidia/nvidia, both followed by "/bin/./uname", the same pattern as 138.197.216.x on day 3
- 92.118.39.x ran the "filter" script 3 times with passwords 123, 1234, 12345. It logged in fine on the first one but kept going anyway, so the bot just works through its list without checking.

## Day 7 – Thu 22 Oct 2026 (written up Thu 29 Oct from the logs)

- Honeypot: live, day 7
- Numbers: 100 connections, 52 unique IPs, 7 logins, 11 commands, 3 files saved
- 195.178.110.x came back (first seen day 3) and ran the "filter" script 3 times, same hash again
- 8.219.94.x tried admin2/admin2 and adminuser/adminuser and ran "uname -s -v -n -r -m" without the /bin/./ part, so a different bot from the signature one

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
