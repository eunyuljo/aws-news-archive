---
title: "AWS Gateway Load Balancer now supports TCP Reset for faster failure recovery"
date: "2026-09-04"
service: "Connect"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-gateway-load-balancer-tcp-reset/"
tags: ["Connect", "2026", "new-region", "performance"]
nav_exclude: true
---

# AWS Gateway Load Balancer now supports TCP Reset for faster failure recovery

**날짜:** 2026년 09월 04일
**서비스:** Connect
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-gateway-load-balancer-tcp-reset/

## 내용

AWS Gateway Load Balancer (GWLB) now supports sending TCP Reset (RST) packets when a target becomes unhealthy, is deregistered, or when a flow's idle timeout expires. This feature helps reduce traffic interruptions from minutes to seconds by enabling TCP endpoints to quickly detect failed connections and establish new TCP flows through healthy targets.  Previously, when a GWLB target failed, existing TCP connections would continue to be forwarded to the unhealthy target (aka fail-open behavior). Client and server applications could experience interruptions lasting several minutes due to TCP retry and exponential back-off mechanisms built in the TCP stacks of clients or servers. When this capability is enabled, GWLB sends TCP Resets in response to the incoming traffic, indicating to the sender that a TCP connection is no longer viable. This allows TCP endpoints to recover in quickly.  TCP Reset is not enabled by default to ensure backward compatibility. You can enable it per target group using the AWS Management Console, AWS CLI, or API. Three triggers are supported independently for generating TCP Reset: target becomes unhealthy, target deregistration (after connection draining), and TCP idle timeout expiry.  This feature is available for all new and existing Gateway Load Balancers in all AWS Regions where GWLB is available. There is no additional charge for using this feature.  To learn more, visit this AWS blog, and GWLB User Guide here and here.&nbsp;

## 핵심 요약

요약 미지원
