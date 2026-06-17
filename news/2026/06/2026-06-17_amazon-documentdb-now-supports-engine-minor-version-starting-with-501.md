---
title: "Amazon DocumentDB now supports engine minor version starting with 5.0.1"
date: "2026-06-17"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-documentdb-engine-minor-version-5-0-1/"
tags: ["CloudWatch", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon DocumentDB now supports engine minor version starting with 5.0.1

**날짜:** 2026년 06월 17일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-documentdb-engine-minor-version-5-0-1/

## 내용

Amazon DocumentDB (with MongoDB compatibility) now supports engine minor versions, starting with 5.0.1. This release delivers enhanced aggregation capabilities with new operators ($rand, $pow, $dateToParts, $dateFromParts), the active connections metric to monitor instances, and granular command-level performance metrics in CloudWatch (find, insert, findAndModify, update, etc.). For a full list of what's included, see release notes. Minor versions provide new features and bug fixes within the same major version, giving you more control over when and how you upgrade your clusters. We recommend upgrading to the latest minor version to benefit from these performance enhancements, bug fixes, and new capabilities.  You can specify minor version 5.0.1 when creating a new cluster, or manually upgrade an existing 5.0.0 cluster to 5.0.1 using the AWS Management Console or AWS CLI (via the modify-db-cluster command with --engine-version 5.0.1). Once you upgrade to a newer minor version, you cannot downgrade back to a previous minor version. Upgrading from 5.0.0 (LTS) to 5.0.1 gives you access to the latest features and fixes, but you will no longer be on the LTS track. If minimizing upgrades is your priority, you should remain on LTS. For more information, see Using a long-term support (LTS) release.  Amazon DocumentDB engine minor version 5.0.1 is available in all AWS Regions where Amazon DocumentDB 5.0 is available. Learn more about minor version upgrades and version support dates in the Amazon DocumentDB Developer Guide. Create or update a fully managed Amazon DocumentDB cluster in the Amazon DocumentDB Management Console.

## 핵심 요약

요약 미지원
