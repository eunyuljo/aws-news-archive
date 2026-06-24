---
title: "AWS HealthOmics now supports ephemeral storage for private workflows"
date: "2026-06-24"
service: "General"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/healthomics-scratch-storage/"
tags: ["General", "2026", "GA", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# AWS HealthOmics now supports ephemeral storage for private workflows

**날짜:** 2026년 06월 24일
**서비스:** General
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/healthomics-scratch-storage/

## 내용

AWS HealthOmics adds ephemeral storage for private workflows, giving bioinformatics workloads dedicated scratch space that delivers more consistent run performance and lower costs. Each workflow task now receives a dedicated local volume mounted at /tmp, and workflows that generate significant scratch data, such as genomic sequence alignment, BAM sorting, and variant calling,&nbsp;can experience faster run times.&nbsp;AWS HealthOmics is a HIPAA-eligible service that helps healthcare and life sciences customers accelerate scientific breakthroughs with fully managed bioinformatics workflows. 
With this launch, workflow tasks can write temporary data to their own local volume, keeping scratch I/O isolated from shared run storage that hosts the working directory. By default, each task includes 16 GiB of ephemeral storage at no additional charge. You can increase the amount of ephemeral storage allocated to individual tasks, up to a maximum of 3,072 GiB per task, using the appropriate directive in your WDL, Nextflow, or CWL workflow definition. You can enable ephemeral storage at runtime with the StartRun API.&nbsp;All ephemeral storage volumes are encrypted and deleted when a task terminates. 
You can use ephemeral storage in all AWS Regions where AWS HealthOmics is available:&nbsp;US East (N. Virginia), US West (Oregon), Europe (Frankfurt, Ireland, London), Israel (Tel Aviv), and Asia Pacific (Singapore, Seoul). To learn more about ephemeral storage, visit the AWS HealthOmics User Guide. For more information on pricing, visit AWS HealthOmics pricing.

## 핵심 요약

요약 미지원
