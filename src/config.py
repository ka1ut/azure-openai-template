import os
from dotenv import load_dotenv

load_dotenv()

class AvilableModels:
    """
    利用可能な OpenAI モデル
    """
    def __init__(self):
        self.models = [
            "openai-edu-info-suzuka",
            "gpt-4o",
            "gpt-4o-mini",
            "text-embedding-3-large",
            "text-embedding-3-small",
            "text-embedding-ada-002",
            "openai-edu-info-suzuka-swc",
            "o1-mini",
            "gpt-4o-realtime-preview",
            "gpt-4o-audio-preview",
            "tts-hd",
            "whisper",
            "dall-e-3"
        ]

class Config:
    """環境変数から設定値を読み込む設定クラス"""
    APP_ENV = os.getenv("APP_ENV", "local")
    AZURE_TENANT_ID = os.getenv("AZURE_TENANT_ID")
    AZURE_CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
    AZURE_CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-08-01-preview")
    # 必要なら他の環境変数も追加できます


config = Config()