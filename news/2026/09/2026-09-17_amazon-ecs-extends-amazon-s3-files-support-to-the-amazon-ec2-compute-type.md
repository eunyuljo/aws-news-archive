---
title: "Amazon ECS extends Amazon S3 Files support to the Amazon EC2 compute type"
date: "2026-09-17"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ecs-s3-files-ec2/"
tags: ["S3", "2026", "GA", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# Amazon ECS extends Amazon S3 Files support to the Amazon EC2 compute type

**날짜:** 2026년 09월 17일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ecs-s3-files-ec2/

## 내용

Amazon Elastic Container Service (Amazon ECS) now supports Amazon S3 Files for tasks running on the Amazon EC2 launch type, enabling customers to connect their containerized applications directly to data in Amazon S3 as a shared file system. With this launch, customers running ECS workloads on EC2 instances can work with their S3 data using standard file system semantics, so file-based applications, AI agents, and data processing workloads run on S3 data with no code changes and without duplicating or staging files first. S3 Files support was previously available for ECS tasks on AWS Fargate and ECS Managed Instances, and now extends to the EC2 launch type, giving customers consistent access to S3 Files across all three ECS launch types.  Amazon S3 Files, built on Amazon EFS, delivers a shared file system that connects AWS compute resources directly with data in Amazon S3, providing full file system semantics and low-latency performance without data leaving S3. S3 Files works with new and existing data in S3 buckets, with no migration required. Customers can mount an Amazon S3 Files volume in their Amazon ECS tasks to read and write data in an S3 bucket using standard file system operations, with no application code changes and no need to copy or stage data.  Amazon S3 Files support is available in all AWS commercial Regions and the AWS GovCloud (US) Regions. To learn more, refer our documentation.

## 핵심 요약

요약 미지원
