---
title: "Amazon EC2 enables AMI creation with local snapshots from instances on Outposts"
date: "2026-08-21"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/ec2-create-image-local-snapshot-outpost"
tags: ["EC2", "2026", "new-region"]
nav_exclude: true
---

# Amazon EC2 enables AMI creation with local snapshots from instances on Outposts

**날짜:** 2026년 08월 21일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/ec2-create-image-local-snapshot-outpost

## 내용

Amazon EC2 now supports creating Amazon Machine Images (AMIs) with local snapshots from instances running on AWS Outposts. This capability makes it easier for customers to create AMIs while storing snapshots directly on the Outpost to meet data residency requirements. 
Customers can now create AMIs with snapshots stored either on the Outpost itself or in the parent AWS Region. When keeping data local, EC2 automatically determines the target Outpost from the instance's location — no need to manually specify an Outpost ARN. This also enables customers to integrate AMI creation into their existing backup and lifecycle workflows for instances on Outposts while ensuring data residency requirements are met. 
This feature is available in all AWS Regions in which AWS Outposts supports local snapshot storage. To learn more, visit the documentation.

## 핵심 요약

요약 미지원
