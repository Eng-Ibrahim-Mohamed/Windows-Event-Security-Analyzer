<p align="center">
  <img src="assets/banner.png" alt="Windows Event Security Analyzer Banner">
</p>
<h1 align="center">🛡️ Windows Event Security Analyzer</h1>

<p align="center">
A Python-based Blue Team tool for analyzing Windows Security Event Logs, detecting suspicious authentication activities, and generating professional security reports.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-v1.0-orange?style=for-the-badge)
![Blue Team](https://img.shields.io/badge/Blue-Team-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen?style=for-the-badge)

</p>

---

# 📖 Overview

**Windows Event Security Analyzer** is a Python-based cybersecurity project that reads **Windows Security Event Logs** directly from the Windows Event Viewer and analyzes authentication-related events.

> **Current Stable Release:** **v1.0.0**
>
> 🚧 Development of **Version 2.0** is currently in progress. The next major release introduces a completely redesigned architecture based on the modern Windows Event Log API for improved scalability, extensibility, and future detection capabilities.

The tool detects suspicious activities such as brute-force attacks, summarizes authentication statistics, generates security alerts, and provides actionable recommendations for Blue Team investigations.

This project was built to demonstrate practical knowledge of:

- Windows Event Logs
- Blue Team Operations
- Detection Engineering
- Security Monitoring
- Python Automation
- SOC Fundamentals

---

# ✨ Features

- 🔍 Read Windows Security Event Logs
- 🚫 Detect Failed Login Attempts (Event ID 4625)
- ✅ Detect Successful Logins (Event ID 4624)
- 👑 Detect Privileged Logons (Event ID 4672)
- 🚨 Brute Force Detection
- ⚠️ Alert Engine
- 📊 Executive Summary
- 💡 Security Recommendations
- 📄 Professional Report Generation
- 🏗️ Modular Project Architecture

---

# 📸 Screenshot

Create a folder named:

```
assets/
```

Place your report screenshot inside it:

```
assets/dashboard.png
```

Then enable this image:

```markdown
![Dashboard](assets/dashboard.png)
```

---

# 🏗️ Architecture

```text
Windows Event Viewer
        │
        ▼
event_reader.py
        │
        ▼
detections.py
        │
        ▼
alerts.py
        │
        ▼
recommendations.py
        │
        ▼
report_generator.py
        │
        ▼
Security Report
```

---

# 📂 Project Structure

```text
Windows-Event-Security-Analyzer
│
├── assets
│   ├── banner.png
│   └── dashboard.png
│
├── analyzer.py
├── event_reader.py
├── detections.py
├── alerts.py
├── recommendations.py
├── report_generator.py
│
├── tests
│   ├── event_test.py
│   ├── extract_user.py
│   └── success_test.py
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Eng-Ibrahim-Mohamed/Windows-Event-Security-Analyzer.git
```

Move into the project

```bash
cd Windows-Event-Security-Analyzer
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Usage

Run the analyzer

```bash
python analyzer.py
```

---

# 📄 Sample Report

```text
==================================================
WINDOWS SECURITY REPORT
Version 1.0
==================================================

EXECUTIVE SUMMARY

Overall Risk      : HIGH

Events Analysed   : 199

Alerts Generated  : 1

==================================================

SECURITY STATISTICS

Failed Logins      : 3

Successful Logins  : 98

Admin Logins       : 98

==================================================

SECURITY ALERTS

[HIGH]

BRUTE FORCE DETECTED

Target User : AL-MOMEN

Source IP   : 127.0.0.1

Attempts    : 3

Status      : OPEN

==================================================

RECOMMENDATIONS

• Review failed login attempts.
• Verify affected user credentials.
• Enable Account Lockout Policy.
• Review Windows Security Logs.
```

---

# 🔍 Detection Rules

Current detection capabilities:

- Failed Login Detection
- Successful Login Detection
- Privileged Logon Detection
- Brute Force Detection

Future releases will include additional detection rules.

---

# 🛠️ Technologies Used

- Python
- pywin32
- Windows Event Logs
- Windows Security
- Blue Team Concepts
-  Windows Event Log API (Upcoming)
- XML Parsing (Upcoming)

---

# 🎯 Learning Objectives

This project demonstrates practical experience with:

- Windows Authentication Events
- Windows Security Logs
- Log Analysis
- Detection Engineering
- Incident Detection
- Blue Team Methodology
- SOC Monitoring
- Python Security Automation
- Windows Event Log API
- XML Event Parsing
- Software Architecture

---

# 🗺️ Roadmap

## ✅ Version 1.0.0 (Current Stable Release)

### Features

- Windows Security Event Reader
- Failed Login Detection
- Successful Login Detection
- Privileged Logon Detection
- Brute Force Detection
- Alert Engine
- Executive Summary
- Security Recommendations
- Professional Security Report

---

# 🚧 Version 2.0.0 (In Development)

The next major release focuses on rebuilding the project architecture using the modern Windows Event Log API.

## New Architecture

- Modern Windows Event API
- XML Event Parsing
- Event Models
- Parser Layer
- Detection Pipeline
- Enterprise Architecture

## New Features

- Attack Timeline
- Risk Scoring Engine
- Enhanced Correlation
- JSON Export
- PDF Reports
- HTML Dashboard
- Live Monitoring
- Sigma Rule Support
- IOC Detection

---

# 🔮 Future Releases

## Version 2.1

- Email Notifications
- Slack Integration
- Discord Webhooks

## Version 2.2

- Windows Service
- Scheduled Scanning
- Automatic Reports

## Version 3.0

- Multi-Host Monitoring
- Centralized Log Collection
- SIEM Integration
- Threat Intelligence

# 🤝 Contributing

Contributions are welcome.

If you'd like to improve the project, feel free to fork the repository and submit a Pull Request.
---

## 🚀 Current Status

**Stable Release:** v1.0.0

**Next Milestone:** v2.0.0 – Next Generation Event Processing Engine

The project is actively under development, with a major architectural redesign planned for the next release.

---

# 👨‍💻 Author

**Ibrahim Mohamed**

Cybersecurity Student

GitHub:
https://github.com/Eng-Ibrahim-Mohamed

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.

It helps support future development and encourages more cybersecurity open-source projects.
