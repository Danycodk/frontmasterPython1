alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
# to_encrypt = False
cipher_text = ""
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text,shift):
    if direction =="encode":
        for i in range(len(text)):
            # print(text[i])
          shiting_leng = alphabet.index(text[i]) + shift
        #   print(f"what the value of the shiftting_len {shiting_leng}")
          cipher_text = text
        #   print(alphabet[shiting_leng])
          cipher_text += alphabet[shiting_leng]
        #   text[i] = alphabet[shiting_leng]
        #   print(f"Agent here is the message {cipher_text}")
          print(f"Look the message agent 007 {cipher_text}")
    elif direction == "decode":
    #    plain_text = text 
       print("nothing")
    #    print(f"The message real sense {plain_text}")
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
encrypt(text,shift=shift)
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 