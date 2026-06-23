---
title: "AWS Network Firewall updates default drop action for improved connection reliability"
date: "2026-06-23"
service: "VPC"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/aws-network-firewall-updates-default-drop-action"
tags: ["VPC", "2026", "new-region"]
nav_exclude: true
---

# AWS Network Firewall updates default drop action for improved connection reliability

**날짜:** 2026년 06월 23일
**서비스:** VPC
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/aws-network-firewall-updates-default-drop-action

## 내용

AWS Network Firewall now uses "Application drop established (server-directed only)" as the default stateful action for all newly created firewall policies, replacing the previous default of "Application drop established (bidirectional)" (formerly named "Application layer drop established"). No action is required to benefit from this change when creating new policies.  AWS Network Firewall is a managed service that lets you deploy network protections across your Amazon VPCs. Previously, the “Application drop established (bidirectional)” default could silently drop legitimate server-to-client TCP packets, such as window updates, keep-alives, and resets — causing intermittent connection failures that were difficult to diagnose. With the safer default now in place, new policies avoid this issue.  If your existing environment requires “Application drop established (bidirectional)” to support post-quantum cryptography (PQC) fragmented TLS handshakes, refer to our documentation for guidance on on switching to "Application drop established (server-directed only)" or adding the “to_server” flag to your TCP drop rules so legitimate flow control packets are not blocked.  This update is available in all AWS Regions where AWS Network Firewall is offered. To get started, see Managing evaluation order for Suricata compatible rules in the AWS Network Firewall service documentation.

## 핵심 요약

요약 미지원
