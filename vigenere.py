#
# vigenere.py
#
# Paul Kaefer
# 2/23/2012
#
# Python implementation of the Vigenere Cipher.
#
# Information on the Vigenere Cipher may be found at
#   http://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
#

# lowercase: a=97; z=122
# uppercase: A=65; Z=90
def number_value(letter):
    #
    # INPUT:  a single character
    # OUTPUT: number value of that character
    #
    # a and A map to zero
    # z and Z map to 25
    #
    number = ord(letter)
    if ( number > 96 ) and ( number < 123 ):
        # lowercase letter
        return number - 97
    elif ( number > 64 ) and ( number < 91 ):
        # uppercase letter
        return number - 65
    else:
        return number

def character_value(number):
    #
    # INPUT:  number value (a, A = 0)
    # OUTPUT: character represented by that value
    #         (lowercase)
    #
    return chr(number + 97)

def encrypt(original_character, additional_value):
    # 
    # INPUT:  char original
    #         int additional_value
    # OUTPIT: char new_character
    #
    number = ord(original_character)
    additional_value = int(additional_value) # cast the string as an int
    if ( number > 96 ) and ( number < 123 ):
        # lowercase letter
        number = (number - 97 + additional_value)%26
    elif ( number > 64 ) and ( number < 91 ):
        # uppercase letter
        number = (number - 65 + additional_value)%26
    return character_value(number)

key = raw_input("\nEnter the key: ")
plaintext = raw_input("Enter the message: ")

key_size = len(key) - 1
msg_length = len(plaintext) - 1

finished = 0      # boolean finished_converting_message = FALSE
key_position = -1 # position within the key
msg_position = 0  # position within the plaintext

encrypted_message = ""

# plaintext to ciphertext
while (finished==0):
    key_position += 1
    if (key_position > key_size):
        key_position = 0
    encrypted_message += encrypt(plaintext[msg_position], number_value(key[key_position]))
    msg_position += 1
    if (msg_position > msg_length):
        finished = 1

print "\nCipher text= "+encrypted_message

cipher_text = plaintext
decrypted_message = ""

key_size = len(key) - 1
msg_length = len(plaintext) - 1

finished = 0      # boolean finished_converting_message = FALSE
key_position = -1 # position within the key
msg_position = 0  # position within the plaintext

while (finished==0):
    key_position += 1
    if (key_position > key_size):
        key_position = 0
    decrypted_message += encrypt(plaintext[msg_position], -1*number_value(key[key_position]))
    msg_position += 1
    if (msg_position > msg_length):
        finished = 1

print "\nPlain text=  "+decrypted_message

#print "\n\n"


