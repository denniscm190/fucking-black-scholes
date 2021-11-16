# syntax=docker/dockerfile:1

# Install Python image
FROM python:3.8-slim-buster

# Create working directory and install dependencies
WORKDIR /fucking-black-sholes

# Copy files
COPY . .

# Install package
RUN ["python", "setup.py", "install"]

# Test package
CMD fbs --spot-price=20.00 --exercise-price=21.00 --risk-free-rate=0.05 --std=0.25 --expiration=0.5