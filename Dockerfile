# Lightweight Linux distro as the base image
FROM alpine:latest

# Install required dependencies
RUN apk update && apk add tor python3

# Copy required files to destination directory
COPY config/torrc /etc/tor/

# Expose necessary ports
EXPOSE 9050

# Run required commands
CMD ["sh", "-c", "cd ~/ && python3 -m http.server --bind 127.0.0.1 5000 & tor"]
