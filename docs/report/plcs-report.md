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

This project aims to develop a series of low-interaction honeypot decoy programs based on popular networking protocols (HTTP, FTP, and Telnet) that can lure potential attackers using Tor Hidden Services (or Onions). The main objective of the honeypots is to capture attacker interactions and encapsulate the information into logs which are processed using the Elastic Stack.

The project is comprised of several components, those being:

- **HTTP Honeypot**: A Python-based Flask application that mimics a genuine Hypertext Transfer Protocol (HTTP) server, including user authentication and directory listings. This honeypot will record any attempts to access the server, including specific pages visited and files downloaded.
- **FTP Honeypot:** A Python-based File Transfer Protocol (FTP) server utilising the `pyftpdlib` library that emulates a basic FTP service. Any login attempts will be logged by this honeypot, aiming to help profile attackers who target FTP services.
- **Telnet Honeypot**: A Python-based Telnet server that provides a realistic representation of an Apache Linux shell interface, complete with a limited set of commands. This honeypot intends to capture any login attempts to access the server.
- **ELK Stack**: An architecture named the Elastic Stack comprising Elasticsearch, Logstash, and Kibana. It is used to store the logs sent from the honeypots and render them into a format for visualisation purposes. The data store is Elasticsearch, followed by Logstash which enriches the logs, and Kibana which provides a user-friendly web interface for analysis.

The attackers will have their specialised enumeration methods to find the honeypot applications as they scan the Tor network. These decoy services can therefore be used as a means to gather valuable intelligence about the techniques, tactics, and procedures (TTPs) used by malicious entities. Using this knowledge can ultimately lead to the improvement of a software's security implementations.

The development of these honeypot applications involved a variety of different technologies and paradigms. Most notably, Python (including libraries), Object-Oriented Programming (OOP), modular programming, and Docker. The reasoning behind these choices is to ensure that the honeypot applications are lightweight and reliable, whilst also incorporating security best practices.

For more information on the full code implementation, please see a link to the GitHub repository in [Appendix 5.1](#51-github-repository).

# 2 Design decisions

This section will explain the rationale and reasoning behind two distinct design decisions.

## 2.1 Programming language and paradigm

The decision to choose Python to develop the honeypot applications was influenced by multiple key factors. Firstly, Python is a popular language due to its ease of development when it comes to its intuitive syntax simplicity, and readability [@python2021]. The Python ecosystem provides access to a huge variety of external libraries that can easily be installed. Some of these libraries formed the basis for networking protocols, for example, the `pyftpdlib` for FTP, and Flask for HTTP. Python itself also comes with many useful pre-built modules (such as `socket` for Telnet), which enabled the focus to be solely on developing the core functionality.

Beyond the inherent developer friendliness and versatility [@van2006], Python has cross-platform compatibility, allowing it to be portable between Windows, Linux, and macOS. Being portable is a major benefit, as it allows for the honeypot solution to be easily replicable and accessible.

In terms of programming paradigms, a modular and object-oriented approach was adopted to create a codebase that is easily scalable, reusable, and maintainable to facilitate enhancements or modifications. By breaking down the honeypot logic into distinct, self-contained components, where each component concerns a specific functionality, it makes it easier for developers to test and debug the individual parts of the code [@wegner1990].

For example, the folder structure within the HTTP honeypot Flask application is categorised into separate folders, where each folder represents a component of the website.

```plain
src (or source folder containing app code)
├── models
│   ├── user.py
├── routes (logic for page routes)
│   ├── login.py
│   ├── logout.py
│   ├── directory_listing.py
├── templates (HTML folder for page UI)
│   ├── login.html
│   ├── directory_listing.html
├── utils (utility functions)
│   ├── log_handler.py
```

Each component can be called with an `import` statement when required, keeping each file contained and simple.

The object-oriented paradigm further reinforces modularity and reusability, with classes being able to encapsulate all similar data and functionality. This promotes code maintainability, readability, and extensibility, allowing for new features to be implemented without disrupting the original code functionality.

To demonstrate an example from the FTP honeypot, the `pyftpdlib` itself has a function called `FTPHandler`. However, since the honeypot required more of a specialised implementation for logging capabilities, the original `FTPHandler` function had to be overridden but still extended the functionality base class. Below is the `on_login_failed()` function that has been overridden with custom logic.

```bash
class CustomFTPHandler(FTPHandler):
    def on_login_failed(self, username, password):
        log_auth(self, username, password)
```

In essence, the powerful combination of Python being developer-centric, cross-platform capabilities, and the application of both an object-oriented and modular design results in a honeypot solution that is easy to adapt, flexible, robust, and extensible to meet necessary security requirements.

## 2.2 Containerisation and deployment

The decision to use Docker containers was mainly driven by the need for cross-platform compatibility, service isolation, management, and scalability of the honeypot applications. Packaging each service – the honeypot applications, Tor, and components of the ELK stack – with the relevant dependencies it requires, consistent yet reproducible deployments in different deployment environments.

For example, in the Telnet honeypot, all necessary Python libraries and packages are installed from Linux and the `requirements.txt`` file.

```dockerfile
# Install Python system packages
RUN apk update && apk add --no-cache python3 python3-dev py3-pip

# Install required Python libraries
RUN pip3 install -r requirements.txt
```

The concept of containerisation allows for each service to be individually managed, meaning that resources can be efficiently allocated as needed [@preeth2015]. More importantly, the isolation provided by Docker containers helps to maintain the overall security of the system, since every component is confined to its execution environment [@bui2015].

This modular and container-based architecture approach offers multiple benefits. Since each Docker container is essentially a virtual machine running a lightweight fork of Linux. For every Docker container, excluding the ELK stack, a base image from the Alpine Linux distribution is used.

```dockerfile
FROM alpine:latest
```

This means it can seamlessly run on a wide range of architectures being bundled with all the necessary packages each application needs. Not only is it beneficial in a production environment, but also when developing, the use of Docker image caching allows for the containers to be built quickly and efficiently each time a change is made [@rad2017]. It also circumvents the limitations users may have on their local machine, such as deprecated devices that don't support the latest packages – the only requirement being raw hardware power [@potdar2020].

In terms of security, each Docker container is isolated, so the attack surface is minimised as much as possible. A vulnerability within one honeypot service would be contained within its container, preventing cross-contamination with other containers [@bui2015]. Any exploits that attackers attempt to use will expose faults within that specific container [@bui2015]. This is helpful to the developer since they are certain that they are only concerned with the codebase for that container making it much easier to develop patches.

# 3 Cyber security considerations

## 3.1 Integrating Tor hidden services

Including Tor hidden services was a vital design decision, as it not only provides a degree of anonymity for the honeypot applications but also helps to lure potential attackers. The accessibility of the honeypot applications, via Tor's `.onion` domains served as a major feature for this project, helping to further increase the availability of these decoy services to malicious entities scanning the Tor network.

However, this presented its own set of unique challenges. Although Tor offered several advantages, it was difficult to optimise the speed at which these honeypot applications could be served to the attacker [@barton2018]. Additional latency would inherently be invoked since all traffic must be routed through multiple relays before reaching the end user's device [@torproject2023]. A slower response time like so could potentially reduce the honeypot's effectiveness and put off impatient attackers. Despite this, it provides an additional layer of security making it more taxing for attackers to trace back to the true origins of the vulnerable services, reducing the risk of system compromise for end-users through masking identities (location, IP address, device information, etc.) through the different relay routers [@2torproject2023]. For honeypot applications, since they are vulnerable, they must be secured without exposing the inner workings of the production system, so the benefits provided by Tor in this case outweigh the performance issues it poses.

Moreover, the use of Tor hidden services also aligns with ethical and legal issues that naturally arise when distributing vulnerable systems. Since the user is under a certain level of risk when using this architecture, through the Tor network, the risk of inadvertently exposing and impacting users as a result of it is greatly reduced [@caliskan2015]. This in turn promotes values of responsibility and integrity when interacting with or developing the honeypot applications.

## 3.2 Integrating the ELK stack

The integration of the ELK (Elasticsearch, Logstash, and Kibana) stack was influenced by the need for a secure but comprehensive logging and visualiation solution [@chhajed2015] to supplement the honeypot applications. Rather than manually implementing a logging system that attackers could use to laterally move throughout the system's architecture, using pre-built solutions would be a wise choice considering vulnerable services are hosted via the honeypots.

Elasticsearch was selected as the main data store, due to its powerful ability to index and query logs – a search engine based on Apache Lucene [@son2017]. Since Elasticsearch has an inherently robust search engine, the tool can essentially ingest, index, and retrieve large quantities of log data generated continuously by the honeypot applications. The speed of Elasticsearch allows for flexible and quick analysis of all data collected, as its helpful in understanding potential attack surfaces and patterns.

Logstash listens for HTTP input from the honeypot applications and applies filters to the raw incoming log data [@son2017]. The various filters help to render and transform the logs in a format through processes such as normalisation that facilitates effective analysis and visualitation through Kibana.

The Kibana web interface enables users to explore and gain insight from gathered results. As this is a user-friendly tool, the dashboard can be configured in multiple combinations to result in charts, graphs, and tables [@son2017]. This can be used to make data-driven decisions and help secure technical aspects of systems hosting HTTP, FTP, or Telnet.

Most importantly, the reasoning behind why the ELK stack was chosen was that it was a pre-built tool that is widely tested and documented, giving it more of an edge over manual logging systems.

For example, in the Dockerfile configuration for Kibana, the container uses the official base image. From this, other custom settings can be applied or overridden.

```dockerfile
FROM docker.elastic.co/kibana/kibana:8.13.1
```

The open-source nature of each ELK stack component means that there is a community of experienced developers who have created custom plugins and forks that can be integrated easily into a default ELK stack configuration.

An example of this would be from the Elasticsearch configuration. Here, a YAML file containing default options can be overridden.

```yaml
# Cluster name
cluster.name: honeypot-cluster

# Node name
node.name: honeypot-node

# Network settings
network.host: 0.0.0.0

# Discovery settings
discovery.type: single-node
```

# 5 Appendices

## 5.1 GitHub repository

[https://github.com/iArcanic/onion-honeypot](https://github.com/iArcanic/onion-honeypot)

# 6 References
