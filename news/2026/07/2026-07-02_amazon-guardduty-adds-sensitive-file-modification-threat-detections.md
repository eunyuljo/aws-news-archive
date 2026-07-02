---
title: "Amazon GuardDuty adds sensitive file modification threat detections"
date: "2026-07-02"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-guardduty-sfm/"
tags: ["EC2", "2026", "GA", "security"]
nav_exclude: true
---

# Amazon GuardDuty adds sensitive file modification threat detections

**날짜:** 2026년 07월 02일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-guardduty-sfm/

## 내용

Amazon GuardDuty Runtime Monitoring now includes three new threat detections that alert security teams when sensitive files are modified on Amazon EC2 instances and container workloads running on Amazon EKS or Amazon ECS. These findings help identify post-compromise attacker activities by monitoring critical system files, including configuration files, authentication settings, and system logs. This capability is designed for security teams, DevSecOps professionals, and cloud security architects who need comprehensive threat visibility across their AWS compute environments.  The new detections—Persistence:Runtime/SensitiveFileModified, PrivilegeEscalation:Runtime/SensitiveFileModified, and DefenseEvasion:Runtime/SensitiveFileModified—help identify attempts to maintain persistent access, escalate privileges, and evade detection after an initial system compromise. By monitoring five specific file operations (open-for-write, rename, symlink, link, and unlink) directly, these findings can detect threats even when attackers use obfuscated techniques that bypass traditional command-line monitoring. The correlation-based analysis distinguishes malicious behavior from legitimate administrative operations, helping reduce false positives while providing actionable intelligence with MITRE ATT&amp;CK® tactics mapping and remediation recommendations.  These sensitive file modification findings are now available to all customers who have enabled GuardDuty Runtime Monitoring for their Amazon EC2, Amazon EKS, or Amazon ECS workloads. A 30-day free trial is available for new users. To learn more, see Amazon GuardDuty Findings. To receive programmatic updates on new Amazon GuardDuty features and threat detections, please subscribe to the Amazon GuardDuty SNS topic.

## 핵심 요약

요약 미지원
