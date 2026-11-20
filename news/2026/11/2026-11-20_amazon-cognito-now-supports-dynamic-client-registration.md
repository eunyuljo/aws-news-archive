---
title: "Amazon Cognito now supports dynamic client registration"
date: "2026-11-20"
service: "Cognito"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/cognito-dynamic-client-registration/"
tags: ["Cognito", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon Cognito now supports dynamic client registration

**날짜:** 2026년 11월 20일
**서비스:** Cognito
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/cognito-dynamic-client-registration/

## 내용

Amazon Cognito now supports OAuth dynamic client registration (DCR, RFC 7591). Amazon Cognito helps you implement secure sign-in and access control for users, AI agents, and microservices in minutes. With DCR support, Model Context Protocol (MCP) clients and AI agents can register themselves at runtime. Previously, you had to create an application client in advance for each AI client before it could connect to an MCP server that uses Cognito for authorization. 
With DCR, Cognito advertises a registration endpoint in its OAuth authorization server metadata. MCP clients that support dynamic client registration discover the endpoint, register to receive a client ID, and then sign users in. You control who can register: either require registration requests to present an access token with a registration scope, or turn on open registration so that any client can register. Dynamically registered clients appear with your other app clients with a client ID prefix and a client type you can filter on, so you can manage them with the same console and APIs. 
DCR is available on the Essentials and Plus feature plans in all AWS Regions where Amazon Cognito is available. To learn more, see Dynamic client registration in the Amazon Cognito Developer Guide.

## 핵심 요약

요약 미지원
