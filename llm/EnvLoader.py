import os
from pathlib import Path


class EnvLoader:
    _project_root = Path(__file__).resolve().parent.parent
    _env_file_path = _project_root / ".env"
    _env_vars: dict[str, str] = {}

    @classmethod
    def load_env(cls, env_file_path: str | None = None) -> dict[str, str]:
        """Load all environment variables from the .env file."""
        env_path = Path(env_file_path) if env_file_path else cls._env_file_path
        cls._env_vars = {}

        if not env_path.exists():
            raise FileNotFoundError(f".env file not found at {env_path}")

        for raw_line in env_path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()

            if not line or line.startswith("#"):
                continue

            if line.startswith("export "):
                line = line[len("export ") :].strip()

            if "=" not in line:
                continue

            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()

            if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
                value = value[1:-1]

            cls._env_vars[key] = value
            os.environ[key] = value

        return dict(cls._env_vars)

    @classmethod
    def get_value(cls, key: str) -> str | None:
        """Return the value for the given key."""
        if not cls._env_vars:
            cls.load_env()

        return cls._env_vars.get(key)

    @classmethod
    def get_all(cls) -> dict[str, str]:
        """Return all loaded environment variables as key-value pairs."""
        if not cls._env_vars:
            cls.load_env()

        return dict(cls._env_vars)
