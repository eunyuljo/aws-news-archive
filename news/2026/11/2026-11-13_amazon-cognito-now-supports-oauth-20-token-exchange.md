---
title: "Amazon Cognito now supports OAuth 2.0 token exchange"
date: "2026-11-13"
service: "Cognito"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/cognito-token-exchange/"
tags: ["Cognito", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon Cognito now supports OAuth 2.0 token exchange

**날짜:** 2026년 11월 13일
**서비스:** Cognito
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/cognito-token-exchange/

## 내용

Amazon Cognito now supports OAuth 2.0 token exchange (RFC 8693). Amazon Cognito helps you add sign-up, sign-in, and access control to your web applications, mobile applications, and AI agents. With token exchange, a service or AI agent acting on a user's behalf can exchange the user's token for a new token scoped to a specific downstream service. Previously, a service that called another service on a user's behalf had to forward the user's original token or build and maintain its own token minting logic. 
With token exchange, you can issue a new token that has a narrower scope than the original token, is bound to a single audience, and comes without a refresh token. When you include an actor token, Cognito adds an act claim that identifies the intermediary, so downstream services can tell a request that an agent made on a user's behalf from one the user made directly. For example, a Model Context Protocol (MCP) server can exchange a user's token for a narrowly scoped token to call a backend API, with the act&nbsp;claim recording the MCP server as the actor. 
You can exchange tokens through the token endpoint or with the new GetDerivedToken API. Token exchange is available on the Essentials and Plus feature plans in all AWS Regions where Amazon Cognito is available. To learn more, see exchanging tokens for downstream services in the Amazon Cognito Developer Guide.

## 핵심 요약

요약 미지원
