#!/bin/bash
######################################################################
# Post-create setup — runs after the container is created
######################################################################

echo "**********************************************************************"
echo "Setting up Docker user development environment..."
echo "**********************************************************************"

echo "Setting up registry.local..."
sudo bash -c "echo '127.0.0.1    cluster-registry' >> /etc/hosts"

echo "Making git stop complaining about unsafe folders"
git config --global --add safe.directory /app

echo "**********************************************************************"
echo "Setup complete"
echo "**********************************************************************"
