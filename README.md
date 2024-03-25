# onion-honeypot
A low interaction honeypot decoy program to lure potential attackers using Tor Hidden Services (Onions) and deployed via Docker containers

## Usage

1. Build the Docker image

```bash
docker build -t <IMAGE_TAG> .
```

2. Verify whether the image has been created

```bash
docker images
```

3. Run a container with the built image

```bash
docker run -p <PORT>:9050 <IMAGE_TAG>
```

4. Open a new terminal tab and verify that the container is running

```bash
docker ps -a
```

5. `cat` the contents of the `hostname` file to get the `.onion` URL string

```bash
docker exec -ti <CONTAINER_ID> cat /var/lib/tor/hidden_service/hostname
```

6. Run the `.onion` site in a Tor-enabled application
