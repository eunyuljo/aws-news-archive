---
title: "Amazon Bedrock AgentCore Identity adds private certificate authority support"
date: "2026-11-20"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/bedrock-agentcore-identity-private-ca/"
tags: ["S3", "2026", "new-region"]
nav_exclude: true
---

# Amazon Bedrock AgentCore Identity adds private certificate authority support

**날짜:** 2026년 11월 20일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/bedrock-agentcore-identity-private-ca/

## 내용

Amazon Bedrock AgentCore Identity now supports private certificate authorities (CAs) for custom OAuth 2.0 credential providers. If you already connect your agents to identity providers (IdPs) hosted in your VPC, you can now configure those connections to trust certificates issued by your own CA — including AWS Private CA, enterprise CAs, and self-signed root CAs.
AgentCore Identity has supported private IdP connectivity through Amazon VPC Lattice, but until now the IdP still had to present a publicly trusted TLS certificate over that private connection. With private CA support, you store your CA certificate in AWS Secrets Manager or Amazon S3 and reference it from your credential provider configuration. AgentCore Identity uses it to verify the IdP's server certificate directly, removing the need for a publicly trusted certificate or additional infrastructure on the private network path.
You can rotate the CA certificate without downtime by combining the current and new certificates in a single PEM file, and remove private CA trust by updating the credential provider without the certificate reference.
Private CA support for AgentCore Identity is available in all AWS Regions where AgentCore Identity supports private IdP connectivity. To get started, see Connect to private identity providers in the Amazon Bedrock AgentCore Developer Guide. To learn more, visit the Amazon Bedrock AgentCore product page.

## 핵심 요약

요약 미지원
