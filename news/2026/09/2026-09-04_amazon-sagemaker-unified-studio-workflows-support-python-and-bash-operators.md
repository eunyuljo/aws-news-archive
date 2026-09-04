---
title: "Amazon SageMaker Unified Studio Workflows support Python and Bash operators"
date: "2026-09-04"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/sagemaker-workflows-python-bash/"
tags: ["Lambda", "2026", "new-region"]
nav_exclude: true
---

# Amazon SageMaker Unified Studio Workflows support Python and Bash operators

**날짜:** 2026년 09월 04일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/sagemaker-workflows-python-bash/

## 내용

Amazon SageMaker Unified Studio Workflows now supports PythonOperator and BashOperator, enabling you to run custom Python functions and shell commands directly in your serverless workflows without provisioning separate compute resources. This eliminates the need to offload custom logic to Lambda or ECS for tasks like data transformations or shell script execution.
To get started, open a serverless visual workflow in your SageMaker Unified Studio project, search for PythonOperator or BashOperator in the task panel, and drag the node onto your canvas. Provide your Python or shell script files through the workflow settings, then point each operator to the function or command in your scripts. For example, configure PythonOperator to call a data transformation function or set BashOperator to run a shell command, all without leaving the visual canvas.
This feature is available in all AWS Regions where Amazon SageMaker Unified Studio is available. For more information, see Supported Regions for Amazon SageMaker Unified Studio.
To learn more, see Supported operators for Amazon MWAA Serverless workflows. To get started, see Serverless visual workflows in the Amazon SageMaker Unified Studio User Guide.

## 핵심 요약

요약 미지원
