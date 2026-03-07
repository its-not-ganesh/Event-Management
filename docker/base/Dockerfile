# Custom base image for development environment
# Replaces quay.io/rofrano/nyu-devops-base:sp26 with a self-built image
# Base: Official Python 3.12 on Debian Bookworm
FROM python:3.12-slim-bookworm

# Avoid interactive prompts during build
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo \
    git \
    curl \
    wget \
    vim \
    nano \
    gnupg2 \
    ca-certificates \
    openssh-client \
    apt-transport-https \
    lsb-release \
    make \
    gcc \
    libpq-dev \
    procps \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

# Install Docker CLI (client only, not the daemon)
RUN curl -fsSL https://download.docker.com/linux/debian/gpg \
      | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] \
      https://download.docker.com/linux/debian $(lsb_release -cs) stable" \
      > /etc/apt/sources.list.d/docker.list && \
    apt-get update && apt-get install -y --no-install-recommends docker-ce-cli && \
    rm -rf /var/lib/apt/lists/*

# Install kubectl
RUN ARCH="$(dpkg --print-architecture)" && \
    curl -fsSL "https://dl.k8s.io/release/$(curl -fsSL https://dl.k8s.io/release/stable.txt)/bin/linux/${ARCH}/kubectl" \
      -o /usr/local/bin/kubectl && \
    chmod +x /usr/local/bin/kubectl

# Install Helm
RUN curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Install pipenv
RUN pip install --no-cache-dir --upgrade pip pipenv

# Create non-root 'vscode' user with sudo and docker group access
RUN groupadd -g 999 docker && \
    useradd -ms /bin/bash -u 1000 -G sudo,docker vscode && \
    echo "vscode ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/vscode && \
    chmod 0440 /etc/sudoers.d/vscode

# Set default user and working directory
USER vscode
WORKDIR /app
