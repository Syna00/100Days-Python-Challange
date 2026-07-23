capital = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nested list in dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

#print Lille 
# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

# print(nested_list[2][1])

travel_log = {
    "France" : {
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visited" : 12
    },
    "Germany": {
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
        "total_visited" : 5
    }
}

print(travel_log["Germany"]["cities_visited"][0])