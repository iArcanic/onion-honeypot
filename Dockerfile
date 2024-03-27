# Lightweight Linux distro as the base image
FROM alpine:latest

# Install required dependencies
RUN apk add --no-cache tor python3 python3-dev py3-pip openssh-server openssh-client

# Create a virtual environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Copy required files to destination directory
COPY config/torrc /etc/tor/
COPY config/banner.txt /etc/ssh
COPY config/sshd_config /etc/ssh
COPY config/motd /etc/motd
COPY src /app

# Expose necessary ports
EXPOSE 5000 9050 22

# Install Python dependencies
WORKDIR /app
RUN pip3 install -r requirements.txt

# Generate SSH host keys
RUN ssh-keygen -A

# Create .ssh directory and add authorized_keys file
RUN mkdir -p /root/.ssh && \
    chmod 700 /root/.ssh && \
    touch /root/.ssh/authorized_keys && \
    chmod 600 /root/.ssh/authorized_keys

# Run required commands
CMD ["sh", "-c", "/usr/sbin/sshd -D & python3 flask_app/app.py & python3 ssh_honeypot/main.py & tor"]
