---
title: "AWS Security Hub now infers resource criticality from installed software and usage"
date: "2026-11-18"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/security-hub-resource-criticality/"
tags: ["EC2", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# AWS Security Hub now infers resource criticality from installed software and usage

**날짜:** 2026년 11월 18일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/security-hub-resource-criticality/

## 내용

Today, AWS Security Hub adds installed software and resource usage as signals for resource criticality, which indicates how important a resource is to your business. Security Hub uses criticality to rank exposure findings, so that central security teams can prioritize the exposures that affect their most important resources. 
Security Hub already infers criticality from resource tags and names, but inconsistently tagged resources often have an Unknown criticality, which makes their exposures harder to prioritize. With installed software and resource usage as additional signals, more of your resources receive a meaningful criticality with no tagging or configuration required. For example, an EC2 instance that runs a database engine and serves steady traffic receives a higher criticality than an instance that runs only monitoring agents and sits idle. 
These signals are included with the Security Hub Essentials plan at no additional cost and require no new enablement. To learn more, see Resources in Security Hub in the AWS Security Hub User Guide and the AWS Security Hub product page. For a list of AWS Regions where Security Hub is available, see the AWS Region table.

## 핵심 요약

요약 미지원
