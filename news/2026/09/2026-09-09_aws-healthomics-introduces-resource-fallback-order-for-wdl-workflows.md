---
title: "AWS HealthOmics introduces resource fallback order for WDL workflows"
date: "2026-09-09"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-healthomics-resourcefallback-wdl/"
tags: ["Config", "2026", "new-region"]
nav_exclude: true
---

# AWS HealthOmics introduces resource fallback order for WDL workflows

**날짜:** 2026년 09월 09일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-healthomics-resourcefallback-wdl/

## 내용

Today, AWS HealthOmics introduces the resource fallback directive, enabling you to define an ordered list of preferred accelerator types, including an option to fallback to CPU instances, for tasks in your Workflow Description Language (WDL) workflows. Researchers and bioinformaticians can use this directive to reduce time spent diagnosing and resubmitting runs due to accelerator constraints and keep production workflows running. AWS HealthOmics is a HIPAA-eligible service that helps healthcare and life sciences customers accelerate scientific breakthroughs at scale with fully managed bioinformatics workflows.&nbsp; 
With resource fallback, you can prioritize your preferred accelerator for your task. When your preferred accelerator is unavailable, HealthOmics automatically moves through your specified alternatives in the fallback without resubmission. Each accelerator profile has a configurable timeout, giving you control over how long HealthOmics searches for that accelerator before moving to the next. Shorter timeouts help you move quickly through the fallback order, while longer timeouts increase the probability of reserving your preferred accelerator. You can also include a CPU profile as a final fallback to increase the likelihood of your task reserving an instance.&nbsp; 
You can now use resource fallback for WDL workflows in all AWS HealthOmics Regions: US East (N. Virginia, Ohio), US West (Oregon), Europe (Frankfurt, Ireland, London), Israel (Tel Aviv), and Asia Pacific (Seoul, Singapore, Tokyo). To learn more, visit the advanced resource configuration documentation.&nbsp;

## 핵심 요약

요약 미지원
