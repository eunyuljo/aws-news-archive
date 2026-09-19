---
title: "Amazon SES now supports tenant-level deliverability insights"
date: "2026-09-19"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ses-vdm-tenants/"
tags: ["Config", "2026", "new-region"]
nav_exclude: true
---

# Amazon SES now supports tenant-level deliverability insights

**날짜:** 2026년 09월 19일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ses-vdm-tenants/

## 내용

Amazon Simple Email Service (SES) now supports tenant-level deliverability insights in Virtual Deliverability Manager (VDM). Tenant management allows email senders to isolate email sending across customers, business units, or applications. Previously, VDM provided deliverability metrics at the account, ISP, sending identity, and configuration set levels. Now, customers who use tenants and have enabled VDM can also monitor the deliverability of each tenant. 
The VDM dashboard adds a Tenants view with per-tenant metrics (send volume, deliveries, bounces, complaints, opens, and clicks) and a detail page that breaks those metrics down by mailbox provider and by associated identities and configuration sets. Customers can also search and export a tenant's sent messages, or query tenant metrics programmatically using the BatchGetMetricData API operation's new TENANT_NAME dimension. This helps senders identify the tenant causing a deliverability issue and correct it without impact to their other tenants. 
Virtual Deliverability Manager is available in all AWS Regions where Amazon SES is available. 
To learn more, visit the Amazon SES console or refer to the Virtual Deliverability Manager dashboard documentation in the Amazon SES Developer Guide.

## 핵심 요약

요약 미지원
