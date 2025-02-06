from azure.identity import ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    config_value = os.getenv('CONFIG_VALUE', 'World')
    #return f"Hello, {config_value}!"

if __name__ == '__main__':
    credential = ManagedIdentityCredential()
    key_vault_url = "https://keyvaultcap4.vault.azure.net/"
    secret_client = SecretClient(vault_url=key_vault_url, credential=credential)
    secret = secret_client.get_secret("my-secret")
    print(f"Retrieved secret: {secret.value}")

    app.run(host='0.0.0.0', port=80)




