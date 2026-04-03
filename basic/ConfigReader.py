from pathlib import Path
from typing import Optional

class ConfigReader:
    _project_root = Path(__file__).resolve().parent.parent
    _config_file_path = _project_root / "configs" / "URI.properties"
    _configs: dict[str, str] = {}
    _loaded = False

    @classmethod
    def load_configs(cls, config_file_path: str | None = None) -> dict[str, str]:
        """Load all URI configs from the properties file."""
        config_path = Path(config_file_path) if config_file_path else cls._config_file_path
        cls._configs = {}

        if not config_path.exists():
            raise FileNotFoundError(f"URI.properties file not found at {config_path}")

        for raw_line in config_path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()

            if not line or line.startswith("#") or "=" not in line:
                continue

            key, value = line.split("=", 1)
            cls._configs[key.strip()] = value.strip()

        cls._loaded = True
        return dict(cls._configs)

    @classmethod
    def get_uri(cls, uri_key: str) -> Optional[str]:
        """Get the URI value for the given config key."""
        if not cls._loaded:
            cls.load_configs()

        return cls._configs.get(uri_key)

    @classmethod
    def get_all(cls) -> dict[str, str]:
        """Return all loaded URI configs as key-value pairs."""
        if not cls._loaded:
            cls.load_configs()

        return dict(cls._configs)
