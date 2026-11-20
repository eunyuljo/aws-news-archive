---
title: "AWS Continuum for Penetration Testing now supports pause and resume"
date: "2026-11-20"
service: "VPC"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/continuum-pentest-pause-resume/"
tags: ["VPC", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Continuum for Penetration Testing now supports pause and resume

**날짜:** 2026년 11월 20일
**서비스:** VPC
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/continuum-pentest-pause-resume/

## 내용

AWS Continuum for Penetration Testing (formerly AWS Security Agent) now lets you pause a running penetration test job and resume it later from its last saved checkpoint. Continuum for Penetration Testing runs on-demand, AI-driven penetration tests against your web applications and APIs. Previously, a pen test job that failed due to client configuration error could not continue, so security teams had to start a new pen test job and repeat work the agent had already done.
When you resume a paused or failed pen test job, it keeps its findings and completed work and continues where it left off. You can pause a pen test job during a deployment or maintenance window, raise the task-hour limit of a pen test job that has reached it, or replace test credentials that expired mid-test. Before you resume, you can also update the network traffic settings or VPC configuration, while the pen test job's scope, including its target endpoints, stays the same.
You can pause and resume pen test jobs in the web application or with the StopPentestJob and ResumePentestJob APIs. You can resume a pen test job within 7 days of its creation. Pause and resume is available in all AWS Regions where AWS Continuum for Penetration Testing is available. To learn more, visit our documentation page.

## 핵심 요약

요약 미지원
