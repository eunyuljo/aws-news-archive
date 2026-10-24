---
title: "Web Search on AWS Bedrock now supports domain filtering and user location controls"
date: "2026-10-24"
service: "Bedrock"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/bedrock-web-search-domain-user-location/"
tags: ["Bedrock", "2026", "new-region"]
nav_exclude: true
---

# Web Search on AWS Bedrock now supports domain filtering and user location controls

**날짜:** 2026년 10월 24일
**서비스:** Bedrock
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/bedrock-web-search-domain-user-location/

## 내용

Web Search on AWS Bedrock now supports two new controls that give you more precision over the results that ground a model's response: domain filtering and user location. Both are configured directly on the web_search tool in your existing OpenAI Responses API request. 
With domain filtering, you can restrict Web Search results to a set of domains you choose. Using the filters parameter, you specify up to 100 allowed_domains to limit results to trusted sources, or up to 100 blocked_domains to exclude sources you don't want. This is useful when you want responses grounded only in specific sites, or when you need to keep certain domains out of results. 
With user location, you can optionally specify location parameters so that Web Search can return results relevant to that geography. This helps with location-dependent questions, such as regional availability or local services. 
Domain filtering and user location are available in all AWS Regions where Web Search is supported: US East (N. Virginia), US East (Ohio), US West (Oregon), and AWS GovCloud (US-West). To get started, see the Web Search section in the AWS Bedrock User Guide. For pricing, see the AWS Bedrock pricing page.

## 핵심 요약

요약 미지원
