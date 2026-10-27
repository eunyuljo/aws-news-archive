---
title: "Amazon WorkSpaces Core Managed Instances now supports ModifyVolume API"
date: "2026-10-27"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-workspaces-cmi-modifyvolume/"
tags: ["EC2", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon WorkSpaces Core Managed Instances now supports ModifyVolume API

**날짜:** 2026년 10월 27일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-workspaces-cmi-modifyvolume/

## 내용

Amazon WorkSpaces Core Managed Instances now supports the ModifyVolume API, which lets you change volume size, volume type, IOPS, or throughput in place, without detaching the volume or restarting the instance. Previously, changing storage capacity or performance on a deployed managed instance required rebuilding it. 
With ModifyVolume, you can increase volume size up to 16,384 GiB, switch between supported Amazon EBS volume types, adjust IOPS for gp3, io1, and io2 volumes, and modify throughput for gp3 volumes. The API supports idempotency tokens to prevent duplicate changes, and you can track progress with the Amazon EC2 DescribeVolumesModifications operation. 
ModifyVolume is available in all AWS Regions where Amazon WorkSpaces Core Managed Instances is available. 
To get started, call ModifyVolume directly, or use it through your WorkSpaces Core partner solution once available. To learn more, see ModifyVolume in the WorkSpaces Instances API Reference and Limitations in the Amazon EBS User Guide, or visit WorkSpaces Core.

## 핵심 요약

요약 미지원
