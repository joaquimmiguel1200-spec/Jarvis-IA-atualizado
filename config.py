# Python 3.12+
from pydantic import Field
from pydantic_settings import BaseSettings

class JarvisConfig(BaseSettings):
    """Configurações centralizadas do sistema JARVIS."""
    HOTWORD: str = "jarvis"
    VOICE_RATE: int = 180
    VOICE_VOLUME: float = 0.9
    CLAP_THRESHOLD: int = 2000  # Sensibilidade para detecção de palmas
    CHUNK_SIZE: int = 1024
    
    # Caminhos de Aplicativos (Ajustar conforme o SO)
    VS_CODE_PATH: str = "code" # Assume que está no PATH
    SLACK_PATH: str = "slack"
    
    class Config:
        env_prefix = "JARVIS_"

config = JarvisConfig()