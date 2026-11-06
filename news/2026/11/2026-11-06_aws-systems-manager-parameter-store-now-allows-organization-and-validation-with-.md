---
title: "﻿﻿AWS Systems Manager Parameter Store now allows organization and validation with built-in data types"
date: "2026-11-06"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-ssm-parameter-store-allows-organization-validation-with-new-data-types/"
tags: ["Config", "2026", "new-region"]
nav_exclude: true
---

# ﻿﻿AWS Systems Manager Parameter Store now allows organization and validation with built-in data types

**날짜:** 2026년 11월 06일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-ssm-parameter-store-allows-organization-validation-with-new-data-types/

## 내용

AWS Systems Manager Parameter Store now supports 13 new parameter data types that automatically validate parameter values when you create or update a parameter. With built-in validation, you can stop malformed configuration values, such as an invalid IP address, AWS account ID, or JSON document, before your applications read them, without writing your own validation logic.&nbsp;These types allow you to better organize your parameters across your workloads. You can filter by type when calling the DescribeParameters API or when browsing parameters in the Parameter Store console.  The following data types are available for both standard and advanced parameters:&nbsp; aws:region, aws:account:id, boolean, integer, float, binary, hostname, email, ipv4-address, and ipv6-address. Three more data types, url, json, and jsonc, are available for advanced parameters. Parameter Store checks the value when you call PutParameter and rejects any value that doesn't match its data type. New data types work with String and SecureString parameters, and several also support StringList parameters, where each item in the list is validated. You can combine a data type with an AllowedPattern for additional constraints, and you can change the data type of an existing text parameter.

## 핵심 요약

요약 미지원
