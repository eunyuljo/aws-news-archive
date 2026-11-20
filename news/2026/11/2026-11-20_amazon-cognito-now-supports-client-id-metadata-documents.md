---
title: "Amazon Cognito now supports client ID metadata documents"
date: "2026-11-20"
service: "Cognito"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/cognito-client-id-metadata-documents/"
tags: ["Cognito", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon Cognito now supports client ID metadata documents

**날짜:** 2026년 11월 20일
**서비스:** Cognito
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/cognito-client-id-metadata-documents/

## 내용

Amazon Cognito now supports OAuth client ID metadata documents (CIMD). Amazon Cognito helps you implement secure sign-in and access control for users, AI agents, and microservices in minutes. With CIMD, Model Context Protocol (MCP) clients and AI agents can sign users in to your user pool without registering a separate app client. Previously, each external client needed its own app client, either created in advance or through dynamic client registration, and you had to manage and clean up those clients over time.
With CIMD, a client uses an HTTPS URL as its client ID and publishes a JSON metadata document at that URL. When the client starts sign-in, Cognito fetches and validates the document and uses it to identify the client and validate its sign-in request. You decide which clients to accept with CIMD policies that map URL patterns to one of your app clients, and Cognito grants only the scopes and grant types that both the app client and the metadata document allow. For example, a company that runs an MCP server can accept an AI assistant by allowing the URL where that assistant publishes its metadata without creating or maintaining an app client for it.
CIMD is available on the Essentials and Plus feature plans in all AWS Regions where Amazon Cognito is available. To learn more, see Client ID metadata documents (CIMD) in the Amazon Cognito Developer Guide.

## 핵심 요약

요약 미지원
