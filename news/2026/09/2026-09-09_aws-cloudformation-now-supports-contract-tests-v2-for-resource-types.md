---
title: "AWS CloudFormation now supports contract tests v2 for resource types"
date: "2026-09-09"
service: "CloudFormation"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-cloudformation-contract-tests-v2-resource-types/"
tags: ["CloudFormation", "2026", "new-region"]
nav_exclude: true
---

# AWS CloudFormation now supports contract tests v2 for resource types

**날짜:** 2026년 09월 09일
**서비스:** CloudFormation
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-cloudformation-contract-tests-v2-resource-types/

## 내용

AWS CloudFormation now supports contract tests v2, available through the --v2 flag of the cfn test command in the CloudFormation CLI. Previously, the contract test suite covered only basic scenarios around the CRUD handlers. Contract tests v2 adds deeper test scenarios that exercise your resource type implementation across each handler operation. All new resource types can run contract tests v2 through the test-type API during registry submission, and Java-based resource types can also run them locally with cfn test --v2, requiring only Docker and a built handler package. 
Contract tests v2 introduces live-state verification that confirms actual resource state matches the requested state after create, update, and delete operations. Developers also benefit from schema backward-compatibility checks, test input linting that flags hardcoded Regions, account IDs, and partitions, and detailed HTML and JUnit XML reports for local contract test execution. These improvements significantly reduce iteration cycles by surfacing issues before registry submission. 
Contract tests v2 is available in all AWS Regions where AWS CloudFormation is available. To learn more, visit the AWS CloudFormation contract tests documentation and the AWS CloudFormation product page.

## 핵심 요약

요약 미지원
