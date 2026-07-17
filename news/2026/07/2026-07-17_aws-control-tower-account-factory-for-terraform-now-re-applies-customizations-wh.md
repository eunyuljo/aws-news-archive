---
title: "AWS Control Tower Account Factory for Terraform now re-applies customizations when accounts move between OUs"
date: "2026-07-17"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-control-tower-account/"
tags: ["Config", "2026", "new-region", "performance", "security", "ai-ml"]
nav_exclude: true
---

# AWS Control Tower Account Factory for Terraform now re-applies customizations when accounts move between OUs

**날짜:** 2026년 07월 17일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-control-tower-account/

## 내용

AWS Control Tower Account Factory for Terraform (AFT) can now automatically re-apply an account's customizations when that account moves to a different Organizational Unit (OU). Previously, moving an enrolled account between OUs required manually triggering customization re-application, creating operational overhead and risk of configuration drift. With this capability, you can opt in to automatic re-application in your AFT deployment, so accounts stay consistent with their OU-specific configuration as soon as they're moved. 
To enable this capability, set aft_customization_triggers = ["account_move"] in your AFT configuration. The re-application workflow skips the bootstrap and provisioning phases, running only global and account-level customizations for faster execution. Individual accounts can be excluded from this behavior by setting account_skip_customization_triggers = "true", giving teams precise control over which accounts participate in automated re-application. 
This release also includes additional improvements: support for custom Terraform Cloud and Enterprise workspace naming variables, tighter access controls on the AFT logging bucket, and improved scaling for large-scale AWS Enterprise Support enrollment. Organizations enforcing compliance or security baselines tied to OU membership will benefit most from these combined enhancements. 
This capability is available today across all AWS regions where AWS Control Tower Account Factory for Terraform is offered.&nbsp;To learn more about enabling automatic customization re-application and upgrading to the latest AFT release, visit the AFT documentation and review the AFT release notes on GitHub.

## 핵심 요약

요약 미지원
