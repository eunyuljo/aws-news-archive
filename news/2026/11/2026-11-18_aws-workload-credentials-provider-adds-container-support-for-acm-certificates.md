---
title: "AWS Workload Credentials Provider adds container support for ACM certificates"
date: "2026-11-18"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/acm-certificates-container-support/"
tags: ["EC2", "2026", "security"]
nav_exclude: true
---

# AWS Workload Credentials Provider adds container support for ACM certificates

**날짜:** 2026년 11월 18일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/acm-certificates-container-support/

## 내용

The open source AWS Workload Credentials Provider can now export AWS Certificate Manager (ACM) certificates to applications running in containers on Amazon Elastic Container Service (Amazon ECS), including AWS Fargate, Amazon Elastic Kubernetes Service (Amazon EKS), and Docker on Amazon EC2. You can now automate certificate deployment and renewal for containerized TLS workloads the same way you do on EC2 instances, on both Linux and Windows.
The provider runs as a sidecar in your ECS task or EKS pod. It exports each certificate and private key to a shared volume and writes the renewed files when ACM rotates the certificate. For TLS servers that don't reload certificate files on their own, such as NGINX, Apache, HAProxy, or IIS, a companion watcher in the TLS container runs your reload command after each renewal. The watcher needs no AWS credentials. TLS servers that reload automatically, such as Envoy, Traefik, and Caddy, need only the shared volume. Access is controlled through IAM: the sidecar assumes a per-workload role that is allowed to export only that workload's certificates.
To get started, download the provider and watcher binaries for Linux (x86_64 and Arm64) or Windows, and follow the setup steps and ECS and EKS examples in the AWS Workload Credentials Provider README on GitHub. The provider is available at no additional charge, and standard ACM charges apply to exported certificates. To learn more, see the AWS Certificate Manager documentation.

## 핵심 요약

요약 미지원
