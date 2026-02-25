usia = input("Masukkan usia anda: ")
try:
    usia = int(usia)
    if usia <= 5:
        print("Balita")
    elif usia <=11:    
        print("Kanak-kanak")
    elif usia <= 25:
        print("Remaja")
    elif usia <= 45:
        print("Dewasa")
    else:
        print("Lansia")
except:
    print("Usia harus berupa angka!")    