from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # App Config
    environment: str = "development"
    debug: bool = True
                
    # GCP Config
    gcp_project_id: str
                            
    # Keys & Secrets
    supabase_url: str
    supabase_key: str
    gemini_api_key: str
    twilio_account_sid: str
    twilio_auth_token: str
                                                        
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
