from pydantic import BaseSettings

class Settings(BaseSettings):
    # Environment configuration
    environment: str = "development"

    # Database settings
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str

    # JWT settings
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    jwt_expiration_minutes: int = 30

    # API keys
    api_key: str

    # Security settings
    enabled_security_features: list = ["feature1", "feature2"]

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()