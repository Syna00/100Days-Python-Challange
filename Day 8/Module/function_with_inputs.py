def greet(nama):
    print(f"Halo sayangku {nama}, kamu sudah pulang? selamat datang di rumah")
    jawaban = input(f"Oh iya, ayang {nama} udah makan? \n").lower()
    if jawaban == "sudah":
        print(f"owhh sudah ya, eh kamu makin diliat makin ganteng aja, ayang {nama} emang ganteng banget")
    elif jawaban == "belum":
        print(f"yaudah sayangku {nama}, aku bikinin makan dulu yaa")

greet("Seto")