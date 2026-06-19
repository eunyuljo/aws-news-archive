---
title: "Amazon GameLift Servers adds new container fleet improvements"
date: "2026-06-19"
service: "CloudFormation"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-gamelift-servers-container-fleet-improvements"
tags: ["CloudFormation", "2026", "new-region"]
nav_exclude: true
---

# Amazon GameLift Servers adds new container fleet improvements

**날짜:** 2026년 06월 19일
**서비스:** CloudFormation
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-gamelift-servers-container-fleet-improvements

## 내용

Amazon GameLift Servers now supports two significant container fleet improvements that enhance flexibility and inter-container communication for game server deployments. These new capabilities address common challenges faced by game developers using containerized architectures, providing greater control over container permissions and enabling seamless discovery of co-located containers on the same instance. 
You can now customize Linux capabilities for containers in your container group definitions, giving you finer control beyond Docker's default capability set. This is particularly valuable for game servers requiring specialized capabilities such as NET_RAW for custom networking protocols or SYS_PTRACE for attaching debuggers and profiling tools. Additionally, game servers can now call the new ListContainersNetworkInfo() server SDK action to retrieve comprehensive network information, including container name, ID, local IP address, and container group type for all containers running on the same instance. This enables automatic service discovery and simplified communication between game servers and auxiliary services like metrics collectors, logging agents, or caching systems. 
These improvements are available through the Amazon GameLift Servers console, AWS CLI, AWS SDK, and AWS CloudFormation. The ListContainersNetworkInfo() action is supported in server SDK 5.x for Go, C++, and C#, as well as in plugins for Unreal Engine and Unity. Both features are available in all AWS regions where Amazon GameLift Servers is supported, except China. To learn more, visit the Amazon GameLift Servers documentation.

## 핵심 요약

요약 미지원
