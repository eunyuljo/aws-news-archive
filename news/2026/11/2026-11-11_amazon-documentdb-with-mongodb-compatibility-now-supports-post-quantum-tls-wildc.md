---
title: "Amazon DocumentDB (with MongoDB compatibility) now supports post-quantum TLS, wildcard indexes, and $unionWith in version 8.0.3"
date: "2026-11-11"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-documentdb-8-0-3/"
tags: ["CloudWatch", "2026", "new-region"]
nav_exclude: true
---

# Amazon DocumentDB (with MongoDB compatibility) now supports post-quantum TLS, wildcard indexes, and $unionWith in version 8.0.3

**날짜:** 2026년 11월 11일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-documentdb-8-0-3/

## 내용

Amazon DocumentDB (with MongoDB compatibility) 8.0.3 adds hybrid post-quantum key exchange for TLS, wildcard indexes, the $unionWith aggregation stage, and new change stream events. Post-quantum TLS protects data in transit from traffic that is recorded today and decrypted later with a quantum computer. The new MongoDB APIs let you move more MongoDB workloads to Amazon DocumentDB without changing application code. 
What's new in 8.0.3: 
 
 Post-quantum TLS: TLS 1.3 connections use hybrid key exchange based on the Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) when the client supports it. Other clients keep using classical key exchange. Two new Amazon CloudWatch metrics, TLSHandshakesClassical and TLSHandshakesPostQuantum, count the handshakes of each type.  
 
 
 Wildcard indexes: index every field, or every field under a path, to query documents with dynamic schemas.  
 
 
 Aggregation: $unionWith combines results from multiple collections in one pipeline. $lookup and $graphLookup work in views, and correlated $lookup sub-pipelines accept $unionWith and $facet.  
 
 
 Change streams: dropIndex() and dropIndexes() now emit dropIndexes events.  
 
 
 Compression metrics: collStats and stats() report per-collection input bytes, output bytes, and compression ratio.  
 
Amazon DocumentDB 8.0.3 is available in all AWS Regions where Amazon DocumentDB is offered. To learn more, see the Amazon DocumentDB Developer Guide.

## 핵심 요약

요약 미지원
