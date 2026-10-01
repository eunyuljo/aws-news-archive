---
title: "Partner Revenue Measurement adds Multi-Partner support to Resource Tagging"
date: "2026-10-01"
service: "General"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/partner-revenue-measurement-multi-partner-resource-tagging"
tags: ["General", "2026", "new-region"]
nav_exclude: true
---

# Partner Revenue Measurement adds Multi-Partner support to Resource Tagging

**날짜:** 2026년 10월 01일
**서비스:** General
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/partner-revenue-measurement-multi-partner-resource-tagging

## 내용

Partner Revenue Measurement (PRM) provides measurement of AWS consumption driven by Partner solutions. Today, PRM adds multi-Partner support to Resource Tagging, so that multiple AWS Partners can receive revenue attribution for the same AWS resource. Previously, a resource carried only one Partner tag, aws-apn-id, so when multiple Partners contributed to the same workload, only one Partner received attribution.&nbsp;
With this update, each Partner tags the resources they contribute to using a new key in the format aws-apn-id-&lt;partner-central-aws-account-id&gt;. When more than one Partner tags the same resource, each tagged Partner receives revenue attribution. This benefits Partners that co-deliver solutions, such as a consulting Partner that deploys and operates a software Partner's product in an AWS account. The existing aws-apn-id key continues to work, and resources tagged with it require no additional changes. &nbsp;
Multi-Partner support in Resource Tagging is available today in all commercial AWS regions. Revenue attributed through the existing aws-apn-id key and the new key both appear under the “Resource Tagging” method in the Attributed Revenue Dashboard, with no changes to the dashboard.
To learn more, see the Partner Revenue Measurement product page and the Resource Tagging&nbsp;onboarding guide.

## 핵심 요약

요약 미지원
