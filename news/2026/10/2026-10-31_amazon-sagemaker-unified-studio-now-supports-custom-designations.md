---
title: "Amazon SageMaker Unified Studio now supports custom designations"
date: "2026-10-31"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/sagemaker-custom-designations/"
tags: ["RDS", "2026", "new-region"]
nav_exclude: true
---

# Amazon SageMaker Unified Studio now supports custom designations

**날짜:** 2026년 10월 31일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/sagemaker-custom-designations/

## 내용

Amazon SageMaker Unified Studio now supports custom designations, named permission sets that control what actions individual project members can perform. Previously, project members could only be assigned Owner or Contributor designations, which provided nearly identical permissions. With custom designations, administrators define permission sets that align with their organization's personas and assign them to project members. Designations govern all actions within a project, providing administrators with a single permission model for separation of duties.
Administrators create designations in the SageMaker Unified Studio administration portal by selecting permissions grouped into categories such as Catalog, Subscriptions, Connections, Notebooks, and Data Agent. For example, a "Data Steward" designation might include permissions to approve subscription requests and publish assets, while an "Analyst" designation is limited to querying data and running notebooks. Each designation is defined at the domain level and assigned across any project in that domain. When a member performs an action, SageMaker Unified Studio evaluates their assigned designation and permits or denies the request. Data engineers, stewards, analysts, and automated pipelines can now work within the same project with differentiated access, removing the need to create separate projects to isolate permissions. Every domain includes two managed designations, Owner and Contributor, and administrators can create up to 10 additional designations.
This feature is available in all AWS Regions where Amazon SageMaker Unified Studio is available. To learn more, visit the Designations documentation.

## 핵심 요약

요약 미지원
