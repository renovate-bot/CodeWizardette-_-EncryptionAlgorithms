#################################
def omer_hayyam_encryption(text):
    encrypted_text = ''
    for char in text:
        encrypted_char = chr(ord(char) + 3)  # Harf kodunu 3 artırarak şifrele
        encrypted_text += encrypted_char
    return encrypted_text

def omer_hayyam_decryption(encrypted_text):
    decrypted_text = ''
    for char in encrypted_text:
        decrypted_char = chr(ord(char) - 3)  # Şifreyi çözerek orijinal harfi elde et
        decrypted_text += decrypted_char
    return decrypted_text
#################################

def omer_hayyam_encryption(text, key):
    encrypted_text = ""
    for char in text:
        encrypted_char = chr((ord(char) * key) % 256)  # Karakteri key ile çarp ve modulo 256 alarak şifrele
        encrypted_text += encrypted_char
    return encrypted_text

def omer_hayyam_decryption(encrypted_text, key):
    decrypted_text = ""
    inverse_key = pow(key, -1, 256)  # Anahtarın tersini hesapla (mod 256)
    for char in encrypted_text:
        decrypted_char = chr((ord(char) * inverse_key) % 256)  # Şifreyi çöz ve orijinal karakteri elde et
        decrypted_text += decrypted_char
    return decrypted_text

plaintext = "merhaba"
key = 17  # Rastgele bir anahtar seçimi
encrypted = omer_hayyam_encryption(plaintext, key)
print("Şifrelenmiş Metin:", encrypted)
decrypted = omer_hayyam_decryption(encrypted, key)
print("Orijinal Metin:", decrypted)
#####################################

def omer_hayyam_encryption(text):
    letter_to_number = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
                           'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
                           't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28,
                           'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37,
                           'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46,
                           'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52, ' ': 53, ',': 54, '!': 55,
                           'Ö': 56, 'ü': 57, 'ğ': 58, 'ç': 59, 'ı': 60, 'ş': 61, 'ö': 62, 'Ü': 63, 'İ': 64,
                           'Ğ': 65, 'Ç': 66, 'I': 67, 'Ş': 68, '(': 69, ')': 70, '-': 71, ':': 72, ';': 73,
                           '\'': 74, '"': 75, '/': 76, '\\': 77, '[': 78, ']': 79, '{': 80, '}': 81, '@': 82,
                           '#': 83, '$': 84, '%': 85, '^': 86, '&': 87, '*': 88, '_': 89, '+': 90, '=': 91,
                           '<': 92, '>': 93, '|': 94, '?': 95}  # Harf-numara eşleme tablosu

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

    # Orijinal 
    original_text = ''.join([number_to_letter[number] for number in original_sequence])
    return original_text

plaintext = "merhaba"
encrypted = omer_hayyam_encryption(plaintext)
print("Şifrelenmiş Metin:", encrypted)
decrypted = omer_hayyam_decryption(encrypted)
print("Orijinal Metin:", decrypted)
