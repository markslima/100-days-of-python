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
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(name, visit_count, cities_list):
    # country = input(f"Which country did you visit?\n ")
    # visits = input("And how many times did you visit?\n ")
    # cities = input("Which cities did you visit?")

    new_country = {}
    new_country["country"] = name
    new_country["visits"] = visit_count
    new_country["cities"] = cities_list
    travel_log.append(new_country)
    # print("\n" * 15)
    
    # print(f"You have visited {new_country[name]} {new_country[visit_count]} times.")
    # print(f"You have been to {new_country[cities_list]}.")



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)




