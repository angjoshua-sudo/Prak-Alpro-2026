bulan = input("Masukkan bulan (1-12): ")

try:
    bulan = int(bulan)
    if bulan == 1:
        print("jumlah hari: 31")
    if bulan == 2:
        print("jumlah hari: 29")
    if bulan == 3:
        print("jumlah hari: 31")
    if bulan == 4:
        print("jumlah hari: 30")
    if bulan == 5:
        print("jumlah hari: 31")
    if bulan == 6:
        print("jumlah hari: 30")
    if bulan == 7:
        print("jumlah hari: 31")
    if bulan == 8:
        print("jumlah hari: 31")
    if bulan == 9:
        print("jumlah hari: 30")
    if bulan == 10:
        print("jumlah hari: 31")
    if bulan == 11:
        print("jumlah hari: 30")
    if bulan == 12:
        print("jumlah hari: 31")
except:
    print("Input bulan harus berupa angka antara 1-12!")    