---
title: "Amazon Bedrock AgentCore Identity now supports OAuth 2.0 discovery URLs"
date: "2026-11-14"
service: "Bedrock"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/bedrock-agentcore-oauth2-discovery/"
tags: ["Bedrock", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon Bedrock AgentCore Identity now supports OAuth 2.0 discovery URLs

**날짜:** 2026년 11월 14일
**서비스:** Bedrock
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/bedrock-agentcore-oauth2-discovery/

## 내용

Amazon Bedrock AgentCore Identity now supports OAuth 2.0 authorization server discovery URLs for both inbound JWT authorization and outbound OAuth credential providers. This update enables developers to configure AgentCore with OAuth 2.0 authorization servers that do not use OpenID Connect (OIDC). 
Previously, AgentCore Identity accepted only OIDC discovery URLs. Authorization servers that implement OAuth 2.0 without OIDC publish their metadata at a different well-known path and could not be used with AgentCore. With this launch, you can use either OIDC or OAuth 2.0 authorization server discovery URLs when you configure a JWT authorizer or a custom OAuth credential provider on AgentCore. 
This feature is available in all AWS Regions where Amazon Bedrock AgentCore is available, at no additional cost. To learn more, see Configure inbound JWT authorizer and Add OAuth client using custom provider in the Amazon Bedrock AgentCore Developer Guide.

## 핵심 요약

요약 미지원
