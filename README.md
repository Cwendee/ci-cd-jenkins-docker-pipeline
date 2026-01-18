# CI/CD Pipeline with Jenkins and Docker

This project demonstrates a production-style CI/CD pipeline that builds, tests, containerizes, and deploys a Flask web application using Jenkins and Docker.

## Architecture Overview

![CI/CD Architecture](ci-cd-architecture.png)


## CI/CD Pipeline Overview

This project demonstrates a production-style CI/CD pipeline using Jenkins and Docker.

### Pipeline Stages
- **Checkout** – Pulls source code from GitHub
- **Build** – Creates a Python virtual environment and installs dependencies
- **Test** – Runs automated pytest tests
- **Docker Build** – Builds a container image
- **Deploy** – Replaces any existing container and deploys the new version
- **Health Check** – Validates deployment via HTTP endpoint

### Key Engineering Decisions
- Host and container ports are explicitly separated to avoid conflicts on shared infrastructure
- Deployment is idempotent and safe to rerun
- Application health is validated before pipeline success

