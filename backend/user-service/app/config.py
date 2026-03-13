from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """
    Application configuration settings loaded from environment variables.
    
    This class uses Pydantic's BaseSettings to automatically load values from:
    1. Environment variables
    2. .env file (if present)
    
    Benefits:
    - Type validation (ensures PORT is an integer, etc.)
    - Default values for optional settings
    - Automatic .env file loading
    - No hardcoded secrets in code
    """
    
    # Application Settings
    APP_NAME: str = "Taxi Booking User Service"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # Database Settings
    DB_HOST: str = Field(default="postgres-db", description="Database host")
    DB_PORT: int = Field(default=5432, description="Database port")
    DB_NAME: str = Field(default="taxi_db", description="Database name")
    DB_USER: str = Field(default="taxi_user", description="Database user")
    DB_PASSWORD: str = Field(default="taxi_pass", description="Database password")
    
    # Server Settings
    SERVER_HOST: str = Field(default="0.0.0.0", description="Server host")
    SERVER_PORT: int = Field(default=8000, description="Server port")
    
    class Config:
        """
        Pydantic configuration class.
        
        env_file: Specifies the .env file to load
        case_sensitive: Makes environment variable names case-sensitive
        """
        env_file = ".env"
        case_sensitive = True
    
    @property
    def database_url(self) -> str:
        """
        Constructs the database connection URL.
        
        Returns:
            str: PostgreSQL connection string
            
        Example:
            postgresql://taxi_user:taxi_pass@postgres-db:5432/taxi_db
        """
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


# Create a single instance of settings to be imported throughout the app
# This ensures configuration is loaded once and reused
settings = Settings()
