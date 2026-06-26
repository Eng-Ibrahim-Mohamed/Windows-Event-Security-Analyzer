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
![Version](https://img.shields.io/badge/Version-v2.0-blue?style=for-the-badge)
![Blue Team](https://img.shields.io/badge/Blue-Team-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen?style=for-the-badge)

</p>

---

# 📖 Overview

**Windows Event Security Analyzer** is a Python-based cybersecurity project that reads **Windows Security Event Logs** directly from the Windows Event Viewer and analyzes authentication-related events.

The tool detects suspicious activities such as brute-force attacks, summarizes authentication statistics, generates security alerts, and provides actionable recommendations for Blue Team investigations.

This project was built to demonstrate practical knowledge of:

- Modern Windows Event Log API (EvtQuery)
- XML-Based Event Parsing
- SecurityEvent Data Model
- Detection Engine
- Rule-Based Detection Architecture
- Correlation Engine
- Brute Force Detection
- Account Compromise Detection
- MITRE ATT&CK Mapping
- Professional Alert Engine
- Time Window Correlation
- Executive Security Report
- Modular Architecture

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

## 🆕 What's New in v2.0

Version **2.0** introduces a complete architectural redesign of the project, transforming it from a basic Windows Event Log analyzer into a modular detection framework.

### Highlights

* 🚀 Migrated to the modern Windows Event Log API (**EvtQuery**)
* 📄 Introduced XML-based event parsing
* 🧩 Added the **SecurityEvent** data model and factory
* 🏗️ Redesigned the project with a modular architecture
* ⚙️ Introduced a dedicated **Detection Engine**
* 🔗 Added a **Correlation Engine** for multi-event detection
* 🚨 Implemented a professional **Alert Engine**
* ⏱️ Added time-window based correlation
* 🎯 Introduced **MITRE ATT&CK** mapping for detections
* 🔍 Added **Account Compromise Detection**
* 🧪 Expanded the project with a comprehensive testing structure
* 📁 Improved project organization for future scalability


# 🏗️ Architecture

```text
Windows Security Log

↓

Event API

↓

XML Parser

↓

SecurityEvent Factory

↓

Detection Engine

↓

Correlation Engine

↓

Alert Engine

↓

Security Report

---

# 📂 Project Structure

```text
Windows-Event-Security-Analyzer
│
├── assets
│   ├── banner.png
│   └── dashboard.png
│
├── core
│   ├── __init__.py
│   ├── alert_engine.py
│   ├── correlation_engine.py
│   ├── detection_engine.py
│   ├── event_api.py
│   ├── models.py
│   ├── parser.py
│   ├── security_event_factory.py
│   ├── xml_parser.py
│   │
│   ├── rules
│   │   ├── __init__.py
│   │   ├── authentication.py
│   │   ├── correlation.py
│   │   └── privilege.py
│   │
│   └── utils
│       ├── __init__.py
│       └── time_utils.py
│
├── tests
│   ├── alert_test.py
│   ├── core_test.py
│   ├── correlation_test.py
│   ├── detection_test.py
│   ├── event_api_test.py
│   ├── event_test.py
│   ├── extract_user.py
│   ├── factory_test.py
│   ├── success_test.py
│   ├── time_test.py
│   └── xml_test.py
│
├── analyzer.py
├── recommendations.py
├── report_generator.py
├── requirements.txt
├── LICENSE
├── README.md
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

## 📄 Sample Reports

### Version 1.1

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

### 🚀 Version 2.0

```text
==================================================
WINDOWS SECURITY REPORT
Version 2.0
==================================================

EXECUTIVE SUMMARY

Overall Risk      : CRITICAL

Events Analysed   : 104

Alerts Generated  : 2

==================================================

SECURITY STATISTICS

Failed Logins      : 6

Successful Logins  : 47

Admin Logins       : 47

==================================================

SECURITY ALERTS

==================================================
                 SECURITY ALERT
==================================================

Title              : Possible Brute Force Attack

Severity           : HIGH

Risk Level         : HIGH

MITRE ATT&CK       : T1110 - Brute Force

Event ID           : 4625

Affected User      : AL-MOMEN

Description
--------------------------------------------------
Multiple failed login attempts (6) were detected
for user 'AL-MOMEN'.

Recommended Action
--------------------------------------------------
• Verify the user's identity.
• Review recent login history.
• Reset the password if the activity is unauthorized.
• Investigate the source IP address.

==================================================

```

RECOMMENDATIONS

• Review failed login attempts.
• Verify affected user credentials.
• Enable Account Lockout Policy.
• Review Windows Security Logs.
```

---

# 🔍 Detection Rules

## Supported Detection Rules

- Failed Login Detection
- Successful Login Detection
- Privileged Logon Detection
- Account Compromise Correlation
- Brute Force Detection


Future releases will include additional detection rules.

---

# 🛠️ Technologies Used

- Python
- pywin32
- Windows Event Logs
- Windows Security
- Blue Team Concepts
- XML Parsing
- MITRE ATT&CK
- Rule Engine

Windows Event Log API

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

---

# 🗺️ Roadmap

## ✅ Version 1.0

* Windows Security Event Reader
* Failed Login Detection
* Successful Login Detection
* Privileged Logon Detection
* Brute Force Detection
* Basic Alert Engine
* Executive Summary
* Security Recommendations
* Professional Security Report
* Modular Project Structure

---

## ✅ Version 2.0 (Current Stable Release)

This release represents a complete architectural redesign of the project.

### Core Improvements

* Modern Windows Event Log API (EvtQuery)
* XML-Based Event Parsing
* SecurityEvent Data Model
* SecurityEvent Factory
* Detection Engine
* Rule-Based Detection Architecture
* Correlation Engine
* Professional Alert Engine
* Time Window Correlation
* Account Compromise Detection
* MITRE ATT&CK Mapping
* Refactored Project Architecture
* Improved Test Suite

---

## 🚀 Version 2.1

* Suspicious RDP Login Detection
* Remote Authentication Monitoring
* Enhanced Login Analysis

---

## 🚀 Version 2.2

* Privilege Abuse Detection
* Elevated Session Monitoring
* Privileged Logon Analysis

---

## 🚀 Version 2.3

* Account Lockout Detection
* Authentication Failure Correlation
* Account Enumeration Detection

---

## 🚀 Version 2.4

* Password Spray Detection
* Credential Attack Correlation
* Authentication Pattern Analysis

---

## 🚀 Version 2.5

* Attack Timeline
* Event Correlation Timeline
* Chronological Investigation View

---

## 🚀 Version 2.6

* Risk Score Engine
* Threat Severity Calculation
* Executive Risk Summary

---

## 🚀 Version 2.7

* HTML Security Dashboard
* Interactive Charts
* Security Metrics Visualization

---

## 🚀 Version 2.8

* PDF Security Reports
* JSON Export
* Report Templates

---

## 🚀 Version 3.0

* EVTX File Analysis
* Multiple Log Source Support
* Detection Packs
* Sigma Rule Support
* IOC Detection
* Real-Time Monitoring
* Live Alerting
* Multi-Host Analysis
* Threat Hunting Features
* Enterprise Reporting


---

# 🤝 Contributing

Contributions are welcome.

If you'd like to improve the project, feel free to fork the repository and submit a Pull Request.

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