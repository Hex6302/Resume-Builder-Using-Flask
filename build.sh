#!/usr/bin/env bash
# exit on error
set -o errexit

# Install system dependencies
apt-get update
apt-get install -y python3-pip python3-dev

# Upgrade pip and install build tools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade setuptools wheel

# Install Python dependencies
python3 -m pip install -r requirements.txt 