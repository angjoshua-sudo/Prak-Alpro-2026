def ganjil(bawah, atas):
    cek_bawah = bawah
    teks = ""

    if bawah < atas:

        if cek_bawah % 2 == 0:
            cek_bawah = cek_bawah + 1

        for i in range(cek_bawah, atas +1, 2):
            teks = teks + str(i)
            if i + 2 <= atas:
                teks = teks + ", "
        print(f"bawah = {bawah}, atas = {atas}. Karena bawah < atas, berati dari kecil ke besar, maka hasilnya adalah: {teks}.")

    else:
        
        if cek_bawah % 2 == 0:
            cek_bawah = cek_bawah - 1

        for i in range(cek_bawah, atas - 1, -2):
            teks = teks + str(i)
            if i - 2 >= atas:
                teks = teks + ", "
        print(f"bawah = {bawah}, atas = {atas}. Karena bawah > atas, berati dari besar ke kecil, maka hasilnya adalah: {teks}.")


ganjil(10,30)
ganjil(97,82)


