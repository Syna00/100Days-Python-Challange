tingkat_kegantengan = {"seto": "dia berada di ganteng tingkat ekstrim",
                       "naufal": "dia lumayan ganteng",
                       "ilyas": "yaa boleh lah"}
# print(tingkat_kegantengan["seto"])
tingkat_kegantengan["wildan"] = "ni orang si kacau ye gantengnya"
    # print(tingkat_kegantengan["wildan"])

empty_list = {}

# Wipe an existing dictionary

    # tingkat_kegantengan = {}
    # print(tingkat_kegantengan)

#Edit an item in a dictionary

tingkat_kegantengan["seto"] = "dia sudah berada di puncak kegantengan"
    # print(tingkat_kegantengan["seto"])

# Loop through a dictionary
    # for ganteng in tingkat_kegantengan:
    #     print(ganteng)

# Loop through a dictionary
for kunci in tingkat_kegantengan:
    print(kunci)
    print(tingkat_kegantengan[kunci])