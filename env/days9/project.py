name =input("Welcome to the secret auction program\n \
            What is your name?.\n").lower()
your_bid = input("What's your bid?\n")
another_player = input("Are there any other bidders? Type 'yes' or 'no'.\n")
list_for_your_bid = []
players = [
   {
    "name": "albert",
    "your_bid": "$20"
  },
  {
    "name": "copernic",
    "your_bid": "$83",
  },
   
]
# stop_count = ""
def create_player(noun , number, ):
    fake_dict_player = {}
    fake_dict_player["name"] = noun
    fake_dict_player["your_bid"] = number 
    players.append(fake_dict_player  )

create_player(name, your_bid)
   
while another_player == "yes":
  name =input("Welcome to the secret auction program\n \
            What is your name?.\n").lower()
  your_bid = input("What's your bid?\n")
  another_player = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  create_player(name,your_bid)
if another_player == "no":
  for i in range(len(players ) ) :
    #  delete_dollard = players[i]["your_bid"].find("$")
    list_for_your_bid += players[i]["your_bid"].replace("$","")
    
    #  compare_to_rigth = i + 1
    #  print(f"This is the {players[i]['name']} length")
#    rigth_number = len(player[i]) + 1
#    if i["your_bid"] >  
     