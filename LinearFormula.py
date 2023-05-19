alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
new_message = ''

message = 'hello world'

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position + key) % 26
        new_character = alphabet[new_position]
        new_message += new_character
    else:
        new_message += character

print(new_message)
