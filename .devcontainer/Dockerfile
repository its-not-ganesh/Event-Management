# Dev container image for Event-Management
# Uses the custom base image instead of quay.io/rofrano/nyu-devops-base:sp26
ARG BASE_IMAGE=event-mgmt-base:latest
FROM ${BASE_IMAGE}

# Set up the Python development environment
WORKDIR /app
COPY Pipfile Pipfile.lock ./
RUN sudo python -m pip install --upgrade pip pipenv && \
    sudo pipenv install --system --dev

# Install user mode tools
COPY .devcontainer/scripts/install-tools.sh /tmp/
RUN cd /tmp && bash ./install-tools.sh
