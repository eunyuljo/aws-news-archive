---
title: "Amazon ElastiCache Global Datastore now supports tagging and tag-based access control"
date: "2026-09-25"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-elasticache-global-datastore-tagging/"
tags: ["IAM", "2026", "GA", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon ElastiCache Global Datastore now supports tagging and tag-based access control

**날짜:** 2026년 09월 25일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-elasticache-global-datastore-tagging/

## 내용

Amazon ElastiCache now supports resource tagging and tag-based access control (TBAC) for Global Datastore. Previously, ElastiCache supported tagging on all resources except Global Datastore, which prevented customers from applying a single, consistent permission and cost-allocation model across their ElastiCache fleet.
With this launch, you can use AddTagsToResource, RemoveTagsFromResource, and ListTagsForResource on a Global Datastore, and reference those tags as conditions in IAM policies and Service Control Policies (SCPs) to grant permissions based on tag attributes rather than enumerating individual resources. Tag changes on a Global Datastore propagate automatically to every Region it spans, so access-control and cost-allocation policies stay consistent without per-Region operations.
There is no additional cost for this feature, and no change to how you create or manage Global Datastores. This feature is available in all AWS Regions where ElastiCache Global Datastore is available. To learn more, see Tagging your ElastiCache resources and Using condition keys with ElastiCache.&nbsp;

## 핵심 요약

요약 미지원
