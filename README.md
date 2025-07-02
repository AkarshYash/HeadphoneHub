🛡️ Phishing Email Deactivation Tool

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Project Level](https://img.shields.io/badge/Level-Advanced-critical)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Security](https://img.shields.io/badge/Security-Focused-red.svg)

An advanced threat intelligence-based tool to detect and flag phishing emails in real time. Designed to scan email inboxes via IMAP, extract and analyze URLs from email content, and flag potential phishing attempts using pattern detection and [VirusTotal](https://www.virustotal.com/) API integration.

🔍 Description

This Python-based tool automatically connects to an email inbox, fetches all emails, parses their content, extracts any URLs, and determines if they're potentially malicious or phishing in nature. It leverages both local heuristics (suspicious keywords, domain structure) and external intelligence (VirusTotal API). Logs are generated for forensic visibility and alerting.

Ideal for SOC teams, cybersecurity learners, red/blue teams, or email security automation workflows.


⚙️ Technologies Used

| Tech           | Purpose                              |
|----------------|--------------------------------------|
| Python 3.10+   | Core programming language            |
| `imaplib`      | For email fetching via IMAP          |
| `email`        | Email content parsing                |
| `requests`     | HTTP calls to VirusTotal API         |
| `BeautifulSoup`| HTML parsing from email content      |
| `logging`      | Logging suspicious activity          |
| `re`, `urlparse`| URL extraction and validation       |

🚀 Features

- ✅ Connects to any IMAP-enabled inbox (e.g., Gmail)
- ✅ Extracts and scans all hyperlinks from email body
- ✅ Detects suspicious URLs based on domain heuristics
- ✅ Integrates with **VirusTotal API** for threat intelligence
- ✅ Logs phishing attempts with subject, sender, and URL
- ✅ CLI-driven and easy to automate (cronjob compatible)
- ✅ Clean, readable, and modular codebase
- 🔒 Focused on security-first development practices

🧠 Skill Level

Project Level: `Intermediate to Advanced`

If you're new to email protocols or phishing detection, this is a solid hands-on tool to understand:
- IMAP protocol
- Email content decoding
- URL analysis
- Threat intelligence workflows


🛠️ Installation

```bash
git clone https://github.com/yourusername/phishing-email-deactivation-tool.git
cd phishing-email-deactivation-tool
pip install -r requirements.txt
