def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Kamu tidak memasukkan input dengan benar"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return(f"Nama kamu adalah : {formated_f_name} {formated_l_name}")

output = format_name(input("Masukkan nama depan kamu : "), input("Masukkan nama belakang kamu : "))
print(output)