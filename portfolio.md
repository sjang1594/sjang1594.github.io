---
layout: list
title: Portfolio
permalink: /portfolio/
sidebar: true
order: 1
description: >
---

* * *
<center>
<span style=
"font-size:150%;
font-weight:bold">
Seungho Jang (장승호)
</span>
</center>

<center>Major : Computer Science & Electrical Engineering</center>

<center>University of Missouri - Saint Louis</center>

<center>32-14, Samseong-ro 75-gil, Gangnam-gu, Seoul</center>

## Personal Data
---
> 1994.10.12  Republic of Korea, Seoul (대한민국)

> Contact(연락처): sjang1594@gmail.com

> Github : <a href="https://github.com/sjang1594">https://github.com/sjang1594</a>

## Education
---
> May.2013 ~ May.2015 : University of Minnesota - Twin City
>
> B.Bm.E. in Biomedical Engineering

> Jan.2016 ~ Dec.2018 : Washington University in St. Louis.
>
> B.S.EE in Electrical Engineering (Emphasis on Signal Processing & Radar System)
> Minor in Computer Science and Mathematics

> Jan.2020 ~ May.2021 : University of Missouri - Saint Louis
>
> M.S in Computer Science (Emphasis on Deep Learning & Computer Vision)

## Work Experience
---
> Aug.2017 ~ Aug.2019 : Washington University in St. Louis
> Teaching Assistant in EE(Electrical Engineering)
> 1. Provided supplemental educational services for undergraduate students studying Signal & System / Engineering Mathematics Course.

> Aug.2018 ~ Dec.2018 : University of Missouri - Saint Louis
> Math & Engineer Tutor
> 1. Tutored for Calculus 1 through Calculus 3, Different Equation, Linear Algebra, and Engineering Statistics.

> Dec.2019 ~ Aug.2021 : University of Missouri - Saint Louis
> Graduate Teaching & Researching Assistant
> 1. Teaching CS 1250 and CS2250 for a year. Developed and delivered hands-on C++ programming labs covering OOP, memory management, STL, and graph algorithms.
> 2. Research the Root Detection []() for Computer Vision Application.

> Oct.2021 ~ Dec.2024 : MORAI Inc.
> Software Engineer - Map Team
> 1. implemented the multi-instancing capability to load and edit multiple HDMaps (MGeo) sumultaneously.
> 2. developed the undo/redo functionality using the command pattern for HDMaps editing operation (e.g., road/traffic Sign/Signals creation/deletion, junction modification)
> 3. created pre-computation algorithm for road intersection in static maps.
> 4. created unit tests by using PyTest to validate intersection accuracy (automated counting and position), and integrated tests into Jenkins CI/CD pipeline to ensure maps integrity checks.

> Software Engineer - Test Automation Team.
> 1. Developed a comprehensive Scenario Runner Application from scratch, implementing the ASAM OpenSCENARIO standards:
> - created functionality to load, edit, and save OpenSCNEARIO files, adhering to the standard's defined elements and attributes, and implemented a user interface for scenario editing for each elements and attributes, and batch simulation management.
> - implemented various OpenSCNEARIO actions, including TrafficSpawnAction and custom PedestrianSpawnAction.
> - integrated gRPC protocol for communication with the simulator; developed an adaptor class to handle responses/requests, with the Scenario Runner client performing all conditions and action evaluations for improved maintainability.
> - optimize collision detection using an Oriented Bounding Box (OBB) and Separating Axis Theorem.
> - architected scalable batch simulation functionality with Python API's for simulation controls (start, skip, stop, load map, simulation time, etc.)
> - provide ongoing support and education to key clients (A2Z, ROKA, ETRI, SureSoft, Hyundai), including bug fixes, feature development based on client feedback , and comprehensive documentation.
> - ported existing features of Scenario Runner to Unreal Editor 5; migrate core features and system from previous Python scripts to Unreal Engine 5.

> Software & Graphics Engineer - Virtual Data Team
> 1. Led a major code refactoring, considering disparate codebases across projects and improving system performance.
> 2. Implemented static analysis in GitLab CI/CD pipeline with Unreal Engine 5 Plugin based on Google C++ and Unreal Engine Coding Standards, enhancing overall code quality and maintenance.
> 3. Developed a shader-based radar simulation using shader programming (.usf / HLSL) in Unreal Engine.
> - utilized low-level radar parameters; the number of chirps, samples, receive antenna, and antenna pattern to simulate radar returns based on those parameters. 
> - created Python scripts to process radar data; received low-level output data(2D samples/chirps) from ROS, and generate range-doppler maps.
> 4. Created the Bounding Box Labeler with the following features in Unreal Engine 5 with advanced features:
> - implemented JSON file output for all object types; vehicles, vehicle parts, pedestrians with animation, and obstacles.
> - supported multiple coordinate system for use cases (Camera, LiDAR, vehicle, and ENU).
> - developed flexible object's bounding box representations; 8-corner point-based and center point-based representation with rotation model (quternion & euler angles).
> - provided user-selectable options for output representation by using Unreal Slate, allwoing customization of coordinate systems and boundign box format.
> 5. Developed Coordinate Converter Plugin for Unreal Engine 5.
> - implemented bidirectional transformation between Unreal Engine's left-handed and right-handed system (NED, ENU, AER, Spherical) with unit tests, enabling cross-team compatibility and project integration.

## Research Interests
---
* 3D Computer Vision
    + XR / VR
* Computer Grpahics
    + DirectX11/12
    + Vulkan
    + Visual Effect
    + Shader Programming 
* Parallel Processing 
    + CUDA
* Radar Simulation

## Projects
---
* HYUNDAI UAM: Radar Point Cloud Visualization in Unreal Engine 5.
- applied Gaussian Random Distribution to generate realistic returns and utilizing the raycasting method to exclusively capture aerial objects, improving point cloud fidelity and target isolation.
- collaborated with Graphics Team to validate and refine object-specific collision models focusing on aircraft. 

* Samsung DataGen:
2. Enhanced LiDAR Simulation with Motion Distortion.
- developed a post-processing technique to apply motion distortion to MORAI Simulator's LiDAR output, implementing coordinate transformation and spherical linear interpolation(SLERP) for rotation modeling, and integrated distortion effects into the pipeline.

* ROKA (Republic of Korea Army):
- Implemented a flexible architecture for Scenario Runner, incorporating a default mapping system for offline loading of vehicles, pedestrians, and miscellaneous objects, while maintaining compatibility with existing RestAPI-based retrieval, ensuring operation across security environments.

## Personal Projects
---
* **RFID Door Lock - JEC2000**  

[RFID Presentation](https://docs.google.com/presentation/d/1wkD3lbgjXfVELOVWqM9DJZEWWYUbUHfj-QLO51gSbvI/edit#slide=id.g47eb0409b1_1_0)

* **XYZ - Camera Controller - Senior Project**

[XYZ Camera Controller](https://docs.google.com/presentation/d/11eDE-hOqh-xyiRGRCgn5WrCFYZxG8LSMyEVw1EaX5zw/edit#slide=id.g489ac9f632_0_10)

* **BCI(Brain Computing Interface) Data Augmentation & Filtering**

`Summer Research Program : Washington University in St. Louis - in ShiNung Ching Lab (Undergrads)`

Conic Method : Recording & Filtering the brain signals(inputs) to the system using the signal processing techniques

* **Ambient Care System with Amazon Alexa**

1. Build the Raw Activity Data Schema/Data Analytics
2. Build LSTM Deep Learning Model for Sentimental Analysis

[Project Repo](https://github.com/sntrenter/FA2020GroupProject) and [Presentation Video](https://vimeo.com/490250102/2e52524b6a)


* **Operating System/System Programming - CS4760**

`Environment: Linux Terminal`, `Language : C`

Learning Linux Environment and Resource/Process/Memory Managements written in C.

1. DepthFirst - ls Command
2. Forked Subset Sum Problem
3. Semaphores
4. OS Process Scheduler
5. OS Resource Management
6. OS Memory Management

The repository for this private for a reason. Contact me if you want the source codes.

* **Udacity - Robotic Software Engineering**

`Environment : Ubuntu 18.04`,`ROS Melodic`
`Language : C++`

1. [Build a Simulation World with Gazebo](https://github.com/sjang1594/RoboND-Udacity/tree/master/Robotics-UD-MyWorld)
2. [Go Chase it](https://github.com/sjang1594/RoboND-Udacity/tree/master/Robotics-UD-GoChaseIt)
3. [MapMyWorld](https://github.com/sjang1594/RoboND-Udacity/tree/master/Robotics-UD-MapMyWorld)
4. [WhereAmI](https://github.com/sjang1594/RoboND-Udacity/tree/master/Robotics-UD-WhereAmI)
5. [HomeServiceRobot](https://github.com/sjang1594/RoboND-Udacity/tree/master/Robotics-UD-HomeServiceRobot)

* **Image Processing / Computer Vision Projects**

`Environment : Windows 10`,`Visual Studio 2019`,`OpenCV4 & CUDA 11.3.`
`Language : C++`

1. [Poter Duff Operation](https://github.com/sjang1594/UMSL/tree/master/CS6420/project1)
2. [Image Registeration](https://github.com/sjang1594/UMSL/tree/master/CS6420/project2)
3. [Frequency Filtering (Denoise the Periodic Noise)](https://github.com/sjang1594/UMSL/tree/master/CS6420/project3)
4. [Image Segmentation using K-mean (Detecting the USA map)](https://github.com/sjang1594/UMSL/tree/master/CS6420/project4)
5. [Image Segmentation using SLIC Algorithms(Simple Linear Iterative Clustering)](https://github.com/sjang1594/UMSL/tree/master/CS6420/project5 )
6. [Harry Potter Movie Character Face Recognition](https://github.com/sjang1594/UMSL/blob/master/CS5390/DL_FINAL_REPORT.pdf)

* **Udacity - C++ (Not completed)**

`Environment : Ubuntu 20.04`,`Visual Studio Code`,`CMAKE`
`Language : C++`

1. [Route Planning Project](https://github.com/sjang1594/CppND_Udacity/tree/master/CppND-Route-Planning-Project)
2. [System Monitor Project](https://github.com/sjang1594/CppND_Udacity/tree/master/CppND-System-Monitor)

* **Root Analysis (In progress for publication)**

Build the software system and algorithm to detect the root system from the given the root imageries.

* **Udacity - Computer Vision (Completed)**

`Environment : Jupyter Notebook`,`OpenCV4`,`Framework: Pytorch`
`Language : Python`

1. [Facial Keypoints - Eye & Face Recognition](https://github.com/sjang1594/cvnn-udacity/tree/master/P1-Facial_KeyPoints)
2. [Image Captioning](https://github.com/sjang1594/cvnn-udacity/tree/master/P2-Image_Captioning) 
3. [Landmark Detection Tracking(SLAM)](https://github.com/sjang1594/cvnn-udacity/tree/master/P3-Landmark%20Detection_Tracking(SLAM))

## Skills and Certification
---
- Language : C / C++ / C#, Java, Python, JavaScript
- Technologies: Git, OpenCV, Open3D, CUDA, DirectX11, DirectX12, Vulkan, HLSL, Unreal Engine, Unity, PyTorch, TensorFlow, TensorBoard, PyQt, PyTest, Jenkins, GitLab CI/CD
- Other: Data Structure and Algorithm, Computer Vision, Deep Learning, Computer Graphics, ROS
- Certification : 
- Graduate Certificate in Artificial Intelligence 
    -  University of Missouri in Saint Louis / NSA/DHS National Center of Academic Excellence in Cyber Defense Education
- Robotic Software Engineering - Udacity
- Computer Vision - Udacity
- Introduction to Computer Graphics with DirectX11 - Part2. Realtime Pipeline.
- AWS Machine Learning - Udacity
- Python for Computer Vision with OpenCV and Deep Learning

## Patents
---
- Eungback Kim, Seungho Jang, Seongyeon Park, Hoseup Lee, Hein Jo, 2024. SCENARIO-BASED AUTONOMOUS DRIVING VEHICLE SIMULATION METHOD AND SYSTEM. WIPO Patent WO2024/117564, filed November 1, 2023, and published June 6, 2024 Patent Approved.

- Heecheol Yoo, Seungho Jang, Hojun Lim, 2024. ELECTRONIC DEVICE AND METHOD FOR PROCESSING POINT CLOUD DATA. KR 10-2024-0076717, filed June 24, 2024.

## Awards
---
- Sweeney Memorial Scholarship, Issued by Washington University in St. Louis, Engineering Department. (June 2018)
- Robert Hedier Engineering Scholarship, Issued by Washington University in St. Louis, Engineering Department. (Jan 2018)

## Classmate Comments & Endorsements
---

* **Vibhav Chemarla (Classmate) - [LinkedIn](https://www.linkedin.com/in/vibhav-chemarla/)**
> Nick(Seungho) is gifted problem solver. Nick(Seungho) and I have been classmates at UMSL for over 4 years, and have collaborated on many projects. I was constantly impressed by this positive attitude, work ethic, and analytical aptitude. Nick would be an oustanding asset to any company, and I highly recommend him **- Associate Agile Engineer at Emerson.**

* **Joseph Hill (Classmate) - [LinkedIn](https://www.linkedin.com/in/joseph-hill-78275b165/)**
> As a classmate during my undergrad program at UMSL, Seungho helped me on both an academic and personal level as my classmate and friend. He was always ready to tutor me on difficult concepts, and was quick to assist other students he didn't know. Every class I shared with Seungho was made better by his presence. **- Associate Business Intelligence Engineer at Aegion Corporation.**

* **Alberto Maiocco (Classmate) - [LinkedIn](https://www.linkedin.com/in/alberto-maiocco/)**
> Seungho possesses rare analytical skills and has the ability to quickly assess a problem and form an inventive solution. He possesses great technical knowledge of many languages and tools and the ingenuity to use them in novel ways to solve any problem. I've been fortunate to benefit from his intelligence and experience, and know that he would be a boon to any organization **- Application Software Engineer at Centene Corporation**

* **Khanh Vong (Classmate) - [LinkedIn](https://www.linkedin.com/in/khanh-vong-6b6561171/)**
> "I met Nick during my time at UMSL. We have taken many classes together and have collaborated on many projects. Nick is very motivated, and driven when it comes to learning. His biggest asset is his ability to learn and absorb new topics quickly. Meeting Nick has motivated me to take my studying more seriously. And thus, he has my highest recommendation. His drive for learning, and his ability to motivate those around him would make him an asset to any company. **- Web Developer at Beanstalk Web Solutions**

* **Jackson Hoeing (Classmate & Coworker) - [LinkedIn](https://www.linkedin.com/in/jackson-hoenig-419968160/)**
> Seungho has always been very knowledgeable about all the topics we covered as students together. He worked harder than everyone on his projects and homework. He constantly was working on learning more whether it was school related, or extracurricular. Any employer would be lucky to him because of his quick learning and broad knowledge of so many fields. Computer Vision, Artificial Intelligence, Deep Learning, Operating Systems, if it was a class at UMSL you can bet he not only aced it but also taught it to other students as a Teacher Assistant/Teacher. **- Jr. Software Developer at Technology Partners**

* **David Gillis (Classmate & Project Peer) - [LinkedIn](https://www.linkedin.com/in/david-gillis-107b20110/)**
> Seungho always stood out among his peers. He was able to rapidly learn new information with ease. In group projects, Seungho always took on a leadership role. He always starts with a problem first approach - he aims to understand the problem deeply and learn the domain, then proposes an optimal solution. Seungho was an effective mentor and role model. This showed in his academic career as he was selected to be a graduate teaching assistant, and a tutor. **- Senior Data Engineer at Bayer Crop Science**

* **Jared Diehl (Students) - [LinkedIn](https://www.linkedin.com/in/jmdiehl/)**
> Seungho is very knowledgeable and passionate about many math and machine learning topics. Back when we were students, he could always explain complex math problems simply. He has the ability to quickly assess a problem and hypothesize solutions. He excelled as a teaching assistant and is always wanting to learn new things. Any employer should be fortunate to have him as part of their team. **- SI at UMSL**

* **Nicholas Kalinowski (Student)**
> Working with Nick as my teacher for CMP SCI 1250 this past summer semester (2020) was a great way to start in the CS community. The most valuable preliminary support he provided was always being available to students- quick to reply to email, even to the point of inviting you into the zoom meeting room if he was free at the time. I had several productive meetings, including working through passing variables by reference, which has been helpful as I moved into studying pointers in CMP SCI 2250, and wrestling with a lot of basic concepts (arrays, loops) which will give me a great foundation in CS. It was great to have Nick as a teacher, and I wish him all the best in his future endeavors.  **- Student at UMSL**