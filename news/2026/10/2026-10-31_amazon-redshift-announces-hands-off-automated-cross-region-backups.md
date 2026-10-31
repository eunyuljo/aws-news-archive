---
title: "Amazon Redshift announces hands-off automated cross-region backups"
date: "2026-10-31"
service: "Redshift"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/redshift-automated-cross-region-backups/"
tags: ["Redshift", "2026", "new-region"]
nav_exclude: true
---

# Amazon Redshift announces hands-off automated cross-region backups

**날짜:** 2026년 10월 31일
**서비스:** Redshift
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/redshift-automated-cross-region-backups/

## 내용

Amazon Redshift announces automated cross-region snapshot copy for Amazon Redshift. You can now have your Amazon Redshift provisioned cluster or serverless workgroup automatically backed up to the target AWS region(s) you choose. The automated cross-region snapshot copy feature will automatically, always copy the most recent snapshot with no manual intervention, continuously and incrementally and ensure your cluster is backed-up to the destination region(s), giving you additional options for business continuity. 
The benefit to enabling the new automated cross-region snapshot copy feature is that you do not need to manually intervene to initiate a cross-region snapshot copy when an unplanned outage event occurs. Also, this feature takes the most recent snapshot available on your system to copy to the destination region, so you don't have to wait for the next snapshot to be taken, making it independent of your snapshot schedule on your local cluster. To configure cross-region snapshot copy, you need to enable the automated cross-region snapshot copy feature for each cluster and configure the destination region(s) to copy snapshots and how long to keep copied automated snapshots in the destination Region. You can choose the retention period for automated snapshots in the destination region. User snapshots are retained until you explicitly delete them. To restore the snapshot in the destination region, use the snapshot restore feature to a new provisioned cluster or serverless workgroup. Snapshots copied with the automated cross-region snapshot copy feature have names prefixed with `copy` in the destination region. 
This feature is available in all regions AWS Commercial and GovCloud (US) regions. 
For more details on configuration and usage see the Amazon Redshift documentation sections for cross-region snapshot copy: Amazon Redshift snapshots and backups. For details on restoring a cluster from a snapshot, see the documentation for Restoring a cluster from a snapshot. For pricing information, please review the 'Backup and storage' and 'Data transfer' sections of the Amazon Redshift pricing page.

## 핵심 요약

요약 미지원
