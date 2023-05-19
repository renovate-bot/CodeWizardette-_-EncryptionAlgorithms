from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

key_pair = DSA.generate(2048)

def sign(key_pair, message):
    hash_obj = SHA256.new(message)
    signer = DSS.new(key_pair, 'fips-186-3')
    signature = signer.sign(hash_obj)
    return signature

def verify(key_pair, message, signature):
    hash_obj = SHA256.new(message)
    verifier = DSS.new(key_pair, 'fips-186-3')
    try:
        verifier.verify(hash_obj, signature)
        print("İmza doğru.")
    except ValueError:
        print("İmza yanlış.")

message = b"Bu bir DSA örneği."

signature = sign(key_pair, message)

verify(key_pair.publickey(), message, signature)
