def greet_with_name(name, location):
    print(f"Hello i am {name}")
    print(f"i live in {location}")

greet_with_name("Afifa", "Johannes_Torka_Str 19")

#greet_with_name() parameter
#greet_with_name(argument)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

direction = input("Type 'encode' to encrypt type to 'decode' to decrypt:\n")

text = input("type your message:\n").lower()
shift= int(input("Type the shift number: \n"))

def caesar(start_text, shift_amount,cipher_direction):
    endd
def encrypt (plain_text, shift_amount):
    cipher_text= ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position+shift_amount
        new_letter = alphabet[new_position]
        cipher_text+= new_letter
    print(f"the encoded text is {cipher_text}")


encrypt(plain_text=text,shift_amount=shift)

