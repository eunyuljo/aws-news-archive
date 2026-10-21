---
title: "Announcing Amazon ECS Gateway, a managed ingress solution for your ECS services"
date: "2026-10-21"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/announcing-amazon-ecs-gateway/"
tags: ["RDS", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# Announcing Amazon ECS Gateway, a managed ingress solution for your ECS services

**날짜:** 2026년 10월 21일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/announcing-amazon-ecs-gateway/

## 내용

AWS announces Amazon Elastic Container Service (Amazon ECS) Gateway, a new resource that simplifies ingress networking for containerized applications by dynamically provisioning and managing Application Load Balancers (ALBs) and their supporting resources directly in your account. 
With ECS Gateway, platform teams define organizational networking standards once on a gateway and associate it with one or more clusters, giving organizations a centralized way to govern how traffic reaches their ECS services. Application teams simply opt in to inherit those standards without requiring networking expertise. ECS Gateway offers host-based routing, allows up to 25 services to share an ALB to optimize infrastructure costs, and gives each service a unique Domain Name System (DNS) hostname. ECS manages the full lifecycle of the underlying infrastructure, provisioning the first ALB when your first service connects, adding more ALBs when capacity is reached, and removing them when no longer needed. You can inspect these resources and the gateway route to each service to see exactly how requests reach your applications. For traffic and health monitoring, you can use standard ALB metrics in Amazon CloudWatch and target health information from Elastic Load Balancing. 
To get started, create an ECS Gateway, associate it with a cluster, and opt in your ECS service by adding the gateway connector parameter using the AWS Management Console, AWS CLI, API, AWS SDKs, or AWS CloudFormation. ECS Gateway is available for ECS services using the awsvpc network mode across all launch types. It is available now in all commercial AWS Regions at no additional charge. You pay only for the underlying infrastructure provisioned in your account when your services connect to the gateway. To learn more, refer to the AWS News blog and our documentation page.

## 핵심 요약

요약 미지원
