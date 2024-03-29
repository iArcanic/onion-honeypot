# Lightweight Linux distro as the base image
FROM alpine:latest

# Install required dependencies
RUN apk update && apk add --no-cache tor python3

# Copy Tor config
COPY torrc /etc/tor/

# Expose necessary ports
EXPOSE 9050

# Start Tor service with Python HTTP server
CMD ["sh", "-c", "cd ~/ && python3 -m http.server --bind 127.0.0.1 5000 & tor"]