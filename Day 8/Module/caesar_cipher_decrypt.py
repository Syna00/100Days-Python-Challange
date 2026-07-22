logo = '''
                                             _       _                 
                                            (_)     | |                
  ___  __ _  ___  ___  __ _ _ __    ___ _ __ _ _ __ | |__   ___ _ __   
 / __|/ _` |/ _ \/ __|/ _` | '__|  / __| '__| | '_ \| '_ \ / _ \ '__|  
| (__| (_| |  __/\__ \ (_| | |    | (__| |  | | |_) | | | |  __/ |     
 \___|\__,_|\___||___/\__,_|_|     \___|_|  |_| .__/|_| |_|\___|_|     
                                              | |                      
                                              |_|                      
'''

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt : \n").lower()
text = input("Type your massage : \n").lower()
shift = int(input("The type shift number : \n"))

# def encrypt(original_text, shift_amount):
#     chiper_text = ""
    
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         chiper_text += alphabet[shifted_position]
#     print(f"Here is the encoded result : {chiper_text}")

# encrypt(original_text=text, shift_amount=shift)

# #TODO-1 : Creat a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs
# #TODO-2 : inside the 'decrypt()' function, shift each letter of the 'original_text' forwards in the alphabet backwards by the 'shift_amount' and print the decrypted text.

# def decrypt(original_text, shift_amount):
#     output_text = ""

#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         output_text += alphabet[shifted_position]
#     print(f"Here is the encoded result : {output_text}")

# decrypt(original_text=text, shift_amount=shift)

#TODO-3 : Combine the 'encrypt()' and 'decrypt() function into a single function called caesar().

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result : {output_text}")

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
