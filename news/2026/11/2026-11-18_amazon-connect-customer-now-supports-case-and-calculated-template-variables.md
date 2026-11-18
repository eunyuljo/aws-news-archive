---
title: "Amazon Connect Customer now supports case and calculated template variables"
date: "2026-11-18"
service: "Connect"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/connect-case-and-calculated-attributes/"
tags: ["Connect", "2026", "new-region"]
nav_exclude: true
---

# Amazon Connect Customer now supports case and calculated template variables

**날짜:** 2026년 11월 18일
**서비스:** Connect
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/connect-case-and-calculated-attributes/

## 내용

Amazon Connect Customer message templates, which personalize each message with details about its recipient, now support case fields from Cases and calculated attributes from Customer Profiles, such as a customer's most frequent contact channel. Companies that send updates about a claim, an order, or an application need each message to reflect that customer's record. Template authors can insert case fields, including custom fields that administrators define, and Connect Customer fills in the current value for each recipient every time it sends a message that uses the template.
A claims manager at an insurance company can build one email template that pulls each claim's reference number and status from its case, so every policyholder receives an update about their own claim. A retailer can add a custom calculated attribute, such as each customer's total orders in the past year, to a loyalty email so every customer sees their own count. Developers can pass these values when they render a template with the RenderMessageTemplate API.
You can use case and calculated attributes in message templates in the following AWS Regions: US East (N. Virginia), US West (Oregon), Africa (Cape Town), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), and Europe (London).
To learn more, see Add personalized content to message templates in the Amazon Connect Customer Administrator Guide.

## 핵심 요약

요약 미지원
