---
title: "AWS Lambda durable functions integrates with Pydantic AI"
date: "2026-09-11"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-lambda-durable-pydantic-ai/"
tags: ["Lambda", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# AWS Lambda durable functions integrates with Pydantic AI

**날짜:** 2026년 09월 11일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-lambda-durable-pydantic-ai/

## 내용

Today, AWS Lambda durable functions announces an integration with Pydantic AI, an open source framework for building AI agents in Python. AWS Lambda durable functions saves your Pydantic AI agent's progress as it runs, so after an interruption like a timeout, your agent resumes from the last completed step instead of starting over. Your agent gains fault tolerance without you having to write the checkpoint and retry logic yourself. 
With this integration, each model and tool call your agent makes is a durable execution step, so an interrupted run does not repeat calls that already completed. This matters when the work is expensive to repeat, such as a chain of model calls that reviews a set of documents or researches a topic across many sources, where starting over means paying again for tokens to do the same work. It also helps to avoid unwanted side-effects when resuming execution, such as billing a customer twice. Because your agent runs on AWS Lambda, you manage no servers and pay only for the compute it uses. 
You can use this integration in any Python AWS Lambda durable function. It is available in all AWS Regions where AWS Lambda durable functions is available. To get started, install Pydantic AI and follow its AWS Lambda durability page. You can also find the integration details in the durable execution SDK reference. For more information about AWS Lambda durable functions, see the developer guide and the AWS Lambda product page.

## 핵심 요약

요약 미지원
