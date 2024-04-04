# onion-honeypot

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
[![Elastic Stack version](https://img.shields.io/badge/Elastic%20Stack-8.13.0-00bfb3?style=flat&logo=elastic-stack)](https://www.elastic.co/blog/category/releases)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A low interaction HTTP honeypot decoy program to lure potential attackers using Tor Hidden Service (Onions) with ELK stack for data logging and visualising.

## Architecture

1. **Host machine**: The underlying hardware (i.e. your machine) that will run the Docker Engine.
2. **Docker Engine**: The container orchestration platform that manages and runs containers.
3. **HTTP honeypot**: A Docker container running the honeypot application.
    - **Flask application**: A lightweight web application within the honeypot container that simulates a vulnerable system and captures the attacker's interactions.
    - **Send logs**: The honeypot application will then send logs of captured interaction data (i.e. attacker IP, user agent etc.) to Logstash.
4. **Logstash**: A Docker container that recieves logs from the honeypot, parses or enriches them for further processing, and sends it to Elasticsearch.
5. **Elasticsearch**: A Docker container that stores the processed logs from Logstash in a searchable format.
6. **Kibana**: A Docker container that provides the web interface for visualising and analysing logs stored in Elasticsearch.

## Features

- The HTTP honeypot is accessible on Tor (or dark web) as a hidden service, luring attackers.
- Using Flask for the HTTP honeypot since it is a lightweight application.
- ELK stack for a versatile and secure way of accessing honeypot data.
- Powerful logging and data visualising capabilities through Kibana.
- Fully containerised setup – no external packages or dependencies required.

## Prerequisites

### Docker

Ensure the Docker engine is installed on your system with version **18.06.0** or higher.

You can download and install the Docker engine from the [official Docker website](https://www.docker.com/get-started/).

> [!NOTE]
> - Especially on Linux, make sure your user has the [required permissions](https://docs.docker.com/engine/install/linux-postinstall/) to interact with the Docker daemon.
> - If you are unable to do this, either append `sudo` in front of each `docker` command or switch to a root user using `sudo -s`.

### Docker Compose

Ensure that Docker Compose is installed on your system with **version 1.28.0** or higher. 

You can download and install Docker Compose from the [official Docker website](https://docs.docker.com/compose/install/).

### Port availability

The services running on each Docker Container use the following ports. Ensure that these ports are free and are not running any conflicting services or have firewall rules concerning them.

- **Tor**:
    - 9050 (for SOCKS)
- **Honeypot**:
    - 5000 (for Python Flask application)
- **Elasticsearch**:
    - 9200 (for HTTP)
    - 9300 (for TCP transport)
- **Logstash**:
    - 5044 (for Beats input) – currently not using Beats at the moment
    - 5514 (for HTTP input)
    - 9600 (for API monitoring endpoint)
- **Kibana**:
    - 5601 (for web UI console)

## Usage

### General usage

1. Clone the repository to your local machine.

```bash
git clone https://github.com/iArcanic/onion-honeypot
```

2. Navigate to the project's directory.

```bash
cd onion-honeypot
```

3. Build and run all Docker containers.

```bash
docker-compose up
```

> [!NOTE]
> With Docker Compose, you can also optionally use the following:
> - If you want to build the images each time (or changed a Dockerfile), use `docker-compose --build`.
> - If you want to run all the services in the background, use `docker-compose -d`

4. Access the Kibana web UI console at [http://localhost:5601](http://localhost:5601). 

> [!NOTE]
> - You may need to give some time (a couple of minutes depending upon your network speed and hardware capabilities) for all containers to run and initialise.
> - If you are running for the first time or using the `--build` flag, expect it to take some time.

### Accessing and testing the HTTP honeypot

> [!NOTE]
> - Alternatively, for speed and ease of access, you can open and interact with the HTTP honeypot locally at [http://localhost:5000](http://localhost:5000).
> - This will produce the same results as accessing the `.onion` site.

1. List all available containers and find the ID of the Tor container.

```bash
docker ps -a
```

2. Using that, display the contents of the `hostname` file.

```bash
docker exec -ti <CONTAINER_ID> cat /var/lib/tor/hidden_service/hostname
```

You should see a long string ending with `.onion`. This is the Tor hidden service.

3. Open that `.onion` in a Tor-enabled application, such as the Tor browser.

4. Interact with the HTTP honeypot and see logged activities at the Kibana console ([http://localhost:5601](http://localhost:5601)).
