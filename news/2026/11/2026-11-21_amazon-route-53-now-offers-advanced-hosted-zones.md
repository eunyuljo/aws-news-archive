---
title: "Amazon Route 53 now offers Advanced Hosted Zones"
date: "2026-11-21"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-offers-advanced-hosted-zones/"
tags: ["RDS", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon Route 53 now offers Advanced Hosted Zones

**날짜:** 2026년 11월 21일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-offers-advanced-hosted-zones/

## 내용

Amazon Route 53 now offers Advanced Hosted Zones, a new hosted zone tier with additional guardrails, visibility, and resilience features. Advanced Hosted Zones include Change Guardrails that prevent accidental record deletions, record-level Change History, and public DNS fallback in private hosted zones.
A single mistaken DNS change can take part of your domain offline, such as deleting a record that is still serving traffic or removing a delegation that resolvers are still using. To protect against this, customers build their own validation pipelines, review processes, and audit tooling. With Change Guardrails turned on, Route 53 checks each change before applying it. It blocks deleting a record that is still receiving DNS queries, a record that an alias record in the same hosted zone points to, or a delegation that is still in use. When a guardrail blocks a change, Route 53 rejects the whole request with an error that explains why, and no records change. Guardrails apply to every change, including changes from infrastructure as code tools. Change History gives you a record-level history of changes to your hosted zone, retained for 365 days, so you can see what changed and when.
To get started, create a new Advanced Hosted Zone or upgrade an existing hosted zone, then turn on the guardrails you want. You can use the Route 53 console, API, AWS CLI, AWS SDKs, or AWS CloudFormation. Advanced Hosted Zones are priced separately from Standard Hosted Zones. For rates, see the Route 53 pricing page.
Advanced Hosted Zones are available in all AWS commercial Regions where Route 53 public and private hosted zones are available. To learn more, see Advanced Hosted Zones in the Route 53 Developer Guide.

## 핵심 요약

요약 미지원
