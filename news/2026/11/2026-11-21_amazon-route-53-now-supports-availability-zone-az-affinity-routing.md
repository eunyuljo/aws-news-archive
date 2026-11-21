---
title: "Amazon Route 53 now supports Availability Zone (AZ) affinity routing"
date: "2026-11-21"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-affinity-routing/"
tags: ["RDS", "2026", "GA", "new-region", "performance"]
nav_exclude: true
---

# Amazon Route 53 now supports Availability Zone (AZ) affinity routing

**날짜:** 2026년 11월 21일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-affinity-routing/

## 내용

Amazon Route 53 now supports Availability Zone (AZ) affinity routing, which routes DNS queries from your VPCs to resources in the same AZ as the client that sends the query. This helps you keep traffic within the same AZ as the client, reducing latency and improving application performance. 
Until now, customers who wanted lower latency used other routing policies, such as latency-based or geoproximity routing. With this launch, DNS queries from your clients are answered with resources in the same AZ. This keeps traffic within the AZ and gives your clients faster responses. If there's no record for the client's AZ, Route 53 falls back to a record for a less specific location: the Zone Group, then the AWS Region, and then Global, in the same order. 
To get started, create AZ-affinity records and choose a location type for each: Availability Zone, Zone Group, Region, or Global. For Availability Zone records, specify the AZ ID, such as use1-az1. You can associate a health check with any AZ-affinity record, whether it's for an AZ, a Zone Group, or a Region. If the endpoint is unhealthy, Route 53 answers with the record for the next location. You can use AZ-affinity routing for records in both public and private hosted zones. The Global record answers queries that don't come from your VPCs, such as queries from the internet. You can create AZ-affinity records with the Route 53 console, API, AWS CLI, AWS SDKs, and AWS CloudFormation. 
AZ-affinity routing is available in all AWS commercial Regions where Route 53 public and private hosted zones are available. To learn more, see the AZ-affinity routing topic in the Route 53 Developer Guide. For pricing, see the Route 53 pricing page.

## 핵심 요약

요약 미지원
