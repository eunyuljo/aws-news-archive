---
title: "Amazon EKS now supports local clusters on AWS Outposts with Amazon EC2 instance store"
date: "2026-06-17"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-eks-aws-outposts-ec2-instance-store/"
tags: ["EC2", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# Amazon EKS now supports local clusters on AWS Outposts with Amazon EC2 instance store

**날짜:** 2026년 06월 17일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-eks-aws-outposts-ec2-instance-store/

## 내용

Today, AWS is expanding support for Amazon Elastic Kubernetes Service (EKS) local clusters on AWS Outposts to first-generation and second-generation AWS Outposts racks running Amazon EC2 instances that boot from Amazon EC2 instance store. AWS Outposts offers static stability for Amazon EC2 instances backed by EC2 instance store, and AWS is now extending that benefit to Amazon EKS local clusters customers. With local clusters, the entire Kubernetes control plane runs on AWS Outposts, supporting advanced data residency requirements and mitigating the risk of impact from temporary network disconnects to the cloud.  Amazon EKS local clusters on AWS Outposts backed by Amazon EC2 instance store use an updated architecture that brings greater operational and feature-level parity with Amazon EKS clusters in the cloud. The Kubernetes control plane on your Outpost&nbsp;is managed by Amazon EKS in a service-owned account, so you don’t need to manage etcd backups or logging agents on control plane instances. New Kubernetes versions and Amazon EKS platform versions are made available for local clusters as they’re released for Amazon EKS in the cloud. Local clusters deployed with the updated architecture support Amazon EKS add-ons, IAM Roles for Service Accounts, EKS Pod Identity, OIDC authentication, access entries, and Bottlerocket worker nodes (in addition to Amazon Linux 2023).  The updated architecture and new capabilities are generally available on AWS Outposts racks backed by Amazon EC2 instance store in all commercial AWS Regions that support AWS Outposts racks. AWS Outposts that boot Amazon EC2 instances from Amazon EBS will continue to use the original local clusters architecture. For more information, see local clusters in the Amazon EKS user guide.

## 핵심 요약

요약 미지원
