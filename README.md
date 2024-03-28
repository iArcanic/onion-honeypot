# onion-honeypot

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A low interaction honeypot decoy program to lure potential attackers using Tor Hidden Services (Onions) and deployed via Docker containers.

## Prerequisites

Before running the application, ensure you have the following prerequisites installed:

1. **Docker**: Ensure Docker is installed on your system. You can download and install Docker from the [official Docker website](https://www.docker.com/get-started/).

The following dependencies are not required since all dependencies are taken care by the Docker container, but can still be useful for testing and/or debugging:

2. **Python 3**: Install Python 3 on your system. You can download Python from the [official Python website](https://www.python.org/downloads/) or install it using your system's package manager.

3. **PIP**: PIP is the package installer for Python. It usually comes installed with Python by default. If not, you can install it using the appropriate package manager for your system.

## Usage

1. Clone the repository to your local machine.

```bash
git clone https://github.com/iArcanic/onion-honeypot
```

2. Navigate to the project's directory.

```bash
cd onion-honeypot
```

> NOTE: Ensure that you are in the project's root directory before running any of the following usage commands

### Accessing the Docker SSH Honeypot

1. Ensure that a SSH RSA key pair exists on your local machine and copy the public key to your clipboard.

```bash
ls ~/.ssh
```

- You should see `id_rsa.pub` (public key) and `id_rsa` (private key) files listed. Copy the contents of `id_rsa.pub` to your clipboard.

- If it does not exist, create a SSH RSA key pair and copy the public key to your clipboard.

```bash
ssh-keygen -t rsa -b 4096
```

2. Build the Docker image and run the container.

```bash
docker-compose up --build
```

3. In a new terminal tab, get the Docker container's ID.

```bash
docker ps -a
```

4. Open up the `authorized_keys` file and paste in your public key using the container ID.

```bash
docker exec -ti <CONTAINER_ID> vi /root/.ssh/authorized_keys
```

5. Get the IP of the Docker container using its container ID.

```bash
docker inspect <CONTAINER_ID> | grep IPAddress
```

6. SSH into the Docker container using the container's IP.

```bash
ssh root@<DOCKER_CONTAINER_IP>
```

7. Remove the Docker container after usage.

```bash
docker-compose down
```

### Accessing Flask RESTful API endpoint

1. Build the Docker image and run the container.

```bash
docker-compose up --build
```

2. Open API endpoint with the URL.

```bash
http://localhost:5000
```

> NOTE: Alternatively, you can also use `curl` or `wget` instead

3. Remove the Docker container after usage.

```bash
docker-compose down
```

### Accessing the `.onion` site

1. Build the Docker image and run the container.

```bash
docker-compose up --build
```

2. Open a new terminal tab and get the container's ID.

```bash
docker ps -a
```

3. Display the contents of the `hostname` file to get the `.onion` URL string using the container ID.

```bash
docker exec -ti <CONTAINER_ID> cat /var/lib/tor/hidden_service/hostname
```

4. Run the `.onion` site in a Tor-enabled application.

5. Remove the Docker container after usage.

```bash
docker-compose down
```