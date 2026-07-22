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

#TODO-1 : Creat a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
#TODO-2 : Inside the 'encrypt()' function, shift the letter of the 'original_text' forward in alphabet by the shift amount and print the encrypted text.
# hello 1
def encrypt(original_text, shift_amount):
    chiper_text = ""
    
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        #TODO-4 : What happens if you try shift z forwards by 9? can you fix the code?
        shifted_position %= len(alphabet)
        chiper_text += alphabet[shifted_position]
    print(f"Here is the encoded result : {chiper_text}")


#TODO-3 : Call the 'encrypt()' functions and pass the user inputs. You should be able to test  the code and encrypt a massage   

encrypt(original_text=text, shift_amount=shift)
