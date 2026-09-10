---
title: "Amazon Bedrock Managed Knowledge Base adds APIs and console support for debugging document-level access control"
date: "2026-09-10"
service: "Bedrock"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-bedrock-knowledge-base-debugging-document-access-control/"
tags: ["Bedrock", "2026"]
nav_exclude: true
---

# Amazon Bedrock Managed Knowledge Base adds APIs and console support for debugging document-level access control

**날짜:** 2026년 09월 10일
**서비스:** Bedrock
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-bedrock-knowledge-base-debugging-document-access-control/

## 내용

AWS announces the CheckIngestedDocumentAcl and GetIngestedDocumentAcl APIs for Amazon Bedrock Managed Knowledge Base, giving customers a self-service way to debug document access issues and audit document-level permissions. When a user doesn't see an expected document in retrieval results for ACL-enabled data sources, it can be difficult to determine whether the cause is an access control misconfiguration or something else entirely. These new APIs and the accompanying console experience close that gap, enabling you to quickly diagnose and resolve permission issues without opening a support case. 
CheckIngestedDocumentAcl lets you verify whether a specific user has access to a given ingested document, while GetIngestedDocumentAcl returns the full ACL attached to a document so you can audit exactly what permissions are configured and catch misconfigurations. The console also introduces a new Document Access Control section on the data source details page, where you can check access by entering a document ID and user email or retrieve a document's full ACL by document ID. Together, these capabilities give administrators the visibility they need to manage access control at scale across enterprise knowledge bases. 
To learn more, see CheckIngestedDocumentAcl and GetIngestedDocumentAcl in the Amazon Bedrock API Reference. For more information about Amazon Bedrock Managed Knowledge Base, visit the Amazon Bedrock Knowledge Bases product page.

## 핵심 요약

요약 미지원
