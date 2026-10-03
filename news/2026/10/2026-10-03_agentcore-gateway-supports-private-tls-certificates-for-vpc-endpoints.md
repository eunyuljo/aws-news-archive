---
title: "AgentCore Gateway supports private TLS certificates for VPC endpoints"
date: "2026-10-03"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/agentcore-gateway-private-tls-vpc/"
tags: ["S3", "2026", "new-region"]
nav_exclude: true
---

# AgentCore Gateway supports private TLS certificates for VPC endpoints

**날짜:** 2026년 10월 03일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/agentcore-gateway-private-tls-vpc/

## 내용

Amazon Bedrock AgentCore Gateway now supports TLS certificates signed by private certificate authorities (CAs) on MCP, OpenAPI, and HTTP proxy targets. This feature enables you to connect securely to gateway targets that use TLS certificates issued by your own private certificate authority. With this feature, you can establish native connections to private endpoints in your VPC without requiring an intermediate Application Load Balancer.
You can register a private CA certificate with gateway targets that use private endpoints powered by Amazon VPC Lattice. The gateway fetches your PEM-encoded CA certificate from Amazon S3 or AWS Secrets Manager and uses it as the trust anchor for outbound TLS connections. Private CA support is available for MCP server targets, OpenAPI targets, and HTTP proxy (passthrough) targets.
Support for private certificates on AgentCore Gateway is available in all Regions where both AgentCore Gateway and Amazon VPC Lattice are available. To learn more, see the AgentCore Developer Guide.

## 핵심 요약

요약 미지원
