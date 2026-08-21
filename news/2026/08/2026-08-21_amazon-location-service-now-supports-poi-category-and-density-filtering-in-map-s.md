---
title: "Amazon Location Service now supports POI category and density filtering in map styles"
date: "2026-08-21"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-location-service/amazon-location-poi-categorization-density-map-styles"
tags: ["Config", "2026", "GA", "new-region"]
nav_exclude: true
---

# Amazon Location Service now supports POI category and density filtering in map styles

**날짜:** 2026년 08월 21일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-location-service/amazon-location-poi-categorization-density-map-styles

## 내용

Today, Amazon Location Service adds per-category and density-based Point of Interest (POI) filtering to its maps. Developers gain server-side control over the density of POIs and which categories of places appear on a map. Developers control this behavior through the GetStyleDescriptor API. Amazon Location Service is a fully managed service that helps developers add maps, places, routing, and tracking to applications using high-quality geospatial data. Previously, every map style rendered all POI categories, and developers who wanted to tailor POIs to their use case relied on a client-side workaround tied to internal style layer identifiers. 
With this launch, the developer provides new poi-categories and poi-density query parameters. The poi-categories parameter takes an allowlist of categories - such as Food &amp; Drink, Transit, or Accommodations—and the poi-density parameter tunes how many POIs appear on the map. Amazon Location Service returns a style descriptor that renders only the requested categories at the chosen density. Filtering is configured server-side, so maps display correctly with no additional code required on the client side, on web, mobile, and headless server-side renderers alike. A property-listing site can surface only accommodations, a logistics fleet app can show only transit and fuel, and a tourist map can highlight sights and dining.&nbsp; 
Amazon Location Service is available in the following AWS Regions: US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific (Mumbai), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Spain), Europe (Stockholm), South America (São Paulo), and AWS GovCloud (US-West). 
To get started, see Map features in the Amazon Location Service Developer Guide.

## 핵심 요약

요약 미지원
