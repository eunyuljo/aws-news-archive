---
title: "Quick now supports smart approvals for agentic actions"
date: "2026-10-29"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/quick-smart-approvals-agentic-actions/"
tags: ["RDS", "2026", "new-region"]
nav_exclude: true
---

# Quick now supports smart approvals for agentic actions

**날짜:** 2026년 10월 29일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/quick-smart-approvals-agentic-actions/

## 내용

Amazon Quick now supports smart approvals, a review layer that reduces unnecessary approval prompts while preserving human oversight of the actions that matter most. As agents take more actions on a user's behalf, such as sending email, updating records, and creating tickets, asking a person to approve every step leads to approval fatigue and weaker oversight over time. With smart approvals, a separate review model called the classifier evaluates each eligible action against the user's request. It approves routine actions automatically and refers consequential actions to the user for review. 
Your existing policies always come first. Smart approvals only reviews actions where the user's setting is "ask" each time. Denied actions stay denied, and smart approvals never grants new access. The classifier sends higher-impact actions to the user for review. These include sending content outside the organization, changing permissions, deleting content, making payments, and actions that go beyond what the user asked for. Each automatic approval covers only the exact action that was reviewed. If a review fails or times out, the action goes to the user. 
Smart approvals is on for all users by default. Administrators control who can use it with custom permissions, and users can turn it off for their conversations and scheduled runs in chat options. AWS CloudTrail records each action review made through smart approvals and each change to a user's smart approvals setting. 
Smart approvals is available in Amazon Quick in all AWS Regions where Amazon Quick agentic capabilities are supported. For more information, see the AWS Region table. 
To learn more about smart approvals, see smart approvals in the Amazon Quick User Guide. For more information about Amazon Quick, see the Amazon Quick product page.

## 핵심 요약

요약 미지원
