import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
##############################################111111111111111111
letters_total = ""
for i in range(0, nr_letters +1):# loop 0 and The number of THE USER
  random_letters = random.randint(0,len(letters)) # give a random number between 0 - number length of letter
  letters_total += letters[random_letters]
#   print(letters[random_letters])
#   
##############################################
##############################################22222222222222222222222222222
numbers_total = ""
for i in range(0, nr_numbers +1):# loop 0 and The number of THE USER
  random_numbers = random.randint(0,len(numbers) -1) # give a random number between 0 - number length of letter
  numbers_total += numbers[random_numbers]
  print(numbers[random_numbers])
print(numbers_total)
##############################################
##############################################33333333333333333333
symbols_total = ""
for i in range(0, nr_symbols +1):# loop 0 and The number of THE USER
  random_symbols = random.randint(0,len(symbols) -1) # give a random number between 0 - number length of letter
  symbols_total += symbols[random_symbols]
#   print(symbols[random_symbols])
#   
##############################################
real_total = symbols_total + numbers_total + letters_total
print(f" There the password {real_total} winnnnnnnnnn!!!!!!!")
  