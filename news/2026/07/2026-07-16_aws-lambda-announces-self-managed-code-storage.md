---
title: "AWS Lambda announces self-managed code storage"
date: "2026-07-16"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/lambda-self-managed-code-storage/"
tags: ["Lambda", "2026", "new-region"]
nav_exclude: true
---

# AWS Lambda announces self-managed code storage

**날짜:** 2026년 07월 16일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/lambda-self-managed-code-storage/

## 내용

AWS Lambda now supports self-managed Amazon S3 buckets for code storage,&nbsp;enabling you to reference source code directly from your own S3 buckets without Lambda creating intermediate copies. This eliminates code storage limits and reduces function activation time after function creates and updates by removing the copy step. 
AWS Lambda is a serverless compute service that runs your code without requiring you to manage servers. Customers who deploy many functions and additional code as Lambda layers often need more than 75GB of code storage per Region, requiring support tickets to increase this quota. Previously, Lambda always copied your deployment package to Lambda-managed storage during function and layer creation, counting against this limit. Now, with self-managed code storage, Lambda references your code directly in your Amazon S3 bucket without creating a copy, so you can store as much function and layer code as your bucket allows. You maintain a single source of truth for your deployment packages in your own account. No additional Lambda charges apply for self-managed storage; you only pay for standard Amazon S3 storage and, where applicable, cross-Region data transfer rates. In addition,&nbsp;Lambda has increased the default limit for Lambda-managed code storage from 75GB to 300GB per Region per account. 
Self-managed Amazon S3 code storage is available in all commercial AWS Regions. 
To get started, set the `S3ObjectStorageMode` parameter to `REFERENCE` when creating or updating functions and layers through the AWS CLI, AWS CloudFormation, AWS SAM, or AWS SDKs. You must grant the Lambda service principal `s3:GetObject` and `s3:GetObjectVersion` permissions on your S3 bucket. You can also update a function to use self-managed code storage via the Lambda Console. To learn more, visit the AWS Lambda Developer Guide.

## 핵심 요약

요약 미지원
