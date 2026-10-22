---
title: "AWS Neuron 2.33 adds native PyTorch support, Neuron Observer, and other new features"
date: "2026-10-22"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-announce-neuron-2-33-0"
tags: ["EC2", "2026", "GA", "ai-ml"]
nav_exclude: true
---

# AWS Neuron 2.33 adds native PyTorch support, Neuron Observer, and other new features

**날짜:** 2026년 10월 22일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-announce-neuron-2-33-0

## 내용

AWS Neuron 2.33 is now available, introducing TorchNeuron, the native PyTorch backend for AWS Trainium, in public beta. You can run models written with the standard PyTorch APIs on Amazon EC2 Trn2 and Trn3 instances, in eager mode or with torch.compile. This release also introduces Neuron Observer in public beta, which detects Trainium health issues in under a second and identifies the affected node or device. 
The vLLM Neuron plugin upgrades to vLLM 0.29.0, and the vLLM Omni Neuron plugin for Wan2.2 video generation is now part of the Neuron release. Both support native PyTorch compilation through TorchNeuron. A new Neuron Deep Learning AMI and Deep Learning Container for PyTorch training include TorchNeuron, PyTorch 2.14, and TorchTitan. Neuron Explorer opens profiles captured with torch.profiler. From a PyTorch memory snapshot, it now attributes allocations to the Python source lines that made them, for debugging out-of-memory errors in eager mode. 
Kernels written with the Neuron Kernel Interface (NKI) can now use the full Python language for metaprogramming, including generators and class inheritance. The NKI Library adds 25 new experimental kernels, including kernels for DeepSeek-V3.2, Qwen3.5, and Kimi Delta Attention. 
To get started, see the following resources: 
 
 AWS Neuron 2.33.0 Release Notes  
 
 
 AWS TorchNeuron documentation  
 
 
 AWS Neuron Observer documentation  
 
 
 AWS Neuron Kernel Interface documentation  
 
 
 AWS Neuron

## 핵심 요약

요약 미지원
