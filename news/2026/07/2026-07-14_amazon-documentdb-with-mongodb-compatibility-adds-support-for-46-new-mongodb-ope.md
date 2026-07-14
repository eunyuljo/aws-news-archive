---
title: "Amazon DocumentDB (with MongoDB compatibility) adds support for 46 new MongoDB operators in version 8.0.1"
date: "2026-07-14"
service: "DocumentDB"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-documentdb-mongodb-8-0-1-mongo-api"
tags: ["DocumentDB", "2026", "new-region"]
nav_exclude: true
---

# Amazon DocumentDB (with MongoDB compatibility) adds support for 46 new MongoDB operators in version 8.0.1

**날짜:** 2026년 07월 14일
**서비스:** DocumentDB
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-documentdb-mongodb-8-0-1-mongo-api

## 내용

Amazon DocumentDB (with MongoDB compatibility) now supports 46 additional MongoDB aggregation operators and cursor methods starting from minor version 8.0.1. This release significantly expands query API compatibility, making it easier to migrate MongoDB workloads to Amazon DocumentDB without application code changes. 
New capabilities span seven categories: 
 
 Accumulators (13): $top, $topN, $bottom, $bottomN, $firstN, $lastN, $maxN, $minN, $count, $median, $percentile, $stdDevPop, $stdDevSamp  
 
 
 Trigonometry (15): $sin, $cos, $tan, $asin, $acos, $atan, $atan2, $sinh, $cosh, $tanh, $asinh, $acosh, $atanh, $degreesToRadians, $radiansToDegrees&nbsp;  
 
 
 Bitwise aggregation (4): $bitAnd, $bitOr, $bitXor, $bitNot  
 
 
 Arithmetic (3): $round, $trunc, $sigmoid  
 
 
 Data size and type (4): $binarySize, $bsonSize, $isNumber, $toUUID  
 
 
 Timestamp (2): $tsIncrement, $tsSecond&nbsp;  
 
 
 Stages and other (5): $sortByCount, $listSearchIndexes, $sampleRate, cursor.min(), cursor.max()  
 
These operators are available starting from Amazon DocumentDB 8.0.1 in all regions where Amazon DocumentDB is available. To learn more, see Supported MongoDB APIs, operations, and data types and Amazon DocumentDB release notes.

## 핵심 요약

요약 미지원
