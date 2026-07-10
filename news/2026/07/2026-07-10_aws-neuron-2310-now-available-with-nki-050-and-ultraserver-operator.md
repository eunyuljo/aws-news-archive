---
title: "AWS Neuron 2.31.0 now available with NKI 0.5.0 and UltraServer Operator"
date: "2026-07-10"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-announce-neuron-2-31-0"
tags: ["EKS", "2026", "GA", "price-reduction", "performance"]
nav_exclude: true
---

# AWS Neuron 2.31.0 now available with NKI 0.5.0 and UltraServer Operator

**날짜:** 2026년 07월 10일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-announce-neuron-2-31-0

## 내용

AWS Neuron 2.31.0 is now available, introducing NKI 0.5.0 with new MX FP8 scale dtype support, tensor indirection on compute operations for fewer instructions in indexed access patterns, and new NkiTensor view APIs for zero-cost tensor layout transformations. This release also introduces the Neuron UltraServer Operator for Amazon EKS in public beta, automating UltraServer discovery, workload allocation, and resource claim generation for Trainium UltraServer workloads on Amazon EKS. 
The Neuron Compiler includes a redesigned code generation backend now enabled by default on Trn2 and Trn3, delivering improved performance. The Neuron Runtime adds contiguous shared scratchpad support, simplifying device configuration by eliminating the need to manually set scratchpad page sizes. The NKI Library adds 14 new experimental kernels covering MoE training collectives, deformable attention, DeepSeek MLA projection, and ring attention, alongside PyTorch reference implementations. Neuron Explorer adds System Trace Viewer source code linking and updated default grouping for improved workload debugging. 
To get started, see the following resources: 
 
 AWS Neuron 2.31.0 What's New  
 
 
 AWS Neuron 2.31.0 Release Notes  
 
 
 Neuron Kernel Interface (NKI) Documentation  
 
 
 Neuron Agentic Development  
 
 
 AWS Neuron Developer Guide

## 핵심 요약

요약 미지원
