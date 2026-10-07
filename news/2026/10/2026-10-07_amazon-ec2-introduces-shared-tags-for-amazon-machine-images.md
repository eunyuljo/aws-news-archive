---
title: "Amazon EC2 introduces shared tags for Amazon Machine Images"
date: "2026-10-07"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/ec2-ami-shared-tags"
tags: ["EC2", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon EC2 introduces shared tags for Amazon Machine Images

**날짜:** 2026년 10월 07일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/ec2-ami-shared-tags

## 내용

Amazon EC2 now supports AMI tag sharing, a new feature that lets AMI owners make selected tags visible to all AWS accounts an AMI is shared with. Whether an AMI is shared with an account, across an organization, or made public, a shared tag is automatically shared alongside the AMI, eliminating the need to build and maintain custom tag replication workflows.
AMI owners simply add the 'ec2:SharedTag/' prefix to any tag key, and every account the AMI is shared with can immediately see it. This removes the operational burden of replicating tags into each account after sharing an AMI. Shared tags are read-only for recipient accounts, so only the owner can create, modify, or delete them. They count only against the owner's 50 tag per resource quota, allowing recipient accounts to continue adding their own private tags without any impact to their limits.
This feature is available in all AWS Regions at no additional cost. To learn more, please visit the documentation&nbsp;and read the blog.

## 핵심 요약

요약 미지원
