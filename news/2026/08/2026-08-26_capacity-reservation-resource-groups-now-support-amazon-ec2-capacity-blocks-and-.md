---
title: "Capacity Reservation Resource Groups now support Amazon EC2 Capacity Blocks and interruptible Capacity Reservations"
date: "2026-08-26"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/capacity-reservation-resource-groups-ec2"
tags: ["EC2", "2026", "GA", "new-region"]
nav_exclude: true
---

# Capacity Reservation Resource Groups now support Amazon EC2 Capacity Blocks and interruptible Capacity Reservations

**날짜:** 2026년 08월 26일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/capacity-reservation-resource-groups-ec2

## 내용

Starting today, you can add Amazon EC2 Capacity Blocks for ML and interruptible Capacity Reservations to Capacity Reservation Resource Groups. Amazon EC2 offers different reservation offerings such as On-Demand Capacity Reservations (ODCRs), interruptible Capacity Reservations, and Capacity Blocks for ML. Previously, a Capacity Reservation Resource Group could only include ODCRs. Now you can add any type of Capacity Reservation to a Capacity Reservation Resource Group, making it easier to launch EC2 instances across your entire portfolio of reserved capacity. 
To use this feature, create a Capacity Reservation Resource Group, add any Capacity Reservation to it, and then target the group in your launch request. When using EC2 Fleet and EC2 Auto Scaling groups, you can also specify your prioritization preferences across reservation types, and configure automatic fall back to EC2 On-Demand capacity when there is no capacity remaining across your reservations. 
There are no additional charges for using this feature. This feature is available in all AWS Regions where Capacity Blocks for ML and interruptible ODCRs are supported, excluding AWS GovCloud (US) and China Regions.&nbsp;To get started, see Capacity Reservation Resource Groups and the Capacity Reservations user guide.

## 핵심 요약

요약 미지원
