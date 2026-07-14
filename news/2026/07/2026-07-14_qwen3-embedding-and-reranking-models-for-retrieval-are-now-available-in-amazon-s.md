---
title: "Qwen3 embedding and reranking models for retrieval are now available in Amazon SageMaker JumpStart"
date: "2026-07-14"
service: "SageMaker"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/qwen3-search-retrieval-on-sagemaker-jumpstart/"
tags: ["SageMaker", "2026", "GA", "performance", "ai-ml"]
nav_exclude: true
---

# Qwen3 embedding and reranking models for retrieval are now available in Amazon SageMaker JumpStart

**날짜:** 2026년 07월 14일
**서비스:** SageMaker
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/qwen3-search-retrieval-on-sagemaker-jumpstart/

## 내용

Today, AWS announced the availability of Qwen3-VL-Embedding-2B and Qwen3-Reranker-4B in Amazon SageMaker JumpStart, expanding the portfolio of foundation models available to AWS customers. These models from Qwen are designed for information retrieval and cross-modal understanding, enabling customers to build comprehensive search pipelines on AWS infrastructure. The two models are typically used in tandem: the embedding model performs efficient initial recall, while the reranker refines results in a subsequent re-ranking stage. 
These models address different stages of the retrieval pipeline with specialized capabilities: 
Qwen3-VL-Embedding-2B accepts diverse inputs including text, images, screenshots, and videos, as well as inputs containing a mixture of these modalities, and generates semantically rich vectors that capture both visual and textual information in a shared space. It delivers performance across diverse multimodal tasks such as image-text retrieval, video-text matching, visual question answering, and multimodal content clustering, with support for over 30 languages. 
Qwen3-Reranker-4B takes a query and document pair as input and outputs a precise relevance score to refine retrieval results. It supports text retrieval, code retrieval, text classification, text clustering, and bitext mining across over 100 languages, with user-defined instructions to enhance performance for specific tasks, languages, or scenarios. 
With SageMaker JumpStart, customers can deploy any of these models with just a few clicks to address their specific AI use cases. To get started with these models, navigate to the Models section of SageMaker Studio or use the SageMaker Python SDK to deploy the models to your AWS account. For more information about deploying and using foundation models in SageMaker JumpStart, see the Amazon SageMaker JumpStart documentation.

## 핵심 요약

요약 미지원
