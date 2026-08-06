---
title: "AWS HealthOmics now supports task-level timeout for WDL workflows"
date: "2026-08-06"
service: "General"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-healthomics-wdl-task-level-timeout/"
tags: ["General", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# AWS HealthOmics now supports task-level timeout for WDL workflows

**날짜:** 2026년 08월 06일
**서비스:** General
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-healthomics-wdl-task-level-timeout/

## 내용

AWS HealthOmics now supports task-level timeout for Workflow Description Language (WDL) workflows, enabling you to set maximum execution duration for individual tasks. AWS HealthOmics is a HIPAA-eligible service that helps healthcare and life sciences customers accelerate scientific breakthroughs at scale with fully managed bioinformatics workflows.&nbsp; 
With task-level timeout, you can define time bounds on individual WDL tasks to control costs and enable automated error recovery. HealthOmics provides the omicsTimeout runtime attribute that you can add to any task's runtime section to specify the maximum duration a task is allowed to run. When a task exceeds the specified duration, HealthOmics stops the task and sets the task and run statuses to failed. The omicsTimeout attribute accepts duration values with standard time units (such as 90s, 2h, 1d). This prevents tasks from consuming resources and helps you set cost guardrails during workflow development.&nbsp; 
Task-level timeout for WDL workflows is available in all supported AWS HealthOmics Regions: US East (N. Virginia, Ohio), US West (Oregon), Europe (Frankfurt, Ireland, London), Israel (Tel Aviv), and Asia Pacific (Seoul, Singapore, Tokyo). To learn more, visit the WDL workflow definition specifics documentation.&nbsp;

## 핵심 요약

요약 미지원
