---
title: "Amazon GameLift Streams Now Offers Service-managed Shader Caching"
date: "2026-08-11"
service: "General"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/Amazon-GameLift-Streams-Shader-Caching/"
tags: ["General", "2026", "new-region"]
nav_exclude: true
---

# Amazon GameLift Streams Now Offers Service-managed Shader Caching

**날짜:** 2026년 08월 11일
**서비스:** General
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/Amazon-GameLift-Streams-Shader-Caching/

## 내용

Amazon GameLift Streams now manages shader cache capture and distribution for your applications. You capture a shader cache from a stream session, and the service automatically makes it available for future sessions across your streaming locations. No application changes are required.  Capturing shader caches can help reduce loading times and visual stuttering, during the session. With service-managed shader caching, you designate a stream session for capture and run your application to generate the cache. Amazon GameLift Streams then replicates the cache to compatible stream groups and locations, and loads it automatically in future sessions.  You can monitor shader cache status and storage size using the ListApplicationShaderCaches API or the Amazon GameLift Streams console. The feature supports Linux (Ubuntu 22.04), Proton, and Windows Server 2022 runtimes.  You are charged for storage of the latest version of each shader cache. For pricing details, visit the Amazon GameLift Streams pricing page. For supported Regions, see the AWS Region table.

## 핵심 요약

요약 미지원
