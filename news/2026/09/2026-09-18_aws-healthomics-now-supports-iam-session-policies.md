---
title: "AWS HealthOmics now supports IAM session policies"
date: "2026-09-18"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/omics-iam-session-policy/"
tags: ["S3", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS HealthOmics now supports IAM session policies

**날짜:** 2026년 09월 18일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/omics-iam-session-policy/

## 내용

AWS HealthOmics now supports IAM session policies, enabling you to restrict permissions for individual runs without creating and managing multiple IAM roles. Until now, there was no way to dynamically scope down permissions for a single run, requiring you to create a separate IAM role for each tenant or run. AWS HealthOmics is a HIPAA-eligible service that helps healthcare and life sciences customers accelerate scientific breakthroughs with fully managed bioinformatics workflows. 
An IAM session policy is an inline policy that limits the maximum permissions of a run without modifying the underlying service role. Your effective permissions during a run are the intersection of permissions allowed by both the underlying identity-based policy and the temporary session policy. For example, if you operate a multi-tenant application, you can pass a session policy that limits a run's access to only that tenant's Amazon S3 buckets, without provisioning a dedicated IAM role for that tenant. You can also use IAM session policies to grant temporary access to specific Amazon S3 objects for a single run, and isolate access to sensitive resources on a per-run basis. 
IAM session policy support is available in all AWS Regions where AWS HealthOmics is available: US East (N. Virginia, Ohio), US West (Oregon), Europe (Frankfurt, Ireland, London), Israel (Tel Aviv), and Asia Pacific (Tokyo, Singapore, Seoul). To learn how to configure IAM session policies for your runs, visit the Permissions section of the &nbsp;AWS HealthOmics User Guide. To learn more about the service, visit &nbsp;AWS HealthOmics.

## 핵심 요약

요약 미지원
