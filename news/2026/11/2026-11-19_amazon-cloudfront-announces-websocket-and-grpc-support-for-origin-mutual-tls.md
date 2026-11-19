---
title: "Amazon CloudFront Announces WebSocket and gRPC Support for Origin Mutual TLS"
date: "2026-11-19"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudfront-origin-mtls-websockets-grpc/"
tags: ["RDS", "2026", "new-region"]
nav_exclude: true
---

# Amazon CloudFront Announces WebSocket and gRPC Support for Origin Mutual TLS

**날짜:** 2026년 11월 19일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudfront-origin-mtls-websockets-grpc/

## 내용

Amazon CloudFront (CF) now supports WebSocket and gRPC traffic to application origins in AWS regions, with mutual TLS authentication between CF and the application origin (origin mTLS). Customers can now use TLS certificates to authenticate requests from CloudFront while setting up WebSocket or gRPC connections to their origins. Origin mTLS protects internet facing applications that need persistent, bidirectional or streaming connections, such as chat platforms, collaborative editing tools or live dashboards from unauthenticated requests. 
Previously, customers serving WebSocket or gRPC traffic through CloudFront had to use shared secrets or IP allow-lists to identify requests originating from CloudFront. This was operationally complex and did not provide strong authentication. With Origin mTLS, customers can use one TLS based authentication for HTTP, WebSocket and gRPC traffic to an application origin. This works with application origins within AWS such as Application Load Balancer and API Gateway, on-premises origins, and origins hosted outside AWS. 
There is no additional charge for origin mTLS, and it is available with pay-as-you-go pricing and in the Business and Premium flat-rate pricing plans. To learn more, visit the CloudFront origin mutual TLS documentation.

## 핵심 요약

요약 미지원
