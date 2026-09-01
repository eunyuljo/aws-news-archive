---
title: "AWS Elastic Beanstalk now supports Active Directory domain join for Windows Server environments"
date: "2026-09-01"
service: "ElasticBeanstalk"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/elastic-beanstalk-active-directory-domain-join/"
tags: ["ElasticBeanstalk", "2026", "GA", "new-region"]
nav_exclude: true
---

# AWS Elastic Beanstalk now supports Active Directory domain join for Windows Server environments

**날짜:** 2026년 09월 01일
**서비스:** ElasticBeanstalk
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/elastic-beanstalk-active-directory-domain-join/

## 내용

AWS Elastic Beanstalk now automatically joins the Windows Server instances in your environment to an Active Directory domain that you manage with AWS Directory Service. Previously, running domain-joined Windows workloads on Elastic Beanstalk required custom join scripts that you had to maintain. With this launch, you set a few configuration options and every instance in the environment — including instances launched later by auto scaling — joins the domain at boot, before your application deploys, with no custom scripts. 
Domain-joined instances can use Windows-integrated authentication, apply group policy, and reach domain resources such as file shares and SQL Server databases that use Windows authentication. You can place instances in an organizational unit that you want to target with a group policy, and each instance takes a predictable computer name derived from its instance ID. The feature is resilient by design: if an instance can't join the domain, your deployment still completes, and the environment reports the problem, so a join failure never blocks a deployment. 
Active Directory domain join is available on Windows Server platform versions released on or after August 18, 2026, in all AWS Commercial Regions and the AWS GovCloud (US) Regions where Elastic Beanstalk is available. For a complete list of supported Regions, see AWS Regions. 
To learn more, see Joining instances to an Active Directory domain in the AWS Elastic Beanstalk Developer Guide. To learn more about Elastic Beanstalk, visit the AWS Elastic Beanstalk product page.

## 핵심 요약

요약 미지원
