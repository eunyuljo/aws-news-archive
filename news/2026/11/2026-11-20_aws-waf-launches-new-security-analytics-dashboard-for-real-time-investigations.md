---
title: "AWS WAF launches new Security Analytics Dashboard for real-time investigations"
date: "2026-11-20"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/02/aws-waf-security-analytics-dashboard/"
tags: ["S3", "2026", "GA", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# AWS WAF launches new Security Analytics Dashboard for real-time investigations

**날짜:** 2026년 11월 20일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/02/aws-waf-security-analytics-dashboard/

## 내용

AWS WAF now gives you one place to find and stop unwanted traffic across every application in your account. The new AWS WAF security analytics dashboard brings together traffic from all of your protection packs (web ACLs), whether they protect Regional resources or Amazon CloudFront distributions, into a single view. The dashboard also lets you search request logs right in the console, with no logging pipeline to build, and includes 21 days of full-fidelity request data at no additional cost. It is available alongside the existing dashboard for each protection pack (WebACL), which continues to work as it does today. 
Until now, spotting a trend across your applications, such as a bot campaign hitting several endpoints or a spike in blocked requests, meant opening each web ACL in turn or individually querying AWS WAF logs. With the AWS WAF security analytics dashboard, you can analyze traffic data from every protection pack (WebACL) at once. You can filter and group traffic by dimensions such as client IP address, country, ASN, user agent, JA4 fingerprint, host, path, rule triggered, and labels. You can see which endpoints are affected and how traffic is changing across all of them. The data is full-fidelity rather than sampled, and filters apply across the whole dashboard. 
Investigating individual requests has also required delivering AWS WAF logs to Amazon CloudWatch Logs, Amazon S3, or Amazon Data Firehose and writing queries. AWS WAF Security analytics dashboard includes a logs widget that lets you search and explore raw request logs in the console, down to the full HTTP request, with no log delivery to configure. When you find unwanted traffic, you can block an IP address or a country directly from the page. You can also filter by the labels that managed rules attach to requests to see what a rule in Count mode would block before you enforce it. 
The AWS WAF security analytics dashboard is available at no additional cost in all commercial AWS Regions where AWS WAF is available. This feature is not available in the AWS GovCloud (US) Regions and China Regions. To get started, open the AWS WAF console and choose Security analytics in the navigation pane.&nbsp;To learn more, see the AWS WAF Developer Guide&nbsp;and launch blog post.

## 핵심 요약

요약 미지원
