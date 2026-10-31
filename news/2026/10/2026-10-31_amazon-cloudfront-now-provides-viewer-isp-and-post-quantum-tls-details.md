---
title: "Amazon CloudFront now provides viewer ISP and post-quantum TLS details"
date: "2026-10-31"
service: "CloudFront"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/cloudfront-viewer-isp-post-quantum-visbility/"
tags: ["CloudFront", "2026", "performance"]
nav_exclude: true
---

# Amazon CloudFront now provides viewer ISP and post-quantum TLS details

**날짜:** 2026년 10월 31일
**서비스:** CloudFront
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/cloudfront-viewer-isp-post-quantum-visbility/

## 내용

Amazon CloudFront can now forward two new optional headers to your origin. The CloudFront-Viewer-ISP header contains the name of the viewer's internet service provider (ISP), so you can see which network a request came from. The CloudFront-Viewer-TLS-Details header describes the cryptography used on each viewer's TLS connection, so you can see whether a connection used post-quantum cryptography (PQC). 
With CloudFront-Viewer-ISP, you can break down traffic and performance by network. You can also isolate unusual traffic from a single provider. CloudFront-Viewer-TLS-Details includes the key exchange, signature scheme, and signature public key type for each connection. You can use it to measure the share of viewers that actually connect with PQC and identify clients that do not yet do so. To forward either header to your origin, add it to an origin request policy and attach the policy to your distribution. 
To get started, see adding CloudFront headers and&nbsp;controlling origin requests with a policy in the Amazon CloudFront Developer Guide

## 핵심 요약

요약 미지원
