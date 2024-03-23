alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
# to_encrypt = False
cipher_text = ""
def encrypt(text,shift):
    it_work = ""
    plain_text = "" 
    if direction =="encode":
        for i in range(len(text)):
          shiting_leng = alphabet.index(text[i]) + shift
        #   print(cipher_text)
        #   print(alphabet[shiting_leng])
          it_work +=  alphabet[shiting_leng]
          print(it_work)
        #   cipher_text = text
        #   cipher_text += alphabet[shiting_leng]

        #   print(f"Look the message agent 007 {cipher_text}")
    elif direction == "decode":
        plain_text = text
        print(f"The message real sense {plain_text}")
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
encrypt(text,shift=shift)