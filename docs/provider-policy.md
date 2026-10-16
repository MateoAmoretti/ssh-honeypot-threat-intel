# Cloud provider policy check

Before deploying the honeypot, I checked that my cloud provider's rules allow it.

- **Provider:** Amazon Web Services (AWS), Europe (Stockholm) region
- **Date checked:14/10/2026
- **Documents read:**
  - [AWS Acceptable Use Policy](https://aws.amazon.com/aup/)

## 1. Does anything forbid running a honeypot or a deliberately vulnerable service?

Answer: No. The word "honeypot" does not appear anywhere in the AWS Acceptable Use Policy. The policy bans using AWS to attack or harm other people's systems.
A honeypot doesn't attack anyone. It waits for attackers to connect and record what they do, so I don't think it breaks this rule.


Closest clause (short quote):  you may not use the services "to violate the
security, integrity, or availability of any user, network, computer or
communications system".

## 2. Does anything forbid storing malicious code?

Cowrie saves files that attackers download by default, so this matters.

Answer: The policy doesn't mention storing malware directly. But if attacker files sat on my server and were ever spread or run, that could harm other systems and break the rule above. So I will never run, open or share these files. I only keep their hashes (fingerprints) to look up on VirusTotal, and the files themselves never leave the server

## 3. What happens if AWS receives an abuse complaint about my server's IP address?

Answer:  AWS can investigate suspected violations and can remove or disable
anything that breaks the policy, which could mean suspending my server. AWS
would contact me about the complaint. Because my honeypot only receives
connections and never attacks anyone, I could explain what it is. If AWS
asked me to shut it down, I would.

## My decision, and the precautions I'm taking

The honeypot runs only on this cloud server, never on my home network.
- My real login is locked down: key-only, a private port and two firewalls.
- I never open, run or download the files attackers upload. I keep hashes only.
- I never scan, probe or attack back at any IP that connects to me.
- API keys stay out of GitHub (.env plus .gitignore).
- Attacker IPs are masked in anything I publish.