---
title: "Amazon ECS now automatically detects and repairs container instances with impaired agent connectivity"
date: "2026-08-25"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ecs-agent-connectivity-health"
tags: ["EC2", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon ECS now automatically detects and repairs container instances with impaired agent connectivity

**날짜:** 2026년 08월 25일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ecs-agent-connectivity-health

## 내용

Amazon Elastic Container Service (Amazon ECS) now&nbsp;automatically detects and repairs container instances, enabling customers to reduce undetected workload failures and improve application availability without manual intervention. 
With this launch, Amazon ECS continuously monitors agent connectivity across container instances. Infrastructure events such as EBS volume degradation, host thermal events, or network connectivity failures can sever the ECS agent's connection to the ECS control plane. Amazon ECS now surfaces a new type of container instance health change event (AGENT_CONNECTIVITY) for all compute options: AWS Fargate, Amazon ECS Managed Instances, and Amazon ECS on EC2. For ECS Managed Instances and AWS Fargate, ECS automatically performs recovery - automatically draining running tasks and launching replacement capacity while deregistering impaired instances. Customers running workloads on Amazon ECS on EC2, can use this health change event to drive instance replacement workflows. 
This capability is available at no additional cost in all AWS Commercial and AWS GovCloud (US) Regions. To learn more, see Monitor Amazon ECS Container Instance Health.

## 핵심 요약

요약 미지원
