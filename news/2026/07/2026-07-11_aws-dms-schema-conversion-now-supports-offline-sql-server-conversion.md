---
title: "AWS DMS Schema Conversion now supports offline SQL Server conversion"
date: "2026-07-11"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-dms-schema-conversion-offline-source/"
tags: ["EKS", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS DMS Schema Conversion now supports offline SQL Server conversion

**날짜:** 2026년 07월 11일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-dms-schema-conversion-offline-source/

## 내용

AWS Database Migration Service (DMS) Schema Conversion&nbsp;now supports offline source conversion for Microsoft SQL Server, enabling you to convert SQL Server schemas and code without direct connectivity to your source databases. You extract metadata using standard database commands in your own environment, then upload it to DMS Schema Conversion for processing. This eliminates security reviews, firewall changes, and VPN setup that delay migration projects, while delivering the same conversion results as the connected approach. 
Offline Source is ideal for organizations with security policies that restrict external tool access to production SQL Server databases. Database administrators generate human-readable metadata files within their existing environment, and security teams can review the commands and output before uploading, making approval straightforward. By removing the connectivity requirement, Offline Source transforms weeks of security reviews into a simple command-and-upload workflow. 
Offline Source supports all DMS Schema Conversion targets at no additional conversion charge. For regional availability, see the&nbsp;Supported AWS Regions&nbsp;page. To get started, see&nbsp;Using Offline Source&nbsp;in the DMS Schema Conversion documentation.

## 핵심 요약

요약 미지원
