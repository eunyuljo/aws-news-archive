---
title: "AWS Security Agent (now part of AWS Continuum) now supports budget controls and finding revalidation"
date: "2026-08-21"
service: "General"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-security-agent/"
tags: ["General", "2026", "price-reduction", "security", "ai-ml"]
nav_exclude: true
---

# AWS Security Agent (now part of AWS Continuum) now supports budget controls and finding revalidation

**날짜:** 2026년 08월 21일
**서비스:** General
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-security-agent/

## 내용

AWS Security Agent (now part of AWS Continuum) has a on-demand penetration testing service that uses an AI agent to autonomously test web applications for vulnerabilities, billing based on cumulative task hours consumed across parallel testing tasks. Security teams and DevSecOps engineers previously had no built-in way to cap test costs or efficiently confirm that a remediated vulnerability had been resolved. These two new capabilities address these use cases.&nbsp; 
You can now set a maximum task-hours limit on any penetration test, choosing a preset value (for example, 20 or 30 hours), a custom value, or no limit at all. When the limit is reached, the test stops gracefully and preserves all findings discovered up to that point and because billing reflects only task hours actually used, a higher limit does not increase cost unless the test requires that additional time. You can also revalidate individual findings after deploying a fix, without re-running a full penetration test. Select one or more findings from a completed run and AWS Security Agent re-tests only those specific findings against your live application, returning a clear Active (still exploitable) or Resolved (fix confirmed) status with full revalidation history linked to the original finding. 
To learn more about revalidating findings, visit the AWS Security Agent Revalidation documentation. To learn more about setting a maximum task-hours limit, visit the AWS Security Agent Penetration Test documentation.

## 핵심 요약

요약 미지원
