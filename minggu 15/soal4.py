def hitung(angka):
    if angka < 10:
        return(angka)
    
    return angka%10 + hitung(angka//10)

angka = int(input("Masukkan jumlah angka: "))
print("Jumlah digit adalah",hitung(angka))
