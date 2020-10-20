import hashlib
from cryptography.fernet import Fernet

hash_object = hashlib.sha3_256()
# Creating a hash object

hash_object.update(b'Calvin')
# content to hash

hexO = hash_object.hexdigest()

# print(hexO)

key = Fernet.generate_key()

print(key)

cipher = Fernet(key)
# Create a cipher

print(cipher.encrypt(b'Calvin'))

other_cipher = Fernet(b'6Auyg4bKj0AiGD3AvVq09JB21jESVURRTV6SJ0geAJI=')

decrypted_message = other_cipher.decrypt(b'gAAAAABfjrl0nNEcLzFWk5syTlz9agHC-G9oxpQqu00KlebKRtqr-YiCEnLSdJSN5fnrHzf22KR_J-u7MG8sChHPzeBGW_WQ9Q==')

print(decrypted_message)