import sys

#Creating definition for encryption, taking in parameters message and k
def encrypt(message, k):

    #String will store the encrypted message
    answer = ""

    #Creating for loop that will go through each charater in the message
    for character in message:

        #If statement checking conditions for characters in alphabet (using ASCII system)
        if character.isalpha():

            #First value in ASCII for both upper (65 represents A) and lowercase letters (97 represents a)
            #Charaters modified and wrapped inside of alpabet range (modulus 26 allows us to wrap characters around alphabet)
            first_value = 65 if character.isupper() else 97 
            modified_text = chr(first_value + (ord(character) - first_value + k)% 26) 
            answer += modified_text
        #Characters that aren't in alphabet accounted for
        else:
            answer += character
    return answer

#Note: Decrypt code is nearly identical to encrypt code, with the exception of how we shift k, or key

#Creating definition for decryption code, taking in parameters message and k
def decrypt(message, k):

    #String will store the decrypted message
    answer = ""

    #Creating for loop that will go through each charater in the message
    for character in message:

        #If statement checking conditions for characters in alphabet (using ASCII system)
        if character.isalpha():

            #First value in ASCII for both upper (65 represents A) and lowercase letters (97 represents a)
            first_value = 65 if character.isupper() else 97 

            #Charaters modified and wrapped inside of alpabet range (modulus 26 remainder)
            #Unlike in encryption code where use addition operator to shift k (key) forwards, we use subtraction operator to shift k backwards
            modified_text = chr(first_value + (ord(character) - first_value - k)% 26) 
            answer += modified_text

         #Characters that aren't in alphabet accounted for
        else:
            answer += character
    return answer
   
#Running file as script
if __name__ == "__main__":
    # take in first arg as word
    message = sys.argv[1]
    # take in second arg as int key
    key = int(sys.argv[2])


    # encrypt your word
    encrypted = encrypt(message, key)

    # decrypt your encrypted word
    decrypted = decrypt(encrypted, key)

    #Printing encrypted and decrypted word in terminal 
    print("Your encrypted word is", encrypted)
    print("Your decrypted word is", decrypted)
