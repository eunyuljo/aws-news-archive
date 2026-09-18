---
title: "AWS Elastic Beanstalk introduces Cluster Mode to run multiple applications on shared infrastructure"
date: "2026-09-18"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/elastic-beanstalk-cluster-mode/"
tags: ["EKS", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# AWS Elastic Beanstalk introduces Cluster Mode to run multiple applications on shared infrastructure

**날짜:** 2026년 09월 18일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/elastic-beanstalk-cluster-mode/

## 내용

AWS Elastic Beanstalk introduces Cluster Mode, a new deployment mode that lets you run and manage multiple applications on shared infrastructure in your account. Provide your source code, a Dockerfile, or a container image in Amazon ECR, and Elastic Beanstalk handles containerization, provisioning, and ongoing operations through the console, CLI, and APIs you already use. A new Elastic Beanstalk GitHub Action deploys your application directly from your repository as part of your CI/CD pipeline. 
AWS Elastic Beanstalk deploys, scales, and manages your applications for their full lifecycle while handling the infrastructure, so you can focus on your code. It now offers two deployment modes. Standard Mode is the existing Elastic Beanstalk experience and continues to support all currently available platforms, including .NET, Node.js, and Python. Cluster Mode runs multiple applications on pooled infrastructure in your account, powered by Amazon EKS, instead of a dedicated environment per application. This can lower your per-application compute cost as your applications scale or your application count grows. Cluster Mode supports event-driven autoscaling, OpenTelemetry-based observability to Amazon CloudWatch and third-party providers, AWS Secrets Manager integration, and HTTPS by default via AWS Certificate Manager. 
To get started, create an environment in the Elastic Beanstalk console and select Cluster Mode. You can also deploy with the AWS CLI, the GitHub Action, or the agent skills. 
Cluster Mode is available in all commercial AWS Regions where Elastic Beanstalk is available. Elastic Beanstalk is HIPAA eligible and in scope for programs including PCI DSS, SOC, FedRAMP, and IRAP. There is no additional charge for Cluster Mode. You pay for the AWS resources your applications consume, including the EKS cluster and EKS Auto Mode charges for the infrastructure Elastic Beanstalk provisions on your behalf. See the Elastic Beanstalk and EKS pricing pages for details. 
To learn more, see the AWS News blog, the Elastic Beanstalk Developer Guide, and the Elastic Beanstalk product page, or download the agent skills.

## 핵심 요약

요약 미지원
