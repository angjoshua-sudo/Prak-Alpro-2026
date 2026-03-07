def perkalian(angka1, angka2):
    akhir = 0
    i = 1
    teks = ""

    while angka1 >= i:
        akhir = akhir + angka2
        teks = teks + str(angka2) 

        if angka1 > i:
            teks = teks + " + "

        i += 1
    print (f"{angka1} x {angka2} = {teks} = {akhir}")
        
perkalian(6,5)
perkalian(7,10)

