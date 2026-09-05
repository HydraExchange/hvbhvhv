```python
import pathlib
from pydantic_settings import BaseSettings, SettingsConfigDict


def get_path_env() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parent.parent / ".env"


class Settings(BaseSettings):
    BOT_TOKEN: str = "8258401803:AAEHZTCKEa74IaxtvSlASJEnvxyODW4-sAI"
    ADMIN_ID: int = 7861322479

    model_config = SettingsConfigDict(
        env_file=get_path_env(),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    def get_db_url(self) -> str:
        db_path = pathlib.Path(__file__).resolve().parent.parent / "db" / "base.db"
        return str(db_path)


settings = Settings()
```
