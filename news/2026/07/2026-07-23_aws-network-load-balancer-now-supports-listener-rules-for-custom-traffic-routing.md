---
title: "AWS Network Load Balancer now supports Listener Rules for custom traffic routing"
date: "2026-07-23"
service: "Connect"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-network-load-balancer-supports-listener-rules/"
tags: ["Connect", "2026", "new-region"]
nav_exclude: true
---

# AWS Network Load Balancer now supports Listener Rules for custom traffic routing

**날짜:** 2026년 07월 23일
**서비스:** Connect
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-network-load-balancer-supports-listener-rules/

## 내용

Network Load Balancer (NLB) now supports listener rules allowing you to route connections to different target groups based on the source IP address type. With listener rules, a single dual-stack NLB sends IPv6 client traffic to IPv6 targets and IPv4 client traffic to IPv4 targets, preserving the original client IP address end to end for both address families.  Previously, serving both IPv4 and IPv6 clients from one NLB meant accepting a tradeoff: either run two separate load balancers (one per IP version) and split clients with DNS, or send all traffic to one target group and lose the original client IP through protocol translation. Listener rules remove that tradeoff by enabling conditional routing at Layer 3, directing each connection to a same-family target group with no translation and no additional infrastructure.  You can add listener rules to existing dual-stack NLBs without recreating them. Rules are supported on TCP, UDP, TCP_UDP, and TLS listeners and work alongside existing NLB features including connection draining, target group stickiness, cross-zone load balancing, weighted target groups, and client IP preservation.  Listener rules for Network Load Balancer are available in all AWS commercial Regions and the AWS GovCloud (US) Regions at no additional charge. Standard NLB pricing for load balancer hours and LCUs applies. To get started, see this AWS blog, and the Network Load Balancer User Guide.

## 핵심 요약

요약 미지원
