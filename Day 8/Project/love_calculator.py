def calculate_love_score(name1, name2):
    combine_name = (name1+name2).lower()
    
    t = combine_name.count("t")
    r = combine_name.count("r")
    u = combine_name.count("u")
    e = combine_name.count("e")
    
    first_name = (t + r + u + e)
    
    l = combine_name.count("l")
    o = combine_name.count("o")
    v = combine_name.count("v")
    e = combine_name.count("e")
    
    second_name = (l + o + v + e)
    
    final = str(first_name) + str(second_name)
    print(final + "%")

calculate_love_score("Sinatrio Seto", "Naufal Fadhli Raihan Hiburan")