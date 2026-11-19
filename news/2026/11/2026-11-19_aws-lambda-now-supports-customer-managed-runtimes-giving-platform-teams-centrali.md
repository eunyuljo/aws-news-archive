---
title: "AWS Lambda now supports customer-managed runtimes, giving platform teams centralized control over runtime contents and updates"
date: "2026-11-19"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-customer-managed-runtimes/"
tags: ["Lambda", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# AWS Lambda now supports customer-managed runtimes, giving platform teams centralized control over runtime contents and updates

**날짜:** 2026년 11월 19일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-customer-managed-runtimes/

## 내용

AWS Lambda now supports customer-managed runtimes for Lambda Event Functions (formerly Lambda functions). Customer-managed runtimes are a standalone resource type that fully decouples runtime management from function deployment. Platform teams gain centralized control over the runtime contents,&nbsp;updates, access, and lifecycle, including the ability to push updates to shared components without per-function redeployments. Application teams consume the runtime from their functions in the same way as a Lambda-managed runtime, preserving their familiar developer experience. 
Many organizations require every function to include approved components, such as SDKs, certificates, and security or monitoring tools. Previously, sharing these through Lambda Layers or container images meant redeploying every function to pick up a change. With customer-managed runtimes, platform teams manage these components in a central runtime, packaged as OCI container images in Amazon ECR and compatible with existing Docker and CI/CD tooling. Functions pick up updates automatically as Lambda recycles execution environments, so there's no need to redeploy each function or coordinate rollouts. Updates can be scheduled and staged to match change control policies, with centralized health metrics and rapid rollback. With this launch, the existing custom runtimes feature is renamed "bring your own language." 
AWS Lambda customer-managed runtimes is now generally available in all commercial AWS Regions. There is no additional charge for customer-managed runtimes; functions are billed at standard Lambda rates and standard Amazon ECR pricing applies to runtime images. 
To get started, build your runtime as a container image in Amazon ECR, starting from a Lambda base image or from scratch, then create a runtime, a version, and an alias. Application teams reference the runtime alias in their function configuration and keep deploying their code as .zip files. Share runtimes with other accounts or an AWS Organization by using a resource-based policy. You can create and manage customer-managed runtimes using the AWS CLI, AWS SDKs, CloudFormation, or AWS CDK. To learn more, see the customer-managed runtimes documentation and launch blog post.

## 핵심 요약

요약 미지원
