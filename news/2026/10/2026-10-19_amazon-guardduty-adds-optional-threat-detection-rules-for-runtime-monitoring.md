---
title: "Amazon GuardDuty adds optional threat detection rules for Runtime Monitoring"
date: "2026-10-19"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/guardduty-runtime-optional-detection-rules/"
tags: ["EC2", "2026", "new-region"]
nav_exclude: true
---

# Amazon GuardDuty adds optional threat detection rules for Runtime Monitoring

**날짜:** 2026년 10월 19일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/guardduty-runtime-optional-detection-rules/

## 내용

Amazon GuardDuty now supports optional detection rules for Runtime Monitoring. You can enable more than 50 Runtime Monitoring rules that help detect process, file, and network activity that might be routine in one environment but a sign of compromise in another, such as modifying sudoers files or disabling audit logging.
The new rules provide detections for Amazon EC2 instances, Amazon EKS, and Amazon ECS on both EC2 and AWS Fargate, and span 13 finding types mapped to MITRE ATT&amp;CK® tactics including persistence, privilege escalation, execution, defense evasion, discovery, exfiltration, and command and control. This release introduces four new finding types: CommandAndControl:Runtime/SuspiciousCommand, CredentialAccess:Runtime/SensitiveFileRead, Discovery:Runtime/SensitiveFileRead, and Exfiltration:Runtime/SuspiciousCommand.
To get started, visit the GuardDuty console. You can enable rules in dry-run mode to evaluate detection efficacy before enabling live detection.
Custom Detection Rules for Runtime Monitoring is available in all AWS commercial Regions and the AWS GovCloud (US) Regions. To learn more, see Amazon GuardDuty Custom Detection Rules. To receive programmatic updates on new Amazon GuardDuty features and threat detections, subscribe to the Amazon GuardDuty SNS topic.

## 핵심 요약

요약 미지원
