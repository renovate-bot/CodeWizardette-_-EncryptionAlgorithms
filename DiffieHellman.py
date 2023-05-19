from pyDH import DiffieHellman

dh_obj1 = DiffieHellman()
dh_obj2 = DiffieHellman()

public_key1 = dh_obj1.gen_public_key()
public_key2 = dh_obj2.gen_public_key()

shared_key1 = dh_obj1.gen_shared_key(public_key2)
shared_key2 = dh_obj2.gen_shared_key(public_key1)

assert shared_key1 == shared_key2

print("Açık Anahtar 1: ", public_key1)
print("Açık Anahtar 2: ", public_key2)
print("Ortak Anahtar: ", shared_key1)
