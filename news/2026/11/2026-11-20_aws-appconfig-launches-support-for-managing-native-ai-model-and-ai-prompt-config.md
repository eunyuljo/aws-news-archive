---
title: "AWS AppConfig launches support for managing native AI model and AI prompt configuration"
date: "2026-11-20"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-appconfig-native-ai-model-invocation-prompt-configurations/"
tags: ["CloudWatch", "2026", "GA", "performance", "ai-ml"]
nav_exclude: true
---

# AWS AppConfig launches support for managing native AI model and AI prompt configuration

**날짜:** 2026년 11월 20일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-appconfig-native-ai-model-invocation-prompt-configurations/

## 내용

Today, AWS AppConfig introduces two new configuration profile types to help you manage the settings for your generative AI applications: AI model invocation configurations, and AI prompt configurations. You can now change model settings and prompts while your application is running, without redeploying code. These updates use AWS AppConfig's safe deployment practices, including gradual rollouts and automatic rollback. This can allow you to move faster and safer, and avoid unexpected behaviors and tokenomics results with rapidly evolving AI solutions. 
AI model invocation configurations store the settings your application uses to call an AI model. These include the model identifier, inference parameters such as temperature and maximum tokens, and messages such as system prompts and example conversation turns. Provider-specific options are managed in custom parameters, so the same schema works across AI providers. Similarly, AI prompt configurations store prompts as separately versioned artifacts. You can update&nbsp; and optimize a prompt on its own,without changing the model configuration, and reuse it across multiple applications. This allows for powerful prompt engineering. 
You can roll out a change to these gradually, for example to 10%, then 20%, then 30% of your traffic. Along the way, you can measure the change's effect on operational metrics, customer experience, and token usage. If an alarm in Amazon CloudWatch, Datadog, New Relic, or another observability solution goes off during the rollout, AWS AppConfig can automatically roll the change back to the previous state.

## 핵심 요약

요약 미지원
