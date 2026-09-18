# Week 4 — SOC Detection & Response Playbook
## Subdomain Takeover Exposure — SEO Scenario

## Overview

This project demonstrates a defensive SOC workflow for identifying
and responding to activity consistent with possible subdomain
takeover exposure in an SEO organization.

The project focuses on detection engineering, alert triage,
incident response, and false-positive reduction.

All testing was performed using authorized simulated log samples.

---

## Objectives

- Understand indicators associated with subdomain takeover exposure.
- Create a detection rule for suspicious DNS and HTTP patterns.
- Test the rule against suspicious and benign log samples.
- Reduce false positives through basic rule tuning.
- Develop an analyst alert-triage checklist.
- Create an incident-response playbook.
- Document detection coverage and limitations.

---

## Project Structure

```text
Week4-Subdomain-Takeover-SOC/
│
├── README.md
│
├── logs/
│   ├── attack_sample.log
│   └── benign_sample.log
│
├── detection/
│   ├── detection_rule.txt
│   └── detect_subdomain_takeover.py
│
├── testing/
│   ├── test_results.md
│   └── detection_coverage.md
│
└── playbook/
    ├── alert_triage_checklist.md
    └── incident_response_playbook.md