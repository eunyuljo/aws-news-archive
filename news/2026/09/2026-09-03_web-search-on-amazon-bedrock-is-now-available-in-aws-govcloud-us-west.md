---
title: "Web Search on Amazon Bedrock is now available in AWS GovCloud (US-West)"
date: "2026-09-03"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-bedrock-web-aws-govcloud/"
tags: ["RDS", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# Web Search on Amazon Bedrock is now available in AWS GovCloud (US-West)

**날짜:** 2026년 09월 03일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-bedrock-web-aws-govcloud/

## 내용

The Web Search built-in server-side tool on Amazon Bedrock is now available in AWS GovCloud (US-West), helping bring grounded web results to compliance-sensitive government and public-sector workloads. Web Search helps supported OpenAI GPT models ground responses with information from the web. Responses include citations to the sources the model used so users can trace each claim back to its web origin. This can be especially valuable whenever an answer depends on information that changes over time or is more recent than a model's training data, such as current events, recent releases or live pricing. Because the tool runs inside Amazon Bedrock, you don't host a search index, manage crawlers, or write the tool-call loop yourself. 
Web Search is designed to support the governance and data-handling standards AWS GovCloud (US) customers require. By default, it keeps your request data within the AWS boundary, serving results from a web index and cache maintained by Amazon. As an AWS-native capability governed by AWS Identity and Access Management (IAM), administrators can allow or deny it at the account or organization level and restrict it by Region, giving teams centralized control while keeping request data within the AWS boundary by default. To get started, add a tool of type web_search to the tools array in your OpenAI Responses API request using your existing OpenAI client library with an Amazon Bedrock API key. The model uses the tool only when it determines a request needs current information. At launch, Web Search in AWS GovCloud (US-West) supports GPT-5.4 , GPT-5.6 Terra and Luna models. 
Web Search is available in AWS GovCloud (US-West), in addition to US East (N. Virginia), US East (Ohio), and US West (Oregon). To get started, see the Web Search technical blog. For implementation guidance, see the Web Search documentation. For pricing, see the Amazon Bedrock pricing page.

## 핵심 요약

요약 미지원
