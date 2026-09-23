# Secure CI/CD Pipeline

This repository demonstrates a CI/CD pipeline implemented with GitHub Actions.

## Pipeline Flow

Trigger → Build → Test → Security Scan → Deploy

## Pipeline Stages

- Build: Installs dependencies and compiles the Python application.
- Validation: Uses flake8 for lint checking and pytest for unit testing.
- Security: Uses pip-audit to scan Python dependencies.
- Deployment: Simulates deployment after all previous stages pass.
