alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']




# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    encrypted = []
    for letter in text:
        if letter in alphabet:
            index = (alphabet.index(letter) + shift) % 26
            encrypted.append(alphabet[index])
        else:
            encrypted.append(letter)
    encrypted_text = ''.join(encrypted)
    print('Here is the encrypted text: '+encrypted_text)


def decrypt(text, shift):
    decrypted = []
    for letter in text:
        if letter in alphabet:
            index = (alphabet.index(letter) - shift) % 26
            decrypted.append(alphabet[index])
        else:
            decrypted.append(letter)
    decrypted_text = ''.join(decrypted)
    print('Here is the decrypted text: ' + decrypted_text)

is_done = True
while is_done == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)
    else:
        direction = input("Sorry, input not understood, Type 'encode' to encrypt, type 'decode' to decrypt:\n")


    done = input('Type "yes" if you would like to go again, otherwise type "no"\n').lower()
    if done == 'no':
        is_done = False
    else:
        is_done = True



