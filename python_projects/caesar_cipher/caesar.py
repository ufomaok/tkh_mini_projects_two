import sys


def encrypt(message, k):
    #Creating alphabet string
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    
    #For loop that will iterate through letters and shift them according to key. 
    #The % len alphabet is also modulus 26, which will keep our letters within range. 
    for letter in message:
        if letter in alphabet:
            letter_ind = (alphabet.find(letter) + key) % len(alphabet)

            result = result + alphabet[letter_ind]
        
        else:
            result = result + letter

    return result
   

def decrypt(message, k):
    return


if __name__ == "__main__":
    # take in first arg as word
    message = sys.argv[1]
    # take in second arg as int key
    key = int(sys.argv[2])


    # encrypt your word
    encrypted = encrypt(message, key)

    # decrypt your encrypted word
    decrypted = decrypt(encrypted, key)


    print("Your encrypted word is", encrypted)
    print("Your decrypted word is", decrypted)
