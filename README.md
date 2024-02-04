# EnviroConfig

EnviroConfig is a Python utility designed to streamline the process of loading and managing configurations from YAML files based on the application's running environment. It supports loading environment-specific configurations and fetching secrets, making it easier to manage different settings for development, testing, and production environments.

## Features

- **Environment-Specific Configuration**: Load configurations specific to the environment your application is running in (e.g., development, production).
- **Fallback to Environment Variables**: If a configuration key is not found in the YAML file, EnviroConfig will attempt to fetch it from the environment variables.
- **Secret Management**: A placeholder method for secret fetching, which can be extended to integrate with secret managers like AWS Secrets Manager, Azure Key Vault, etc.

## Getting Started

### Prerequisites

- Python 3.x
- PyYAML

Install PyYAML using pip:

```bash
pip install pyyaml
