---
title: "Introducing AWS Nitro Sandboxes on Amazon EKS, ECS and EC2 for hardware isolated pods, tasks and VMs"
date: "2026-11-09"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/nitro-sandboxes-eks-ecs-ec2/"
tags: ["S3", "2026", "GA", "price-reduction", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Introducing AWS Nitro Sandboxes on Amazon EKS, ECS and EC2 for hardware isolated pods, tasks and VMs

**날짜:** 2026년 11월 09일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/nitro-sandboxes-eks-ecs-ec2/

## 내용

AWS Nitro Sandboxes are now available as lightweight VMs managed by the Nitro Hypervisor. You can use Nitro Sandboxes for an Amazon EKS pod, or Amazon ECS task, or lightweight Virtual Machines (VMs), including AI agents running inside them, in their own hardware-isolated virtual machine powered by the AWS Nitro System. Each workload gets the isolation boundary of a Nitro isolated virtual machine. This allows you to safely run untrusted, multi-tenant, or regulated workloads within the resources of a single instance. 
Nitro Sandboxes run on your EC2 instances with near-native EC2 performance and inherits Nitro-hypervisor isolation. You can also validate your workloads through cryptographic attestation, so that secrets are released only to Nitro Sandboxes that have proven their integrity. With Nitro Sandboxes, you can safely execute LLM-generated code in an isolated environment of its own all while improving utilization and lowering compute costs by securely sharing a single EC2 instance across multiple agentic workloads. You can easily enable EKS pods or ECS tasks to run on Nitro Sandboxes and each pod or task gets its own isolated environment. Enabling Nitro Sandboxes in EKS or ECS is a one-line change and each pod or task gets its own VM, with your workloads remaining fully native (Pod Identity, VPC CNI, EBS/EFS/S3 storage, and CloudWatch all work out of the box). If you want full control, run Nitro Sandboxes directly on EC2 with your own AMI, orchestration, and with virtual machine monitors (VMMs). Amazon Linux and Firecracker are natively supported, and patches for other options are available today. 
AWS Nitro Sandboxes are available today on most nitro-based ec2 instances, in all commercial regions worldwide, at no additional charge. 
To learn more and get started, see the EKS User Guide or ECS User Guide. For implementation details or to fully customize your Nitro Sandbox usage, see the Nitro Sandboxes documentation in the EC2 user guide.

## 핵심 요약

요약 미지원
