---
title: "Amazon CloudFront Functions now supports network calls"
date: "2026-11-19"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/cloudfront-functions-network-calls/"
tags: ["Lambda", "2026", "price-reduction", "security", "ai-ml"]
nav_exclude: true
---

# Amazon CloudFront Functions now supports network calls

**날짜:** 2026년 11월 19일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/cloudfront-functions-network-calls/

## 내용

Amazon CloudFront Functions can now make network calls and act on the response during a request. CloudFront Functions runs lightweight JavaScript at CloudFront edge locations to customize requests and responses. Previously, if your logic depended on data from another service, you had to use Lambda@Edge or move that logic to your origin. Now your functions can use real-time data to personalize, authenticate, or route requests at the edge, close to your viewers. 
With the new cf.fetch() method, your functions can call your API endpoints and use the response to decide how to handle each request. For example, you can check an AI agent's permissions and usage budget so that only authorized requests reach your API or MCP server, or send request signals to a security or fraud detection service to block or challenge bad traffic. With cf.beacon(), you can send analytics events in the background without slowing down viewers, even for content served from cache. Both methods take advantage of the origin settings already on your distribution, including origin access control (OAC), VPC origins, and connection reuse. 
Network calls are available at all CloudFront edge locations. They cost $0.10 per million calls, on top of CloudFront Functions invocation charges, and are included at no additional cost in the Pro plan and above in CloudFront flat-rate plans. To learn more, see Helper methods for network calls in the Amazon CloudFront Developer Guide and Amazon CloudFront pricing.

## 핵심 요약

요약 미지원
