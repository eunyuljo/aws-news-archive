---
title: "AWS Systems Manager now supports sharing documents through AWS Resource Access Manager"
date: "2026-09-30"
service: "SystemsManager"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/systems-manager-sharing-documents-ram/"
tags: ["SystemsManager", "2026", "new-region"]
nav_exclude: true
---

# AWS Systems Manager now supports sharing documents through AWS Resource Access Manager

**날짜:** 2026년 09월 30일
**서비스:** SystemsManager
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/systems-manager-sharing-documents-ram/

## 내용

AWS Systems Manager now lets you share your Systems Manager Documents (SSM Documents) with an entire AWS organization or with specific organizational units (OUs) using AWS Resource Access Manager (AWS RAM). Previously, you could only share a document publicly or with a list of individual account IDs. You can now easily share a document with your organization or OUs, and Systems Manager automatically keeps that sharing up to date as accounts are added to or removed from your organization or OU, so you no longer need to track and update accounts manually.
To share a document, you create an AWS RAM resource share, add the SSM Documents you want to share, and select the organizations or OUs to share them with. Because sharing is managed through AWS RAM and resource-based policies, access is granted through standard AWS authorization. When you share a document with an account outside your organization, that account receives a resource share invitation and gains access only after it accepts, giving both the document owner and the consumer more control over shared access.
This capability is available in the Systems Manager console, the AWS Command Line Interface (AWS CLI), and the AWS SDKs, in all AWS Regions where AWS Systems Manager is available. There is no additional charge to share documents through AWS RAM. To get started, open the Documents page in the Systems Manager console, or see the AWS Systems Manager User Guide at https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-ssm-sharing.html.

## 핵심 요약

요약 미지원
