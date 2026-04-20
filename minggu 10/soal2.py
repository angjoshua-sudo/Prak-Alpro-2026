file1 = input("nama file1: ")
isi_soal = []
isi_jawaban = []
try: 
    handle = open(file1)
    for line in handle:
            line = line.strip()
            line = line.split("||")
            soal = line[0].strip()
            jawaban = line[1].strip().lower()
            isi_soal.append(soal)
            isi_jawaban.append(jawaban)

    for i in range (len(isi_soal)):
        print(isi_soal[i])
        user_jawab = input("jawab: ")
        user_jawab = user_jawab.strip().lower()
        if user_jawab == isi_jawaban[i]:
            print("Jawaban benar!")
        else:
            print("Jawaban salah!")

    handle.close()

except:
    print("file tidak ditemukan")

