---
title: "Launching External Web Access for Web Search on Amazon Bedrock"
date: "2026-08-20"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-web-access-web-search/"
tags: ["IAM", "2026", "GA", "price-reduction", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# Launching External Web Access for Web Search on Amazon Bedrock

**날짜:** 2026년 08월 20일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-web-access-web-search/

## 내용

Earlier this month, we announced Web Search on Amazon Bedrock, a built-in server-side tool that allows you to ground model responses with current web knowledge, while maintaining data within your secured AWS environment with zero data egress. Today, we are expanding Web Search to enable the external_web_access parameter allowing Web Search to retrieve content directly from the public web so models can ground responses in the latest information. 
To enable external_web_access, grant the bedrock-websearch:ExternalWebAccess IAM permission to the request identity and leave the external_web_access parameter at its default of true. &nbsp;In doing so, Web Search can then fetch content live from the public web for use cases that need the freshest possible information, such as latest sports score, live pricing, or newly released documentation. If handling sensitive data, to keep retrieval entirely within your AWS boundary, set external_web_access: false. By setting it false, Web Search serves results only from Amazon's in-AWS web index and knowledge graph, with no request data leaving the AWS boundary. &nbsp; 
Enabling External Web Access is available in the following AWS Regions: US East (N. Virginia), US East (Ohio), and US West (Oregon). To learn more, read our blog post Introducing Web Search on Amazon Bedrock for foundation model grounding, review Controlling external web access in the Amazon Bedrock User Guide, and visit the Amazon Bedrock pricing page for cost details. 
&nbsp;

## 핵심 요약

요약 미지원
