---
title: "Amazon RDS now adds full snapshot size information to the Console and API"
date: "2026-09-30"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-rds-full-snapshot-size-available/"
tags: ["RDS", "2026", "new-region"]
nav_exclude: true
---

# Amazon RDS now adds full snapshot size information to the Console and API

**날짜:** 2026년 09월 30일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-rds-full-snapshot-size-available/

## 내용

Amazon RDS now displays the full snapshot size for RDS Snapshots. With this enhancement, customers can now retrieve full snapshot sizes programmatically through the DescribeDBSnapshots API using the new field, ‘FullSnapshotSizeInBytes’. They can also view this on the console with the ‘Full Snapshot Size’ column.&nbsp; &nbsp;
Amazon RDS snapshots are incremental. This means that if you take multiple snapshots of a volume over time, each snapshot only stores the new or modified blocks while maintaining references to unchanged blocks from previous snapshots. The ‘FullSnapshotSizeInBytes’ field shows you the total size of all blocks that make up a snapshot, including both the blocks stored directly in that snapshot and all blocks referenced from previous snapshots. For instance, if you have a 100 GB database volume with 50 GB of data, the ‘full snapshot size’ would show 50 GB regardless of whether it's the first snapshot or a subsequent one. Please note that this is different from the incremental snapshot size, which only refers to the size of newly changed blocks stored in that specific snapshot.
Full snapshot size is available all Amazon RDS database instances in all commercial AWS Regions. You can start using it today through the Amazon RDS Management Console, the AWS Command Line Interface (CLI), or the AWS SDKs. To learn more, see&nbsp;the Amazon RDS User Guide.

## 핵심 요약

요약 미지원
