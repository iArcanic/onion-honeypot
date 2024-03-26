# Lightweight Linux distro as the base image
FROM alpine:latest

# Install required dependencies
RUN apk add --no-cache tor python3 python3-dev py3-pip

# Create a virtual environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Copy required files to destination directory
COPY config/torrc /etc/tor/
COPY src /app
COPY requirements.txt /app

# Expose necessary ports
EXPOSE 5000 9050

# Install Python dependencies
WORKDIR /app
RUN pip3 install -r requirements.txt

# Run required commands
CMD ["sh", "-c", "python3 flask_app/app.py & tor"]
