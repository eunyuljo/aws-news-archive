---
title: "Announcing Blockchain Snapshots on AWS for node bootstrapping"
date: "2026-10-15"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/blockchain-snapshots-node-bootstrapping/"
tags: ["S3", "2026", "new-region", "performance"]
nav_exclude: true
---

# Announcing Blockchain Snapshots on AWS for node bootstrapping

**날짜:** 2026년 10월 15일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/blockchain-snapshots-node-bootstrapping/

## 내용

For blockchain node operators running Ethereum or Solana, AWS is announcing Blockchain Snapshots on AWS, an initiative that publishes pre-synced public blockchain node chain data in Amazon Simple Storage Service (Amazon S3) so you can bootstrap a node from a snapshot instead of peer-to-peer syncing from the network. These&nbsp;snapshots are hosted on Amazon S3 within AWS infrastructure, enabling customers running nodes on AWS benefit from reduced latency and optimized data transfer. Blockchain Snapshots on AWS republishes each network's authoritative snapshot in a format optimized for parallel extraction across multiple cores, reducing setup time, that an Amazon Elastic Compute Cloud (Amazon EC2) instance can use.
Snapshots cover Ethereum and Solana, are available at no charge, and refresh on the same cadence as the upstream provider. Use them to add capacity to a remote procedure call (RPC) fleet, recover a failed node, or re-sync a corrupted database.
You can use Blockchain Snapshots on AWS in the following AWS Regions: US East (N. Virginia), Europe (Ireland), and Asia Pacific (Tokyo). Access requires an Amazon EC2 instance in the same Region with an Amazon S3 gateway VPC endpoint.
To get started, visit the Blockchain Snapshots on AWS documentation to access setup instructions and download the latest snapshots.

## 핵심 요약

요약 미지원
