---
title: "Amazon GameLift Streams now supports sharing streams with stream URLs"
date: "2026-08-04"
service: "General"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-gamelift-streams/"
tags: ["General", "2026", "new-region"]
nav_exclude: true
---

# Amazon GameLift Streams now supports sharing streams with stream URLs

**날짜:** 2026년 08월 04일
**서비스:** General
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-gamelift-streams/

## 내용

Amazon GameLift Streams now offers stream URLs, which give end users temporary, unauthenticated access to a playable stream session in a supported web browser. Recipients need no AWS account, no credentials, and no software install. 
To share a playable stream, create a stream URL for a stream group and one of its applications, set how long the stream URL stays valid and how many sessions it can start, and send the link. Each person who opens the link starts an independent stream session, and Amazon GameLift Streams routes them to a nearby streaming location from the locations you selected. No client integration or backend service is required. You can create, monitor, and revoke stream URLs in the Amazon GameLift Streams console or with the new CreateStreamUrl, GetStreamUrl, ListStreamUrls, and RevokeStreamUrl APIs. 
There is no additional charge for stream URLs. You are charged for the stream capacity that sessions started from a stream URL consume, as described on the Amazon GameLift Streams pricing page. For a full list of supported Regions, see the AWS Region table. 
To get started, see Share stream sessions with stream URLs in the Amazon GameLift Streams Developer Guide and the CreateStreamUrl API Reference. To learn more about the service, see the Amazon GameLift Streams product page.&nbsp;

## 핵심 요약

요약 미지원
