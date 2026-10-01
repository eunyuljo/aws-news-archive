---
title: "AWS Deadline Cloud now supports expressions in job templates"
date: "2026-10-01"
service: "Lex"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-deadline-cloud-expressions-job-templates/"
tags: ["Lex", "2026", "new-region"]
nav_exclude: true
---

# AWS Deadline Cloud now supports expressions in job templates

**날짜:** 2026년 10월 01일
**서비스:** Lex
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-deadline-cloud-expressions-job-templates/

## 내용

AWS Deadline Cloud now supports flexible expressions and rich parameter types in job templates, giving customers a cleaner, more powerful way to fit the service to existing production pipelines. Deadline Cloud is a fully managed service that helps teams run compute-intensive workloads in the cloud for visual effects, animation, product design, simulation, and gaming.
Customers can now express pipeline logic directly in their job templates. This includes expressions such as arithmetic, conditionals, string and path operations, and list comprehensions, all in a familiar Python-style syntax. Customers can use this to split a frame range into per-task frames, derive an output path from the scene name, or toggle an optional flag directly within job templates themselves, making it easier to automate bespoke pipeline operations. New boolean, list, and frame-range parameter types match how pipelines already describe work. For example, a checkbox can add a --gpu flag and its matching host requirement when set, and a list of cameras can become a step's task range. Expressions are type-checked at submission, and their evaluation is deterministic, meaning that job execution behaves predictably every time.
These capabilities come from the new EXPR extension to Open Job Description, the open specification Deadline Cloud uses for job templates, and are available in all AWS Regions where AWS Deadline Cloud is supported.
To get started, visit the Deadline Cloud developer guide.

## 핵심 요약

요약 미지원
