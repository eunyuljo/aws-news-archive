---
title: "AWS Neuron 2.32 introduces expanded NKI programming, MXFP8 training kernels, and variable-size collectives for Trn2 and Trn"
date: "2026-08-25"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-announce-neuron-2-32-0"
tags: ["EC2", "2026", "GA", "new-region", "ai-ml"]
nav_exclude: true
---

# AWS Neuron 2.32 introduces expanded NKI programming, MXFP8 training kernels, and variable-size collectives for Trn2 and Trn

**날짜:** 2026년 08월 25일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-announce-neuron-2-32-0

## 내용

AWS Neuron 2.32.0 is now available, introducing NKI 0.6.0 with an on-device top-K instruction, a variable-length `all-gather `for kernels whose ranks hold differently sized tensors, and new loop constructs for data-dependent iteration. &nbsp; 
This release also introduces 13 new NKI Library kernels for Mixture of Experts (MoE) training and sparse attention, and a new Neuron Agentic Development skill that ports transformer models to the vLLM Neuron plugin. The NKI Library kernels cover context encoding for DeepSeek-V3.2 sparse multi-head latent attention, MXFP8 attention for the decode step, and a matched MXFP8 forward and backward pass that lets blockwise MoE layers train end to end in MXFP8, with PyTorch reference implementations for 22 additional kernels. &nbsp; 
The Neuron Runtime adds variable-size all-gather, reduce-scatter, and all-to-all collectives on Trn2 and Trn3, letting each rank contribute or receive a different number of elements. The vLLM Neuron plugin moves to vLLM 0.24.0 and is included in all Neuron Deep Learning AMIs and Deep Learning Containers. The Neuron Compiler adds explicit control over 64-bit integer compilation, and Neuron Explorer adds per-core host CPU utilization to the System Trace Viewer. 
AWS Neuron is available in all AWS Regions where Amazon EC2 Trn1, Trn2, Trn3, Inf2, and Inf1 instances are available. For more information about Regional availability, see the AWS Region table. 
To get started, see the following resources: 
 
 AWS Neuron 2.32.0 Release Notes  
 
 
 Neuron Kernel Interface (NKI) Documentation  
 
 
 Neuron Agentic Development  
 
 
 AWS Neuron

## 핵심 요약

요약 미지원
