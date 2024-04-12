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

This project aims to develop a series of low-interaction honeypot decoy programs based on a set of popular networking protocols (HTTP, FTP, and Telnet) that can lure potential attackers using Tor Hidden Services (or known as Onions). The main objective of the honeypot applications is to capture attacker interactions and encapsulate that information into logs which can effectively be analysed using the Elastic Stack infrastructure (commonly known as the ELK stack).

The cyber tool is comprised of several key components, those being:

- **HTTP Honeypot**: A Python-based Flask application that mimics a genuine Hyper Text Transfer Protocol (HTTP) server, including user authentication and a web directory listing. This honeypot application will record any attempts to access the server, including the specific pages visited and files downloaded.
- **FTP Honeypot:** A Python-based File Transfer Protocol (FTP) server utilising the `pyftpdlib` library that emulates a basic FTP service. Any login attempts and FTP activities will be logged by this honeypot, aiming to help profile attackers who target FTP services.
- **Telnet Honeypot**: A Python-based Telnet server that provides a realistic representation of an Apache Linux shell interface, complete with a limited set of executable commands. This honeypot application intends to capture any attempts to access the server via Telnet.
- **ELK Stack**: An architecture named the Elastic Stack comprising Elasticsearch, Logstash, and Kibana. It is used to store the logs sent from the respective honeypot applications and render them into a format for visualisation purposes. The data store in this case would be Elasticsearch, followed by Logstash which enriches and processes the logs, and finally, Kibana is the versatile yet user-friendly web interface for analysing the collected logs.

Via the `.onion` sites, the attackers will have their specialised enumeration methods to find the honeypot applications as they scan the Tor network. These decoy services can therefore be used as a means to gather valuable intelligence about the techniques, tactics, and procedures (TTPs) used by malicious entities. Using this knowledge can ultimately lead to more robust technical measures to improve a software's security implementations.

The development of these honeypot applications and their deployment involved a variety of different programming languages and paradigms. Most notably, Python (including libraries), Object Oriented Programming (OOP), modular programming, and Docker. The reasoning behind these choices was to ensure that the honeypot applications are lightweight, flexible, and reliable, whilst also incorporating relevant security features and best practices.

In essence, this project serves as a powerful cyber tool that can be used by security professionals and researchers in the industry to understand the interactions and behaviors of potential attackers with the overarching goal of improving the current cybersecurity landscape.

# 2 Design decisions

<!-- 575 words -->

# 3 Cyber security considerations

<!-- 575 words -->

# 4 Conclusion

<!-- 175 words -->

# 5 Appendices

# 6 References
