---
title: "Amazon S3 Object Lock now supports variable retention with event holds"
date: "2026-09-09"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-s3-object-lock-variable-retention/"
tags: ["S3", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon S3 Object Lock now supports variable retention with event holds

**날짜:** 2026년 09월 09일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-s3-object-lock-variable-retention/

## 내용

Amazon S3 Object Lock now supports variable retention, allowing you to apply write-once-read-many (WORM) protection to objects whose required retention period starts with a future event, such as a contract closing or an audit completing. You place an event hold with a retention duration on an object and S3 protects the object while the hold is in place. When you release the hold, S3 retains the object for the duration you specified. Unlike legal holds, which end protection immediately upon removal, event holds provide WORM compliance for the required retention period after the triggering event, so you can meet event-based retention requirements without retaining data longer than your policy requires.  You can apply event holds to individual objects, configure them as a bucket default, or apply them at scale with S3 Batch Operations. New AWS IAM and bucket policy condition keys let you control who can set or release holds and enforce minimum or maximum hold durations. AWS CloudTrail logs all hold operations and S3 Inventory reports hold status across your buckets.  Event holds for S3 Object Lock are available in all AWS Regions, including China Regions, at no additional charge. To learn more, read the AWS Storage Blog post, the S3 Object Lock overview page, and the S3 documentation.&nbsp;This capability has been assessed by&nbsp;Cohasset Associates&nbsp;for use in environments subject to SEC Rule 17a-4(f), FINRA Rule 4511, and CFTC Regulation 1.31.

## 핵심 요약

요약 미지원
