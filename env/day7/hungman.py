
import random
word_list = ["aardvark", "baboon", "camel"]

random_word = random.randint(0,len(word_list)-1)#  Randomly choose a word

chosen_word = word_list[random_word] # stock the 
user_word = input("guess the letter\n"),lower()# Ask the user to guess


cancel_the_game = 0
test_letter = chosen_word.find(user_word)

# print(f"this is to see if it is a number{random_word}")

while cancel_the_game < 2 :
  if test_letter != -1 :
     chosen_word.replace(user_word,"")
     second_user_word = input("guest a other letter")
     if

  else: #test_letter == -1 :
    # if (0,len(chosen_word)) : 
      cancel_the_game += 1
      if test_letter == -1:
         cancel_the_game += 1
    #   print(f"sorry {cancel_the_game} loose")
    #   print(cancel_the_game)


# while cancel_the_game < 2:
  
