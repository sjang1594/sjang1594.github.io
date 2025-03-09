---
title: Image Cache & Loaders
layout: post
category: study
tags: [swift, mobile dev]
published: true
---

## Apple Invites App

### Current State of the project.
I'm currently doing the project from the BootCamp. The goal is to make a member introduction app. Then the motivation was from the `Apple Invites` app. As I delved into optimizing the performance of our app, particularly focusing on image loading times, I realized the importance of implementing an effective image caching strategy. The motivation stemmed from observing how apps like Apple Invites handle image loading efficiently. Initially, I noticed that fetching images from the internet could lead to slower loading times, especially if the same images were loaded multiple times. This led me to explore how caching could improve the user experience by reducing the need for repeated network requests.

Caching images is a crucial technique in mobile app development, as it significantly enhances app performance by reducing load times and conserving bandwidth. By storing images locally on the device, either in memory or on disk, apps can quickly retrieve them instead of fetching them from the internet every time they are needed. This approach not only speeds up image rendering but also reduces data usage, which is beneficial for both users and developers in terms of cost savings and improved user satisfaction.

In iOS, there are several ways to implement image caching, including using built-in classes like NSCache for memory caching and URLCache for both memory and disk caching. Additionally, third-party libraries such as Kingfisher provide robust caching capabilities with features like asynchronous image loading and customizable cache behavior.

For the product, I am not going to post about the app, but I will show you the example of how to chache image on very simple app.

### How to cache the image in iOS.

### Resource
