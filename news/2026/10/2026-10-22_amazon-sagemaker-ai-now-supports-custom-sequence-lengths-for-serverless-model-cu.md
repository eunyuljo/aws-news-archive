---
title: "Amazon SageMaker AI now supports custom sequence lengths for serverless model customization jobs"
date: "2026-10-22"
service: "SageMaker"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/sagemaker-custom-sequence-lengths/"
tags: ["SageMaker", "2026", "GA", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker AI now supports custom sequence lengths for serverless model customization jobs

**날짜:** 2026년 10월 22일
**서비스:** SageMaker
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/sagemaker-custom-sequence-lengths/

## 내용

Today, Amazon SageMaker AI announces the ability to configure the sequence length used during your serverless model customization job. Amazon SageMaker AI serverless model customization supports fine-tuning for many open-weight models, including models from popular families including gpt-oss, Gemma, Llama, Nemotron, and Qwen. Previously, each fine-tuning recipe ran at a fixed sequence length that customers could not modify. Customers sometimes need to modify these parameters to achieve better results for their use case. Customers also asked for longer sequence lengths than the static defaults we supported on some models.
Now, you can set sequence length parameters as part of the customization job's hyperparameters, anywhere up to the published maximum for your chosen model and technique. You can set the dataset_max_len hyperparameter for SFT and DPO jobs or set max_prompt_length and max_response_length hyperparameters for RFT jobs. This gives you more control to match your training data characteristics, whether you are working with short question-answer pairs or multi-page documents. Published maximums are up to 16K tokens for many models depending on model and technique.
Serverless model customization on SageMaker AI is available in US East (N. Virginia), US West (Oregon), Asia Pacific (Tokyo), and Europe (Ireland). To get started, navigate to the Models page in Amazon SageMaker Studio to launch a customization job, use the SageMaker Python SDK or use our Agent skills with your choice of coding assistant. To learn more, and see the list of models and supported sequence lengths per technique, see the SageMaker AI documentation.

## 핵심 요약

요약 미지원
