import os
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()


@dataclass
class Settings:
    app_env: str = os.getenv("APP_ENV", "dev")
    app_name: str = os.getenv("APP_NAME", "Gestor.ia API")
    secret_key: str = os.getenv("SECRET_KEY", "dev-secret")
    jwt_issuer: str = os.getenv("JWT_ISSUER", "gestor-ia")
    jwt_audience: str = os.getenv("JWT_AUDIENCE", "gestor-ia-users")
    jwt_expires_minutes: int = int(os.getenv("JWT_EXPIRES_MINUTES", "1440"))
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://gestor:gestor@localhost:5432/gestor_ia",
    )
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    field_encryption_key: str = os.getenv("FIELD_ENCRYPTION_KEY", "dev-fernet-key")
    storage_path: str = os.getenv("STORAGE_PATH", "./app/storage")
    rag_min_confidence: float = float(os.getenv("RAG_MIN_CONFIDENCE", "0.6"))


settings = Settings()
