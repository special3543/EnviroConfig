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
```
## Installation
Clone the repository to your local machine:

```bash
git clone https://github.com/<your-github-username>/EnviroConfig.git
cd EnviroConfig
```

## Usage
Create a YAML configuration file (config.yaml) with your settings:

```yaml
development:
  database_url: sqlite:///dev.db
production:
  database_url: postgresql://user:password@localhost/prod_db
```

Use the EnvConfigurator in your application:

```python
from env_configurator import EnvConfigurator

config = EnvConfigurator('config.yaml')
database_url = config.get('database_url')
```


## Running Tests
Ensure you have pytest installed, then run:

```bash
pytest
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


### Additional Notes:

- Replace `<your-github-username>` with your actual GitHub username.
- Make sure to include a LICENSE file in your repository. The MIT License is a good default choice for open source projects.
- You might also want to include a `.gitignore` file tailored for Python projects to exclude unnecessary files (like `__pycache__` directories) from your repository.
