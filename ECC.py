from Crypto.PublicKey import ECC

key = ECC.generate(curve='P-256')

private_key = key.export_key(format='PEM')
public_key = key.public_key().export_key(format='PEM')

message = b"Hello, World!"

encrypted_message = key.public_key().encrypt(message, None)

decrypted_message = key.decrypt(encrypted_message)

print("Özel Anahtar: ", private_key.decode('utf-8'))
print("Açık Anahtar: ", public_key.decode('utf-8'))
print("Orijinal Mesaj: ", message)
print("Şifreli Mesaj: ", encrypted_message)
print("Çözümlenmiş Mesaj: ", decrypted_message)
