# Week 5 CI/CD DevSecOps Pipeline

This repository demonstrates a CI/CD pipeline implemented with GitHub Actions.

## Pipeline Flow

Trigger → Build → Test → Security Scan → Deploy

## Pipeline Stages

### Source Control Trigger

The workflow runs when code is pushed to the main branch or a feature
branch. It also runs when a pull request targets the main branch. The
workflow can be started manually through workflow_dispatch.

### Build

The build job checks out the repository, configures Python, installs the
project dependencies, compiles the application files, and runs the
sample application.

### Validation and Test

The test job uses flake8 to inspect the Python files for code-quality
problems. It then uses pytest to run automated unit tests.

### Security Scan

The security job runs pip-audit against requirements.txt to identify
known vulnerabilities in the application's Python dependencies.

### Simulated Deployment

The deployment job runs only after the build, test, and security jobs
have completed successfully. It prints deployment messages to simulate
a successful release.

## Security Control

Dependency scanning occurs before deployment. This prevents the
deployment job from running when pip-audit detects a known vulnerable
dependency.
