---
title: "AgentCore runtime instances now support Amazon EC2 G7 instances"
date: "2026-11-21"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/agentcore-ec2-g7/"
tags: ["EC2", "2026", "price-reduction", "new-region", "ai-ml"]
nav_exclude: true
---

# AgentCore runtime instances now support Amazon EC2 G7 instances

**날짜:** 2026년 11월 21일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/agentcore-ec2-g7/

## 내용

Amazon Bedrock AgentCore runtime instances now support Amazon EC2 G7 instances, powered by NVIDIA RTX PRO 4500 Blackwell Server Edition GPUs. Runtime instances run your agents on Amazon EC2 instances while AgentCore handles provisioning, patching, scaling, and lifecycle management. G7 instances give agents that do 3D rendering or model inference another GPU option, alongside families such as G6e and G7e. 
To use G7, add G7 instance types, from g7.2xlarge to g7.48xlarge, to the allowed instance types of your capacity provider. AgentCore installs the NVIDIA drivers on the instance, so standard container images run GPU workloads without bundling drivers. For example, an agent can render 3D scenes or run a vision model on its own GPU, in sessions of up to 14 days. 
G7 instances on runtime instances are available in select AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Europe (Frankfurt), Europe (London), Europe (Stockholm), Asia Pacific (Mumbai), and Asia Pacific (Sydney). You are charged for managing the provisioned compute, in addition to your Amazon EC2 costs. 
To get started, see the following resources: 
 
 Use GPU instance types in the Amazon Bedrock AgentCore Developer Guide 
 AgentCore pricing

## 핵심 요약

요약 미지원
