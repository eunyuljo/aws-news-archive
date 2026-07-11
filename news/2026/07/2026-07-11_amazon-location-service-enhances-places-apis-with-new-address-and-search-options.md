---
title: "Amazon Location Service enhances Places APIs with new address and search options"
date: "2026-07-11"
service: "General"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-location-service-enhanced-address-search"
tags: ["General", "2026", "new-region"]
nav_exclude: true
---

# Amazon Location Service enhances Places APIs with new address and search options

**날짜:** 2026년 07월 11일
**서비스:** General
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-location-service-enhanced-address-search

## 내용

Today, Amazon Location Service announced new enhancements to its Places APIs that give developers greater control over address name formatting, multilingual address, travel-optimized POI search, and drive-through data. These capabilities span the Geocode, ReverseGeocode, GetPlace, Suggest, Autocomplete, SearchNearby, and SearchText APIs. 
&nbsp; 
Developers can now control how address component names are returned using the new AddressNamesMode parameter. By default, addresses are returned with normalized (canonical) names; developers can instead request matched names (echoing input) or administrative (government hierarchy) names. The new AddressTranslations parameter returns place name translations in 50+ languages, making it easier to build multilingual applications. A TravelMode parameter optimizes Suggest and SearchText results for users on the move, improving relevance for navigation and in-vehicle scenarios. Additionally, GetPlace, Suggest, SearchNearby, and SearchText now return a DriveThrough attribute indicating whether a place offers drive-through service — useful for logistics, food delivery, and navigation applications. The Geocode API also now supports a new Parsing.AdditionalInfo response field with additional detail about how the input address was interpreted. 
 Amazon Location Service is available in the following AWS Regions: US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific (Mumbai), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Spain), Europe (Stockholm), South America (São Paulo), and AWS GovCloud (US-West).  To get started, see the Amazon Location Service Places API reference, or learn more about Places in the Amazon Location Service Developer Guide.

## 핵심 요약

요약 미지원
