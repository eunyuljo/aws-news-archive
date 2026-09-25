---
title: "AWS Billing and Cost Management now provides billing context for your account through a new API"
date: "2026-09-25"
service: "General"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-billing-and-cost-management-billing-context-api/"
tags: ["General", "2026", "price-reduction", "new-region", "ai-ml"]
nav_exclude: true
---

# AWS Billing and Cost Management now provides billing context for your account through a new API

**날짜:** 2026년 09월 25일
**서비스:** General
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-billing-and-cost-management-billing-context-api/

## 내용

AWS Billing and Cost Management now offers the ListBillingViewSegments API, which returns the billing context of your account over a time period you specify.
You can use the API to retrieve information about how your accounts are positioned in the billing hierarchy, such as management accounts, member accounts, or billing group primary accounts. You can also identify which accounts managed your billing relationship and the rate settings, either billable or pro forma, applied to your cost data. The API returns billing context only, not cost and usage data. You can call the API directly or through an AI agent.
Your billing context can change mid-period. The API therefore divides the requested period into time segments, each with its effective date range. For example, an account starts as its own payer, then moves under another organization as a member account, and in a later month has its new payer manage its billing through AWS Billing Conductor. A request covering all three periods returns three segments, each identifying the accounts and billing settings that were in effect.
ListBillingViewSegments is available in all commercial AWS Regions at no additional charge and supports primary billing views. To get started, visit the AWS Billing API Reference.

## 핵심 요약

요약 미지원
