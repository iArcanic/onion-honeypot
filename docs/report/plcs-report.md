---
title: "PLCS-CW2 Report"
author: "2242090"
bibliography: docs/report/references.bib
toc: true
toc-title: Table of Contents
toc-depth: 4
geometry: "left=1.25cm, right=1.25cm, top=1.25cm, bottom=1.25cm"
csl: docs/report/harvard-imperial-college-london.csl
---

# 1 Introduction

<!-- 325 words maximum -->
<!-- Currently 337 words -->

This project aims to develop a series of low-interaction honeypot decoy programs based on popular networking protocols (HTTP, FTP, and Telnet) that can lure potential attackers using Tor Hidden Services (or Onions). The main objective of the honeypots is to capture attacker interactions and encapsulate the information into logs which are processed using the Elastic Stack.

The project is comprised of several components, those being:

- **HTTP Honeypot**: A Python-based Flask application that mimics a genuine Hypertext Transfer Protocol (HTTP) server, including user authentication and directory listings. This honeypot will record any attempts to access the server, including specific pages visited and files downloaded.
- **FTP Honeypot:** A Python-based File Transfer Protocol (FTP) server utilising the `pyftpdlib` library that emulates a basic FTP service. Any login attempts will be logged by this honeypot, aiming to help profile attackers who target FTP services.
- **Telnet Honeypot**: A Python-based Telnet server that provides a realistic representation of an Apache Linux shell interface, complete with a limited set of commands. This honeypot intends to capture any login attempts to access the server.
- **ELK Stack**: An architecture named the Elastic Stack comprising Elasticsearch, Logstash, and Kibana. It is used to store the logs sent from the honeypots and render them into a format for visualisation purposes. The data store is Elasticsearch, followed by Logstash which enriches the logs, and Kibana which provides a user-friendly web interface for analysis.

The attackers will have their specialised enumeration methods to find the honeypot applications as they scan the Tor network. These decoy services can therefore be used as a means to gather valuable intelligence about the techniques, tactics, and procedures (TTPs) used by malicious entities. Using this knowledge can ultimately lead to the improvement of a software's security implementations.

The development of these honeypot applications involved a variety of different technologies and paradigms. Most notably, Python (including libraries), Object-Oriented Programming (OOP), modular programming, and Docker. The reasoning behind these choices is to ensure that the honeypot applications are lightweight and reliable, whilst also incorporating security best practices.

# 2 Design decisions

<!-- 575 words maximum -->

This section will explain the rationale and reasoning behind two distinct design decisions.

## 2.1 Programming language and paradigm

<!-- 287 words maximum -->
<!-- Currently  words -->

The decision to choose Python to develop the honeypot applications was influenced by multiple key factors. Firstly, Python is a popular language due to its ease of development when it comes to its intuitive syntax simplicity, and readability. The Python ecosystem provides access to a huge variety of external libraries that can easily be installed. Some of these libraries formed the basis for networking protocols, for example, the `pyftpdlib` for FTP, and Flask for HTTP. Python itself also comes with many useful pre-built modules (such as `socket` for Telnet), which enabled the focus to be solely on developing the core functionality. Beyond the inherent developer friendliness and versatility, Python has cross-platform compatibility, allowing it to be portable between Windows, Linux, and macOS. Being portable is a major benefit, as it allows for the honeypot solution to be easily replicable and accessible.

In terms of programming paradigms, a modular and object-oriented approach was adopted to create a codebase that is easily scalable, reusable, and maintainable to facilitate enhancements or modifications. By breaking down the honeypot logic into distinct, self-contained components, where each component concerns a specific functionality, it makes it easier for developers to test and debug the individual parts of the code. The object-oriented paradigm further reinforces modularity and reusability, with classes being able to encapsulate all similar data and functionality. This promotes code maintainability, readability, and extensibility, allowing for new features to be implemented without disrupting the original code functionality.

In essence, the powerful combination of Python being developer-centric, cross-platform capabilities, and the application of both an object-oriented and modular design results in a honeypot solution that is easy to adapt, flexible, robust, and extensible to meet necessary security requirements.

## 2.2 Containerisation and deployment

<!-- 288 words maximum -->
<!-- Currently 110 words -->

The decision to use Docker containers was mainly driven by the need for cross-platform compatibility, service isolation, management, and scalability of the honeypot applications. Packaging each service with the relevant dependencies it requires, including each honeypot application, Tor, and components of the ELK stack, allows for consistent yet reproducible deployments in different deployment environments. The concept of containerisation allows for each service to be individually managed, meaning that resources can be efficiently allocated and faults can easily be identified. More importantly, the isolation provided by Docker containers helps to maintain the security of each service individually and for the whole architecture, since every component is confined to its execution environment.

# 3 Cyber security considerations

<!-- 575 words maximum -->

## 3.1 Integrating Tor hidden services

<!-- 287 words maximum -->
<!-- Currently 126 words -->

Including Tor hidden services was a vital design decision, as it not only provides anonymity for the honeypot applications but also helps to lure potential attackers. The accessibility of the honeypot applications, via Tor's `.onion` domains served as a major feature for this project, helping to further increase the availability of these decoy services to malicious entities scanning the Tor network. However, this presented its own set of unique challenges. Although Tor offered several advantages, it was difficult to optimise the speed at which these honeypot applications could be served to the attacker. Ultimately, it provides an additional layer of security making it more taxing for attackers to trace back to the true origins of the vulnerable services, reducing the risk of system compromise for end-users.

## 3.2 Integrating the ELK stack

<!-- 288 words maximum -->
<!-- Currently 124 words -->

The choice to integrate the ELK stack (Elasticsearch, Logstash, and Kibana) was influenced by the need for a secure but comprehensive logging system. Rather than manually implementing a logging system that attackers could use to laterally move throughout the system's architecture, using pre-built solutions would be a wise choice considering vulnerable services are hosted via the honeypots. Elasticsearch was used as the primary data store, providing an effective way to ingest, query, and index incoming logs. Logstash applied filters to those logs, enriched them, and made them suitable for analysis. Kibana, the web interface, enables users to explore and gain insight from gathered results. This can be used to make data-driven decisions and help secure technical aspects of systems hosting HTTP, FTP, or Telnet.

# 4 Conclusion

<!-- 175 words maximum -->

# 5 Appendices

# 6 References
