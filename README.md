# onion-honeypot
A low interaction honeypot decoy program to lure potential attackers using Tor Hidden Services (Onions) and deployed via Docker containers

## Usage

### Access Flask RESTful API endpoint

1. Build the Docker image and run the container

```bash
docker-compose up --build
```

2. Open API endpoint

- Access the URL in the browser directly, at:

    ```bash
    http://127.0.0.1:5000
    ```

    or

    ```bash
    http://localhost:5000
    ```

- With `curl`:

    ```bash
    curl localhost:5000
    ```

- With `wget`:

    ```bash
    wget -O - localhost:5000
    ```

3. Remove the existing Docker container

```bash
docker-compose down
```

### Accessing the `.onion` hidden service site

1. Build the Docker image and run the container

```bash
docker-compose up --build
```

2. Open a new terminal tab and get the container's ID

```bash
docker ps -a
```

3. Display the contents of the `hostname` file to get the `.onion` URL string using the container ID

```bash
docker exec -ti <CONTAINER_ID> cat /var/lib/tor/hidden_service/hostname
```

4. Run the `.onion` site in a Tor-enabled application

5. Remove the existing Docker container

```bash
docker-compose down
```