# Lightweight Linux distro as the base image
FROM alpine:latest

# Install required dependencies
RUN apk update && apk add --no-cache tor

# Copy Tor config
COPY torrc /etc/tor/

# Expose necessary ports
EXPOSE 9050

# Start Tor service
CMD ["tor"]