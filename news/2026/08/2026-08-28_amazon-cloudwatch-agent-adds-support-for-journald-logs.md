---
title: "Amazon CloudWatch agent adds support for journald logs"
date: "2026-08-28"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cloudwatch-agent-journald/"
tags: ["CloudWatch", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon CloudWatch agent adds support for journald logs

**날짜:** 2026년 08월 28일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cloudwatch-agent-journald/

## 내용

AWS announces support for collecting systemd journal (journald) logs with the Amazon CloudWatch agent. You can now configure the CloudWatch agent to read log entries directly from the systemd journal on Linux instances and send them to Amazon CloudWatch Logs, without first writing those logs to files on disk. 
Many modern Linux distributions, including Amazon Linux 2023, use systemd journal as the primary logging system and no longer write traditional text log files such as /var/log/messages by default. Previously, collecting these logs with the CloudWatch agent required additional configuration to export the journal to files on disk. With this launch, the CloudWatch agent reads journald entries natively, preserving the structured metadata that journald captures, such as the systemd unit, priority, and process information. You can filter log entries using systemd units, journal priority levels, and journal field matches, and you can apply regular expression filters before logs are published to CloudWatch Logs. This helps you reduce noise and control log volume and costs. 
Support for journald in the CloudWatch agent is available in all AWS Commercial Regions and GovCloud(US) regions. Standard Amazon CloudWatch Logs pricing applies for ingested logs. For more information, see Amazon CloudWatch Pricing page. 
To get started, update to the latest version of the CloudWatch agent and add a journald section to your agent configuration file. To learn more, see Manually create or edit the CloudWatch agent configuration file in the Amazon CloudWatch User Guide.

## 핵심 요약

요약 미지원
