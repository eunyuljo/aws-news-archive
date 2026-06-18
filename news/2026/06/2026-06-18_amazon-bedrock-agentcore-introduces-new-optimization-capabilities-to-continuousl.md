---
title: "Amazon Bedrock AgentCore introduces new optimization capabilities to continuously improve agents in production"
date: "2026-06-18"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-new-optimization-capabilities"
tags: ["Lambda", "2026", "GA", "preview", "new-region"]
nav_exclude: true
---

# Amazon Bedrock AgentCore introduces new optimization capabilities to continuously improve agents in production

**날짜:** 2026년 06월 18일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-new-optimization-capabilities

## 내용

Today, AWS announces new optimization capabilities in AgentCore that turn production traces into continuous improvement for agents. The most dangerous agent failures are not the ones that throw errors. They are the silent ones that look fine on dashboards. These failures produce no error signal and often surface through customer complaints weeks later. AgentCore closes that gap with a loop to understand what agents are doing, generate fixes grounded in data, and prove they work.  To understand agent behavior, AgentCore surfaces failure, intent, and trajectory insights across hundreds of sessions, revealing patterns no dashboard or one-at-a-time trace review would catch. Failure insights discover recurring failure patterns, including silent behavioral failures, explain the root cause of each, and rank them by how widespread they are, so teams can fix the problems hurting the most users first. Intent insights cluster requests by what users were trying to do, and trajectory insights group the paths agents take through a task, surfacing common patterns and outliers. Customers can enable continuous monitoring or run a targeted investigation in minutes. To fix issues with confidence, recommendations analyze traces and evaluation outputs to suggest specific improvements to system prompts and tool descriptions, grounded in how the agent actually behaves. Each recommendation includes a clear rationale tied to observed failures and comes ready to validate, not a generic suggestion but a targeted change derived from production data. Before a change reaches users, batch evaluation tests recommendations against a defined test dataset and reports aggregate scores across multiple evaluators, catching regressions early. Customers define what "good" looks like, and batch evaluation measures each candidate change against that bar at scale. A/B testing then confirms improvements hold under real conditions, running a controlled comparison between agent versions by splitting live production traffic and measuring outcomes side by side. This provides statistical evidence that a change actually works in production, not just on test data, before customers commit to rolling it out fleet-wide. These capabilities work regardless of where agents run: on AgentCore’s runtime, AWS Lambda, Amazon EKS, or non-AWS environments.  Failure, intent, and trajectory insights are available in preview today in 13 AWS Regions. Batch evaluations, recommendations, and A/B tests are generally available today in 14 AWS Regions. To learn more, visit Amazon Bedrock AgentCore or explore the documentation.

## 핵심 요약

요약 미지원
