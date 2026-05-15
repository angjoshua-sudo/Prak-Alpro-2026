import string
file1 = input('Masukkan nama file pertama: ')
file2 = input('Masukkan nama file kedua: ')
try: 
    handle = open(file1)
    handles = open(file2)
except:
    print("File tidak ditemukan atau tidak bisa dibaca")
    exit()

kata1 = []
for line in handle:
    line = line.translate(str.maketrans('','', string.punctuation))
    line = line.lower()
    pisah = line.split()
    for kata in pisah:
        kata1.append(kata)

kata2 = []
for line in handles:
    line = line.translate(str.maketrans('','', string.punctuation))
    line = line.lower()
    pisah = line.split()
    for kata in pisah:
        kata2.append(kata)

kata1 = set(kata1)
kata2 = set(kata2)

gabung = kata1 & kata2
print(gabung)
handle.close()
handles.close()
