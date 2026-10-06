---
title: "AWS Advanced Ruby Driver Wrapper is generally available"
date: "2026-10-06"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-ruby-driver-wrapper-available/"
tags: ["RDS", "2026", "GA", "security"]
nav_exclude: true
---

# AWS Advanced Ruby Driver Wrapper is generally available

**날짜:** 2026년 10월 06일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-ruby-driver-wrapper-available/

## 내용

The Amazon Web Services (AWS) Advanced Ruby Driver Wrapper is now generally available for use with Amazon RDS and Amazon Aurora PostgreSQL and MySQL-compatible databases. This advanced database driver reduces RDS Blue/Green switchover, Aurora Global database switchover and database failover times, improving application availability. Additionally, it supports multiple authentication mechanisms for your database, including AWS Secrets Manager authentication, and token-based authentication with AWS Identity and Access Management (IAM).
The AWS Advanced Ruby Driver Wrapper builds on top of the community pg (PostgreSQL), and the mysql2 (MySQL) drivers to provide enhanced functionality beyond standard database connectivity. The wrapper is natively integrated with Aurora and RDS databases, enabling it to monitor database cluster status and quickly connect to newly promoted writers during unexpected failures that trigger database failovers. Furthermore, the wrapper seamlessly integrates with the ActiveRecord through provided aws_postgresql and aws_mysql2 adapters, so you can enable it without changing your application code.
The driver is available as an open-source project under the Apache 2.0 license. Refer to the instructions on the GitHub repository to get started.

## 핵심 요약

요약 미지원
