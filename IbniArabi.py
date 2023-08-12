def ibn_arabi_encryption(text):
    letter_to_number = {'a': 1, 'b': 2, 'c': 3, ...}  # Harf-numara eşleme tablosu

    # Metni sayı dizisine çevir
    number_sequence = [letter_to_number[letter] for letter in text]

    # İbn Arabi'nin matematiksel işlemi
    transformed_sequence = [number * 2 + 3 for number in number_sequence]

    # Şifreli metni oluştur
    encrypted_text = ''.join([str(num) for num in transformed_sequence])
    return encrypted_text

def ibn_arabi_decryption(encrypted_text):
    # Şifreli metni sayı dizisine çevir
    encrypted_sequence = [int(encrypted_text[i:i+2]) for i in range(0, len(encrypted_text), 2)]

    # Ters işlem
    original_sequence = [(number - 3) // 2 for number in encrypted_sequence]

    # Orijinal 
    original_text = ''.join([number_to_letter[number] for number in original_sequence])
    return original_text

plaintext = "merhaba"
encrypted = ibn_arabi_encryption(plaintext)
print("Şifrelenmiş Metin:", encrypted)
decrypted = ibn_arabi_decryption(encrypted)
print("Orijinal Metin:", decrypted)
