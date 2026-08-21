---
title: "Amazon EKS now supports certificate authority (CA) rotation with automated lifecycle management"
date: "2026-08-21"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-certificate-authority-ca-rotation-automated-lifecycle-management"
tags: ["RDS", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon EKS now supports certificate authority (CA) rotation with automated lifecycle management

**날짜:** 2026년 08월 21일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-certificate-authority-ca-rotation-automated-lifecycle-management

## 내용

Today, Amazon Elastic Kubernetes Service (Amazon EKS) announced certificate authority (CA) rotation, enabling customers to rotate their cluster's CA through a managed lifecycle with automated safeguards. Each Amazon EKS cluster has its own CA that allows encrypted connections to the cluster's Kubernetes API, and now you can rotate the CA before it expires to ensure your cluster remains operational and secure. 
Amazon EKS clusters created since launch in 2018 have CAs with a 10-year validity period, and clusters from that era are now approaching the point where CA rotation activities should begin. CA rotation in Amazon EKS is a shared responsibility. Amazon EKS manages the rotation lifecycle and automatically updates AWS-managed components to trust the successor CA. Customers are responsible for replacing their worker nodes and updating external clients to trust the successor CA before it is activated. EKS Auto Mode instances and AWS Fargate nodes are updated automatically by AWS, but customers are still responsible for updating any external clients that connect to the cluster's API server. Amazon EKS provides automated safeguards to support customers through this process, including advance notifications before CA expiration, automatic appending of a successor CA if one is not created by the customer, and automatic activation if the customer does not activate on their own schedule. A rollback capability allows customers to revert to the previous CA to resolve any issues that may arise with their updates during the transition to the successor CA. 
Amazon EKS CA rotation is available at no additional cost in all commercial AWS Regions. To get started with CA rotation, you can use the AWS CLI, EKS APIs, CloudFormation, and the AWS console. For more information, see the Amazon EKS documentation&nbsp;and&nbsp;Deep dive into Amazon EKS certificate authority rotation.

## 핵심 요약

요약 미지원
