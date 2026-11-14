---
title: "Amazon SageMaker Unified Studio now supports layout customization for designations"
date: "2026-11-14"
service: "SageMaker"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-studio-layout-customization/"
tags: ["SageMaker", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker Unified Studio now supports layout customization for designations

**날짜:** 2026년 11월 14일
**서비스:** SageMaker
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-studio-layout-customization/

## 내용

Amazon SageMaker Unified Studio now supports layout customization, a new capability that gives domain administrators control over which tools and left navigation items project members see based on their designation. Organizations with data engineering, analytics, and machine learning teams on a single platform can configure a layout within each designation definition, and that layout applies across every project in the domain without per-project configuration. 
Previously, all project members saw the same interface regardless of their role, creating confusion and potential governance issues. With layout customization, administrators define a layout as part of a designation that specifies which left navigation items are visible for project members assigned to that designation. When a project member opens a project, SageMaker Unified Studio resolves the member's designation and renders only the tools included in their designation's layout. For example, a SQL analyst designation can be configured to show only the Query Editor, while an ML engineer designation shows notebooks, training jobs, and model endpoints. Navigation items are configurable across categories including Data Analytics, artificial intelligence and machine learning (AI/ML), Generative AI, and IDEs. If a project member navigates directly to a hidden page, they see an access-denied page. For members with multiple designations, visible tools are the union of all their designations' layouts. New navigation items added to SageMaker Unified Studio remain hidden for designations with a configured layout until an administrator adds them. 
This feature is available in all AWS Regions where Amazon SageMaker Unified Studio is available. To learn more, visit the Designations documentation.

## 핵심 요약

요약 미지원
