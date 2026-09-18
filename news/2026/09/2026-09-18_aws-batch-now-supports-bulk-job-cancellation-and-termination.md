---
title: "AWS Batch now supports bulk job cancellation and termination"
date: "2026-09-18"
service: "Lex"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-batch-bulk-cancellation/"
tags: ["Lex", "2026", "new-region"]
nav_exclude: true
---

# AWS Batch now supports bulk job cancellation and termination

**날짜:** 2026년 09월 18일
**서비스:** Lex
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-batch-bulk-cancellation/

## 내용

AWS Batch now supports bulk job cancellation and termination, enabling you to cancel or terminate up to 50 jobs with a single API call. The new CancelJobs, TerminateJobs, and TerminateServiceJobs APIs reduce the operational complexity of managing large-scale batch workloads, letting you act on groups of jobs at once and receive per-job results in a single response. Additionally, ListJobs now returns isCancelled and isTerminated fields, and ListServiceJobs returns isTerminated, making it easier to track the lifecycle state of your jobs. 
To get started, call CancelJobs for jobs in SUBMITTED, PENDING, or RUNNABLE states, or TerminateJobs and TerminateServiceJobs for jobs in any state, including STARTING and RUNNING. All three APIs accept up to 50 job IDs and work with individual and array jobs. You can access them through the AWS CLI or AWS SDKs. 
Bulk job cancellation and termination is available in all AWS Regions where AWS Batch is available. For more information, see CancelJobs,&nbsp;TerminateJobs, and TerminateServiceJobs pages in the AWS Batch API Reference Guide.

## 핵심 요약

요약 미지원
