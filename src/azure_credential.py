import os
from dotenv import load_dotenv
from azure.identity import (
    DefaultAzureCredential,
    EnvironmentCredential,
    AzureDeveloperCliCredential,
    ManagedIdentityCredential,
)

load_dotenv()

from src.config import Config

def get_credential(app_env: str):
    """APP_ENV に応じた認証方法を返す"""
    if app_env == "azure_container_app":
        return ManagedIdentityCredential(client_id=os.getenv("AZURE_USER_ASSIGNED_IDENTITY_CLIENT_ID"))
    elif app_env == "local":
        return AzureDeveloperCliCredential(tenant_id=Config.AZURE_TENANT_ID)
    elif app_env == "local_container":
        return EnvironmentCredential()
    else:
        return DefaultAzureCredential()
