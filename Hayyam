def omer_hayyam_encryption(text):
    letter_to_number = {'a': 1, 'b': 2, 'c': 3, ...}  # Harf-numara eşleme tablosu

    # Metni sayı dizisine çevir
    number_sequence = [letter_to_number[letter] for letter in text]

    # Ömer Hayyam'ın öklidyen algoritması
    gcd = number_sequence[0]
    for num in number_sequence[1:]:
        gcd = calculate_gcd(gcd, num)  # Öklidyen algoritmasını uygula

    # Sayı dizisini bölerek yeni bir dizi oluştur
    encrypted_sequence = [num // gcd for num in number_sequence]

    # Şifreli metni oluştur
    encrypted_text = ''.join([str(num) for num in encrypted_sequence])
    return encrypted_text

def omer_hayyam_decryption(encrypted_text):
    # Şifreli metni sayı dizisine çevir
    encrypted_sequence = [int(encrypted_text[i:i+2]) for i in range(0, len(encrypted_text), 2)]

    # Öklidyen algoritmasını tersine çevirerek orijinal sayı dizisini elde et
    original_sequence = [num * encrypted_sequence[0] for num in encrypted_sequence]

    # Orijinal metni elde et
    original_text = ''.join([number_to_letter[number] for number in original_sequence])
    return original_text

# Örnek kullanım
plaintext = "merhaba"
encrypted = omer_hayyam_encryption(plaintext)
print("Şifrelenmiş Metin:", encrypted)
decrypted = omer_hayyam_decryption(encrypted)
print("Orijinal Metin:", decrypted)
