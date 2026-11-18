---
title: "AWS Transform now supports migration to AWS Outposts"
date: "2026-11-18"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-transform-outposts-migration/"
tags: ["S3", "2026", "GA", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# AWS Transform now supports migration to AWS Outposts

**날짜:** 2026년 11월 18일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-transform-outposts-migration/

## 내용

AWS Transform now supports AWS Outposts as a migration target. You can migrate workloads onto your Outposts from on-premises environments, another Outpost, or a different Availability Zone or Region. AWS Transform is a collaborative enterprise IT transformation service powered by agentic AI that accelerates cloud migration, application modernization, and continuous tech debt reduction. Run your migration with AI agents in AWS Transform for migrations, or use AWS Transform MGN, the rehost engine within AWS Transform, directly from its console.
If you run workloads on Outposts for low latency, local data processing, or data residency, migrating them has meant manual effort or legacy tooling, often with a detour through the Region and an AMI copy. Now you choose subnets on the Outpost for your migration, and AWS Transform continuously replicates your source servers at the block level, directly from your source environment to the Outpost. You launch test instances before cutover and cut over with minimal downtime.
Migration to Outposts is available in all AWS Transform for migrations target Regions and AWS Transform MGN Regions and requires Amazon EBS on the Outpost. If your Outpost has Amazon S3 on Outposts, you can keep snapshots on the Outpost for data residency or store them in the parent Region. Without it, snapshots are stored in the parent Region.
To get started, see the AWS Transform documentation or visit the AWS Transform product page.

## 핵심 요약

요약 미지원
