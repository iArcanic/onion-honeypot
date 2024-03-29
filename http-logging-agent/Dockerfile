# Lightweight Linux distro as the base image
FROM alpine:latest

# Install required dependencies
RUN apk update && apk add --no-cache python3 python3-dev py3-pip

# Create virtual Python environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Copy HTTP Logging Agent Python files
COPY src/ /app/
COPY requirements.txt /app/

# Set working directory
WORKDIR /app

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Start HTTP Logging Agent
CMD ["python3", "main.py"]