def encrypt(text,s):
    encrypted_string = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        
        if (char.isupper()):
            encrypted_string += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            print('the entered string is not upper case')
            quit()

    return encrypted_string



#check the above function
text = input('enter the text here : ') #DEFENDTHEFORT
s = int(input('enter the key for encryption : '))

print ("Plain Text : " + text)
print ("Shift pattern : " + str(s))
print ("Cipher: " + encrypt(text,s))

text_to_decrypt = encrypt(text,s)


#===========================================================
def decrypt(text,s):
    decrypted_string = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        
        if (char.isupper()):
            decrypted_string += chr((ord(char) - s - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            print('the entered string is not upper case')
            quit()

    return decrypted_string

print('decripted : ',end="")
print(decrypt(text_to_decrypt,s))