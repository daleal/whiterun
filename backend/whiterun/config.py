import os
from typing import List


class Settings:
    database_url: str = os.environ["DATABASE_URL"].replace(
        "postgres://", "postgresql://"
    )
    fintoc_secret_key: str = os.environ["FINTOC_SECRET_KEY"]
    fintoc_webhook_secret: str = os.environ["FINTOC_WEBHOOK_SECRET"]
    webhook_tolerance_seconds: int = int(
        os.environ.get("WEBHOOK_TOLERANCE_SECONDS", "30")
    )
    cors_allowed_origins: List[str] = list(
        filter(lambda x: x, os.environ.get("CORS_ALLOWED_ORIGINS", "").split(" "))
    )


settings = Settings()
