---
title: "EC2 Image Builder now integrates with ASG for faster image builds"
date: "2026-10-20"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/ec2-image-builder-asg-faster-builds/"
tags: ["EC2", "2026", "GA", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# EC2 Image Builder now integrates with ASG for faster image builds

**날짜:** 2026년 10월 20일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/ec2-image-builder-asg-faster-builds/

## 내용

EC2 Image Builder now supports using existing instances from an Auto Scaling Group (ASG) for building images, enabling faster builds by eliminating the time spent in launching and bootstrapping new instances and reusing already running EC2 instances.
With this feature, you can provide an ASG in your Image Builder infrastructure configuration. Instead of launching a new instance at the build time, Image Builder selects an already-running instance from this ASG, applies your build components, and creates the image. The ASG continuously replenishes the pool as instances are used for builds, ensuring instances are always available for subsequent pipeline runs.
This feature is fully opt-in and does not affect existing pipelines. Pipelines without an ASG configured continue to use the default launch path with no behavior change.
This feature is available in all AWS Regions at no additional cost. To configure ASG integration in your Image Builder pipelines, see the EC2 Image Builder documentation.

## 핵심 요약

요약 미지원
