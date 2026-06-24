---
title: "Amazon CloudWatch Logs supports managed syslog ingestion"
date: "2026-06-24"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-cloudwatch-syslog-ingestion/"
tags: ["CloudWatch", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# Amazon CloudWatch Logs supports managed syslog ingestion

**날짜:** 2026년 06월 24일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-cloudwatch-syslog-ingestion/

## 내용

Amazon CloudWatch Logs supports managed syslog ingestion, enabling customers to send syslog messages from firewalls, routers, switches, and Linux servers directly into CloudWatch Logs.  With today's launch, customers can configure their network devices and servers to send syslog messages over TCP, TCP+TLS, or UDP to a VPC endpoint in their account - without installing or managing any agents. Amazon CloudWatch Logs supports RFC 5424, RFC 3164, and Cisco FTD/ASA syslog formats, making it compatible with a wide range of infrastructure. Amazon CloudWatch Logs automatically parses incoming syslog messages and extracts structured fields such as facility, severity, hostname, and application name, thereby eliminating the need for custom parsing pipelines. For example, customers can ingest syslog from their network firewalls and immediately query by severity or hostname using Logs Analytics to investigate security events or troubleshoot connectivity issues. This feature helps teams centralize infrastructure log visibility, simplify operational workflows, and reduce the overhead of deploying and maintaining log collection agents across distributed environments.  Available in all commercial AWS Regions except Middle East (UAE), Middle East (Bahrain), and Israel (Tel Aviv). To get started, see the Amazon CloudWatch Logs documentation.

## 핵심 요약

요약 미지원
