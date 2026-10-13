---
title: "AWS Transfer Family supports custom ports for public SFTP servers"
date: "2026-10-13"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/transfer-family-custom-ports-sftp/"
tags: ["Config", "2026", "GA", "new-region"]
nav_exclude: true
---

# AWS Transfer Family supports custom ports for public SFTP servers

**날짜:** 2026년 10월 13일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/transfer-family-custom-ports-sftp/

## 내용

AWS Transfer Family now lets you configure custom ports on public SFTP servers and choose a communication mode for each port. You can support clients that require different ports or start SFTP connections differently on a single server.
Previously, public SFTP servers accepted connections only on port 22 and used server-first communication. With this launch, you can configure up to three ports (22, or any port from 2000 to 65535), allowing you to use the port numbers your business or network requires and offer multiple ports on one server. Some SFTP clients initiate communication themselves, and their connections can occasionally stall on a server-first port. For each port, you can now select client-first or server-first communication and direct clients to the port that matches their connection behavior. Using a port other than 22 can also reduce unwanted connection attempts from automated scanners that target port 22.
This capability is available in all AWS Regions where Transfer Family public SFTP servers are offered. To get started, visit the AWS Transfer Family console or use the AWS CLI or AWS SDKs. To learn more, visit Create an SFTP-enabled server in the AWS Transfer Family User Guide

## 핵심 요약

요약 미지원
