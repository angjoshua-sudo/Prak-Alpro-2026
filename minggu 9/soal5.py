from datetime import datetime

kalimat = input("Masukkan kalimat: ")
temp = []

kalimat = kalimat.split(' ')
for i in kalimat:
    simpan = i.strip(",()!?./;:'\"")
    jadi = simpan.split("-")
    
    if len(jadi) == 3 and all(j.isdigit() for j in jadi):
        temp.append(simpan)
        
for j in temp:
    tanggal = datetime.strptime(j, "%Y-%m-%d")
    sekarang = datetime.now()

    selisih = (sekarang - tanggal).days

    ubah_tanggal = tanggal.strftime("%d-%m-%Y")
    print(f"{ubah_tanggal} selisih {selisih} hari")

