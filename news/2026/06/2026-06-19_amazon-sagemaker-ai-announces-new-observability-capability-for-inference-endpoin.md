---
title: "Amazon SageMaker AI Announces New observability capability For Inference Endpoints"
date: "2026-06-19"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-sagemaker-ai-inference/"
tags: ["CloudWatch", "2026", "new-region", "performance", "security", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker AI Announces New observability capability For Inference Endpoints

**날짜:** 2026년 06월 19일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-sagemaker-ai-inference/

## 내용

Amazon SageMaker AI's new observability capability allows customers to operate production generative AI inference workloads with confidence by providing comprehensive visibility into token performance, GPU health, inference component placement, and autoscaling behavior. It takes away the manual work of searching CloudWatch for per-endpoint metrics, correlating latency spikes with GPU saturation or KV cache exhaustion and diagnosing why scaling operations are slow. This capability tracks inference performance metrics in real-time, including Time to First Token, inter-token latency, queue depth, and tokens per second, and surfaces them alongside infrastructure health so customers can identify and resolve issues in minutes rather than hours. 
SageMaker AI detailed observability transforms how customers monitor and optimize their inference fleet. The new pre-built SageMaker AI Insights dashboard in Amazon CloudWatch gives customers token latency, GPU utilization, inference component copy counts, scaling events, and cold start breakdowns in a single view with OpenTelemetry native metrics published automatically, no instrumentation required. This allows teams to quickly diagnose TTFT degradation, verify availability zone compliance, and tune autoscaling policies. Customers who have standardized on observability tools like Grafana can connect directly using the regional PromQL endpoint and import a pre-configured dashboard template. This capability helps customers self-serve operational issues and maximize the performance of their AI investments. 
SageMaker AI Inference observability is available in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), US West (N. California), Canada (Central), South America (São Paulo), Europe (Ireland), Europe (Frankfurt), Europe (London), Europe (Stockholm), Europe (Zurich), Asia Pacific (Mumbai), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Asia Pacific (Seoul), and Asia Pacific (Jakarta). To learn more, visit the Documentation and Amazon SageMaker AI webpage.

## 핵심 요약

요약 미지원
