import os
import yaml
from typing import Any, Dict, Optional

class EnvConfigurator:
    def __init__(self, config_path: str, environment: Optional[str] = None):
        self.environment = environment or os.getenv('ENVIRONMENT', 'development')
        self.config = self._load_config(config_path)

    def _load_config(self, config_path: str) -> Dict[str, Any]:
        with open(config_path, 'r') as file:
            all_configs = yaml.safe_load(file)
        env_config = all_configs.get(self.environment, {})
        return env_config

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, os.getenv(key.upper(), default))

    def get_secret(self, key: str, default: Any = None) -> Any:
        # Placeholder for secret fetching logic
        # This could be extended to fetch secrets from a secret manager
        return os.getenv(key.upper(), default)

# Example usage:
# config = EnvConfigurator('config.yaml')
# database_url = config.get('database_url')
# secret_api_key = config.get_secret('api_key')
