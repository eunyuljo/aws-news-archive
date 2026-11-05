---
title: "AWS DataSync Enhanced mode supports OpenID Connect (OIDC) for Google Cloud and Microsoft Azure"
date: "2026-11-05"
service: "CloudFormation"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/datasync-enhanced-oidc-google-azure/"
tags: ["CloudFormation", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS DataSync Enhanced mode supports OpenID Connect (OIDC) for Google Cloud and Microsoft Azure

**날짜:** 2026년 11월 05일
**서비스:** CloudFormation
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/datasync-enhanced-oidc-google-azure/

## 내용

AWS DataSync Enhanced mode now supports OpenID Connect (OIDC) authentication for Google Cloud Storage and Microsoft Azure Blob Storage locations. DataSync uses an AWS Identity and Access Management (IAM) role to get short-lived credentials from Google Cloud or Microsoft Entra ID and refreshes them automatically so your transfers run without interruption. 
You can now use DataSync to access your Google Cloud Storage and Azure Blob Storage without long-term credentials such as hash-based message authentication code (HMAC) keys or shared access signature (SAS) tokens. This lets you move data across clouds while complying with security policies that might prohibit long-term credentials. 
You can get started by adding an IAM role to your DataSync location with the AWS CLI, API, or AWS CloudFormation. This capability is available in all AWS Regions where DataSync Enhanced mode is supported. To learn more, visit the AWS DataSync User Guide.

## 핵심 요약

요약 미지원
