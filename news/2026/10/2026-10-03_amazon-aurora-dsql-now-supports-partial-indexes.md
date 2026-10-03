---
title: "Amazon Aurora DSQL now supports partial indexes"
date: "2026-10-03"
service: "Aurora"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aurora-dsql-partial-indexes/"
tags: ["Aurora", "2026", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Amazon Aurora DSQL now supports partial indexes

**날짜:** 2026년 10월 03일
**서비스:** Aurora
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aurora-dsql-partial-indexes/

## 내용

Amazon Aurora DSQL now lets you build an index over a specific subset of a table, storing only qualifying rows rather than every row in the entire table, which improves query performance and lowers index storage cost.
Many tables hold a small working set alongside a much larger history, such as open orders among years of completed ones. Add a WHERE clause to CREATE INDEX to index just that working set. The index stays small as the table grows, and queries that target those rows read less data. Aurora DSQL uses a partial index for any query whose filter falls within the index's condition.
Partial indexes are available in all AWS Regions where Aurora DSQL is available. To learn more, see CREATE INDEX in the Aurora DSQL User Guide.

## 핵심 요약

요약 미지원
