from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key_pair = RSA.generate(2048)

public_key = key_pair.publickey()

def encrypt(public_key, plaintext):
    encryptor = PKCS1_OAEP.new(public_key)
    ciphertext = encryptor.encrypt(plaintext)
    return ciphertext

def decrypt(key_pair, ciphertext):
    decryptor = PKCS1_OAEP.new(key_pair)
    plaintext = decryptor.decrypt(ciphertext)
    return plaintext

plaintext = b"Bu bir RSA örneği."

ciphertext = encrypt(public_key, plaintext)

decryptedtext = decrypt(key_pair, ciphertext)

print("Orijinal Metin: ", plaintext)
print("RSA ile Şifreli Metin: ", ciphertext)
print("RSA ile Çözülen Metin: ", decryptedtext)
