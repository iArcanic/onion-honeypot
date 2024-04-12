---
title: "PLCS-CW2 Report"
author: "Preetham Ananthkumar 2242090"
bibliography: docs/report/references.bib
toc: true
toc-title: Table of Contents
toc-depth: 4
geometry: "left=1.25cm, right=1.25cm, top=1.25cm, bottom=1.25cm"
csl: docs/report/harvard-imperial-college-london.csl
---

# 1 Introduction

<!-- 325 words -->

This project aims to develop a series of low-interaction honeypot decoy programs based on popular networking protocols (HTTP, FTP, and Telnet) that can lure potential attackers using Tor Hidden Services (or Onions). The main objective of the honeypots is to capture attacker interactions and encapsulate the information into logs which are processed using the Elastic Stack.

The project is comprised of several components, those being:

- **HTTP Honeypot**: A Python-based Flask application that mimics a genuine Hypertext Transfer Protocol (HTTP) server, including user authentication and directory listings. This honeypot will record any attempts to access the server, including specific pages visited and files downloaded.
- **FTP Honeypot:** A Python-based File Transfer Protocol (FTP) server utilising the `pyftpdlib` library that emulates a basic FTP service. Any login attempts will be logged by this honeypot, aiming to help profile attackers who target FTP services.
- **Telnet Honeypot**: A Python-based Telnet server that provides a realistic representation of an Apache Linux shell interface, complete with a limited set of commands. This honeypot  intends to capture any login attempts to access the server.
- **ELK Stack**: An architecture named the Elastic Stack comprising Elasticsearch, Logstash, and Kibana. It is used to store the logs sent from the honeypots and render them into a format for visualisation purposes. The data store is Elasticsearch, followed by Logstash which enriches the logs, and Kibana which provides a user-friendly web interface for analysis.

The attackers will have their specialised enumeration methods to find the honeypot applications as they scan the Tor network. These decoy services can therefore be used as a means to gather valuable intelligence about the techniques, tactics, and procedures (TTPs) used by malicious entities. Using this knowledge can ultimately lead to the improvement of a software's security implementations.

The development of these honeypot applications involved a variety of different technologies and paradigms. Most notably, Python (including libraries), Object-Oriented Programming (OOP), modular programming, and Docker. The reasoning behind these choices is to ensure that the honeypot applications are lightweight and reliable, whilst also incorporating security best practices.

# 2 Design decisions

<!-- 575 words -->

This section will explain the rationale and reasoning behind the design decisions.

## 2.1 Programming language

<!-- 115 words -->

The decision to choose Python to develop the honeypot applications was influenced by multiple key factors. Firstly, Python is a popular language due to its ease of development when it comes to its syntax, including its simplicity and readability. The Python community consists of many experienced developers, meaning there is a huge variety of external libraries that can easily be installed. Some of these libraries formed the basis for networking protocols, such as `pyftpdlib` for FTP, and Flask for HTTP. Python itself also comes with many useful pre-built modules (such as `socket` for Telnet), which enabled the focus to be on developing the core functionality. Furthermore, Python has cross-platform compatibility, allowing it to be portable between Windows, Linux, and macOS.

## 2.2 Modular design and Object-Oriented Programming (OOP)

<!-- 115 words -->

A modular and object-oriented approach 

## 2.3 Containerisation with Docker

<!-- 115 words -->

## 2.4 ELK stack integration

<!-- 115 words -->

## 2.5 Tor hidden service integration

<!-- 115 words -->

# 3 Cyber security considerations

<!-- 575 words -->

# 4 Conclusion

<!-- 175 words -->

# 5 Appendices

# 6 References
