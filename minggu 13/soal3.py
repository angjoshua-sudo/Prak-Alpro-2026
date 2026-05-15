file = input('Enter a file name: ')
handle = open(file)

tabel ={}

for line in handle:
    if line.startswith('From '):
        kata = line.split()
        waktu = kata[5]
        waktu = waktu.split(":")
        jam = waktu[0]
        tabel[jam] = tabel.get(jam,0) +1

urut = sorted(tabel.items())

for i in urut:
    pukul,jummlah = i
    print(f"{pukul} {jummlah}")
