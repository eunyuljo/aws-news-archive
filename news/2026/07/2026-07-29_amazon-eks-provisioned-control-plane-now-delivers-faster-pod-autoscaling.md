---
title: "Amazon EKS Provisioned Control Plane now delivers faster pod autoscaling"
date: "2026-07-29"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-provisioned-control/"
tags: ["EKS", "2026", "performance"]
nav_exclude: true
---

# Amazon EKS Provisioned Control Plane now delivers faster pod autoscaling

**날짜:** 2026년 07월 29일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-provisioned-control/

## 내용

Amazon EKS now delivers faster pod autoscaling across all Provisioned Control Plane clusters by increasing Horizontal Pod Autoscaler (HPA) sync concurrency to up to 40 times the default Kubernetes value. This reduces the time it takes for HPA-driven workloads to scale in response to increased load, enabling faster responsiveness to demand.  The Kubernetes Horizontal Pod Autoscaler (HPA) continuously monitors workload metrics and adjusts pod counts to match demand. In clusters running hundreds or thousands of HPA objects, the speed at which the Kubernetes control plane processes these objects determines how quickly workloads scale in response to changing demand. The HPA sync concurrency setting controls how many HPA objects the control plane evaluates in parallel. By increasing this value, Provisioned Control Plane clusters now process more HPA objects simultaneously, reducing the time between detecting increased load and scaling out pods.  This enhancement is available to all customers using EKS Provisioned Control Plane and requires no configuration changes. To learn more about this enhancement, see EKS Provisioned Control Plane in the EKS User Guide.

## 핵심 요약

요약 미지원
