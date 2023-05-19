from Crypto.Util import number
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

def eg_encrypt(m, pub_key):
    p, g, h = pub_key
    k = number.getRandomRange(1, p-1)
    c1 = pow(g, k, p)
    s = pow(h, k, p)
    c2 = [(ord(m[i]) * s) % p for i in range(len(m))]
    return c1, c2

def eg_decrypt(c, priv_key):
    c1, c2 = c
    x, p = priv_key
    s = pow(c1, x, p)
    m = [chr((c2[i] * pow(s, p-2, p)) % p) for i in range(len(c2))]
    return ''.join(m)

message = "Merhaba, bu bir Elgamal şifreleme algoritması örneğidir."
key = get_random_bytes(16)  # AES anahtarı oluştur
iv = get_random_bytes(AES.block_size)  # AES şifreleme modu
cipher = AES.new(key, AES.MODE_CBC, iv)  # AES şifreleyici oluştur
ciphertext = cipher.encrypt(message.encode('utf-8'))  # Metin AES ile şifrele

p = number.getPrime(1024)
g = number.getRandomRange(1, p-1)
x = number.getRandomRange(1, p-2)
h = pow(g, x, p)
pub_key = (p, g, h)
priv_key = (x, p)

eg_ciphertext = eg_encrypt(ciphertext, pub_key)

decrypted_ciphertext = eg_decrypt(eg_ciphertext, priv_key)

cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_message = cipher.decrypt(decrypted_ciphertext.encode('utf-8')).decode('utf-8')

print("message: ", message)
print("AES message: ", ciphertext)
print("Elgamal message: ", eg_ciphertext)
print("Elgamal last message: ", decrypted_ciphertext)
print("AES lastmessage: ", decrypted_message)
