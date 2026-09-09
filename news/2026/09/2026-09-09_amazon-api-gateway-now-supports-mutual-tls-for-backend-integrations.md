---
title: "Amazon API Gateway now supports mutual TLS for backend integrations"
date: "2026-09-09"
service: "CloudFormation"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-api-gateway-mutual-tls-backend/"
tags: ["CloudFormation", "2026", "new-region"]
nav_exclude: true
---

# Amazon API Gateway now supports mutual TLS for backend integrations

**날짜:** 2026년 09월 09일
**서비스:** CloudFormation
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-api-gateway-mutual-tls-backend/

## 내용

You can now configure Amazon API Gateway REST APIs to present an AWS Certificate Manager (ACM) certificate to your backend during the TLS handshake, enabling mutual TLS (mTLS). Previously, API Gateway could present only a self-signed certificate that it generated; now you can use a certificate signed by a certificate authority you trust. Your integration endpoint validates this certificate during the handshake to confirm the connection comes from your API.&nbsp; 
You can import a certificate into ACM from your existing public key infrastructure (PKI), or have ACM issue and manage one for you through AWS Private Certificate Authority. When a certificate is reimported or renewed in ACM, API Gateway propagates the update automatically, with no redeployment and no downtime. Combined with the existing inbound mTLS support for client connections, you can apply mutual authentication across both the client-to-API and API-to-backend connections, which is a common requirement in financial services, healthcare, and other regulated or zero-trust environments. 
Mutual TLS for backend integrations is available in all commercial AWS Regions and the AWS GovCloud (US) Regions, where API Gateway REST APIs are available. You can configure it through the API Gateway console, AWS CLI, or AWS CloudFormation. To get started, see Amazon API Gateway documentation and AWS blog post.&nbsp;

## 핵심 요약

요약 미지원
