country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
dict_new_country = { }
def add_new_country(country, visits, list_of_cities):
  dict_new_country["country"] = country
  dict_new_country["visits"] = visits 
  # split_in_cities_in_list = list_of_cities.split(",")
  # if list_of_cities.find(",") != -1:
     # dict_new_country["list_of_cities"] = list_of_cities.split(",")
  # else:
      # dict_new_country["list_of_cities"] = list_of_cities
  dict_new_country["list_of_cities"] = list_of_cities
  travel_log.append(dict_new_country)
  
print (dict_new_country)

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")