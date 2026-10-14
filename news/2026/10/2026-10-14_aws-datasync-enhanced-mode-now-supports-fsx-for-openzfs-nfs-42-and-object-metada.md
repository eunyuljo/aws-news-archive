---
title: "AWS DataSync Enhanced mode now supports FSx for OpenZFS, NFS 4.2, and object metadata controls"
date: "2026-10-14"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/datasync-enhanced-openzfs-nfs42-metadata/"
tags: ["Config", "2026", "new-region"]
nav_exclude: true
---

# AWS DataSync Enhanced mode now supports FSx for OpenZFS, NFS 4.2, and object metadata controls

**날짜:** 2026년 10월 14일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/datasync-enhanced-openzfs-nfs42-metadata/

## 내용

AWS DataSync Enhanced mode now supports Amazon FSx for OpenZFS as a source or destination location, NFS version 4.2 for on-premises NFS servers and FSx for OpenZFS file systems, and a new ObjectMetadata option for object storage transfers. Previously, customers transferring data to or from FSx for OpenZFS were limited to Basic mode.
NFS 4.2 lets you transfer data from NFS servers on the latest version without reconfiguring them to an older protocol version. The ObjectMetadata option gives you control over whether an object's user metadata is copied to the destination, which helps when destination metadata must stay intact, such as buckets served by AWS Storage Gateway, or when source metadata keys are not compatible with the destination, such as Azure Blob Storage. Existing tasks remain unaffected and continue to run as scheduled.
These capabilities are available for Enhanced mode tasks in all AWS Regions where AWS DataSync Enhanced mode is supported. To learn more, visit the AWS DataSync documentation.

## 핵심 요약

요약 미지원
