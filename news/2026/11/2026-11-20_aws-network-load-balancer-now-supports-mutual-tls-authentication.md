---
title: "AWS Network Load Balancer now supports mutual TLS authentication"
date: "2026-11-20"
service: "IoT"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/network-load-balancer-mtls/"
tags: ["IoT", "2026", "GA", "new-region"]
nav_exclude: true
---

# AWS Network Load Balancer now supports mutual TLS authentication

**날짜:** 2026년 11월 20일
**서비스:** IoT
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/network-load-balancer-mtls/

## 내용

AWS Network Load Balancer (NLB) now supports mutual TLS (mTLS) authentication for clients that present X.509 certificates. Until now, customers who needed mTLS with NLB built their own solutions or ran third-party proxies to authenticate clients. With this launch, NLB verifies client certificates on its TLS listeners, so only trusted clients can reach your targets. You can offload the compute-intensive processing required for mTLS authentication to NLB, without adding certificate logic to your backend applications. 
Mutual TLS is commonly used to secure communication between IoT devices, APIs, and microservices, and in regulated environments where both sides must prove their identity. To use mTLS, create a trust store with a certificate authority (CA) certificate bundle from a CA of your choice or AWS Private Certificate Authority, and attach it to a new or existing NLB TLS listener. To block certificates you no longer trust, add one or more certificate revocation lists (CRLs) to the trust store. To admit only specific clients, add client certificate filters that match the Common Name, Organizational Unit, or the DNS name or URI in the Subject Alternative Name, such as a SPIFFE ID. You can set up mTLS with the AWS Management Console, AWS Command Line Interface (AWS CLI), or APIs. 
Mutual TLS for NLB is available in all AWS commercial and AWS GovCloud (US) Regions where NLB is available. To learn more, visit the AWS Blog and the NLB User Guide.

## 핵심 요약

요약 미지원
