from azure.identity import (
    get_bearer_token_provider
)
from openai import AzureOpenAI


from src.config import config
from src.azure_credential import get_credential

def main():
    credential = get_credential(config.APP_ENV)

    token_provider = get_bearer_token_provider(credential, "https://cognitiveservices.azure.com/.default")

    client = AzureOpenAI(
        api_version=config.AZURE_OPENAI_API_VERSION,
        azure_endpoint=config.AZURE_OPENAI_ENDPOINT,
        azure_ad_token_provider=token_provider
    )

    # Chat API の呼び出し例
    response = client.chat.completions.create(
        model="gpt-4o",
        max_tokens=100,
        messages=[
            {"role": "system", "content": "あなたは学校の先生です。"},
            {"role": "user", "content": "英語の学習で大切なことは何ですか？"}
        ]
    )

    print(response)
    print("="*10 + "ai response" + "="*10)
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
