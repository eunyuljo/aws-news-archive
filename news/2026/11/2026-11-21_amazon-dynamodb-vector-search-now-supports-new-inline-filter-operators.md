---
title: "Amazon DynamoDB vector search now supports new inline filter operators"
date: "2026-11-21"
service: "DynamoDB"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/dynamodb-vector-filters/"
tags: ["DynamoDB", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon DynamoDB vector search now supports new inline filter operators

**날짜:** 2026년 11월 21일
**서비스:** DynamoDB
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/dynamodb-vector-filters/

## 내용

Amazon DynamoDB vector search inline filters now support range comparisons, value lists, and logical operators in addition to the equality operator, so you can narrow a vector search to exactly the items you want. You can now filter on numeric ranges such as price, rating, or publish date, match an attribute against a list of values, check whether an attribute exists, and combine conditions with OR and NOT.&nbsp;Amazon DynamoDB vector indexes store vector embeddings alongside your operational data, and the SearchVectors API returns the items whose embeddings are most similar to your query vector. 
The search condition expression in a SearchVectors request now accepts the comparison operators &lt;, &lt;=, &gt;, &gt;=, and BETWEEN on Number attributes, the IN operator, the attribute_exists and attribute_not_exists functions, and the logical operators AND, OR, and NOT. DynamoDB applies the filter during the search, so every result it returns matches. For example, a retail application can return the products most similar to a shopper's query within a price range and a set of brands, and a retrieval-augmented generation application can limit results to selected document categories published after a given date. 
The new operators are available in all AWS Regions where DynamoDB vector search is available. 
To learn more, see vector search in the Amazon DynamoDB Developer Guide, or visit the Amazon DynamoDB page.

## 핵심 요약

요약 미지원
