---
title: "Amazon API Gateway REST APIs now support JWT authorizers"
date: "2026-11-18"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-api-gateway-rest-authorizers-jwt/"
tags: ["Lambda", "2026", "new-region"]
nav_exclude: true
---

# Amazon API Gateway REST APIs now support JWT authorizers

**날짜:** 2026년 11월 18일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-api-gateway-rest-authorizers-jwt/

## 내용

Amazon API Gateway now offers a native JWT authorizer for REST APIs, a new authorizer type that validates JSON Web Tokens directly in the gateway. Until now, validating tokens from an OpenID Connect or OAuth 2.0 identity provider other than Amazon Cognito required a Lambda authorizer. You now configure token validation instead of writing and operating code for it. 
You can define one or more issuers, the audiences accepted for each, the signing algorithms you permit, and any additional claims a token may present. API Gateway verifies each token's signature, issuer, audience, expiry, and claims on every request. You can attach one authorizer to many methods and require different scopes on each. This fits machine-to-machine APIs, mobile and web backends, and multi-tenant APIs that accept tokens from several identity providers. 
The JWT authorizer works on Regional, edge-optimized, and private REST APIs, and is available in all commercial AWS Regions and the AWS GovCloud (US) Regions. To get started, see Amazon API Gateway documentation and AWS blog post.&nbsp;

## 핵심 요약

요약 미지원
