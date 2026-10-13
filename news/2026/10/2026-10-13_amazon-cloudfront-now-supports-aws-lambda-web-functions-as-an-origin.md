---
title: "Amazon CloudFront now supports AWS Lambda Web Functions as an origin"
date: "2026-10-13"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/cloudfront-lambda-web-functions-origin/"
tags: ["Lambda", "2026", "new-region", "performance", "security"]
nav_exclude: true
---

# Amazon CloudFront now supports AWS Lambda Web Functions as an origin

**날짜:** 2026년 10월 13일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/cloudfront-lambda-web-functions-origin/

## 내용

Starting today, you can deliver web applications built on AWS Lambda Web Functions through CloudFront's global edge network. &nbsp;
With CloudFront in front of a Lambda Web Function, you get TLS termination at the edge for lower latency and faster connections, caching for better performance, and custom domains with managed TLS certificates. No changes to application code are needed. CloudFront Origin Access Control (OAC) restricts your Lambda Web Function so it's reachable only through CloudFront, so unintended requests that bypass your security protections do not reach your origin. With OAC in place, CloudFront's edge network protects your Lambda Web Function from network-layer DDoS attacks, and you can attach AWS WAF for additional application-layer security. For applications that authenticate their own users, OAC ensures that original credentials reach the application unchanged, so existing sign-in flows keep working.
CloudFront support for AWS Lambda Web Functions is available worldwide, except in the CloudFront China region. To get started, use the CloudFront Console, SDK, CLI, or CloudFormation to configure your Lambda Web Function as a CloudFront origin. For more information, refer to the CloudFront Developer Guide. There are no additional fees associated with this feature.

## 핵심 요약

요약 미지원
