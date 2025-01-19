import base64

# Encrypt the API key
def encrypt_api_key(api_key: str) -> str:
    return base64.b64encode(api_key.encode()).decode()

# Decrypt the API key
def decrypt_api_key(encrypted_key: str) -> str:
    return base64.b64decode(encrypted_key.encode()).decode()

# Example usage
api_key = ""
encrypted_key = encrypt_api_key(api_key)
decrypted_key = decrypt_api_key(encrypted_key)


print(f"Encrypted API Key: {encrypted_key}")
print("\n \n")
print(f"Decrypted API Key: {decrypted_key}")