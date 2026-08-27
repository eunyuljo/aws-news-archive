---
title: "Mountpoint for Amazon S3 adds memory usage controls"
date: "2026-08-27"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/mountpoint-for-S3-adds-memory-usage-controls"
tags: ["S3", "2026", "GA", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Mountpoint for Amazon S3 adds memory usage controls

**날짜:** 2026년 08월 27일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/mountpoint-for-S3-adds-memory-usage-controls

## 내용

Mountpoint for Amazon S3 can now limit memory usage, either automatically based on the environment it runs in or with a limit that you define. This lets you run Mountpoint alongside memory-intensive applications, for example, in machine learning training or analytics workloads where applications share a memory budget. 
Previously, Mountpoint’s memory usage could expand over time based on usage patterns, potentially causing performance or stability issues when competing with other memory-intensive applications. With this launch, you can define a memory target for Mountpoint to reserve memory for your applications. Alternatively, Mountpoint can automatically determine a safe default based on the environment it runs in. For example, when running in Amazon EKS, Mountpoint can automatically detect a container's assigned memory budget. Under memory pressure, Mountpoint slows down operations to stay within this budget, enabling you to run Mountpoint in containers with strict memory allocations. &nbsp; 
Mountpoint is available in all AWS Regions. To upgrade to the latest version, visit the Mountpoint GitHub repository. To learn more about Mountpoint, see the overview page and the configuration guide in the Mountpoint GitHub repository.

## 핵심 요약

요약 미지원
