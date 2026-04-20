file1= input("masukkan nama file ke-1: ")
file2= input("masukkan nama file ke-2: ")
isi1= []
isi2= []
count = 0

try:
    handle1 = open(file1)
    handle2 = open(file2)

    for line in handle1:
        line = line.strip()
        isi1.append(line)

    for line in handle2:
        line = line.strip()
        isi2.append(line)

    len1 = len(isi1)
    len2 = len(isi2)

    if len1  > len2:
        panjang = len2
    elif len1 < len2:
        panjang = len1
    else:
        panjang = len1
    
    for i in range (panjang):
        if isi1[i] != isi2[i]:
            count += 1
            print(f'baris ke-{i+1} berbeda, file1: {isi1[i]} sedangkan file2: {isi2[i]}')

    if len1 > len2:
        for i in range (panjang, len1):
            count += 1
            print(f'baris ke-{i+1} berbeda, file1: {isi1[i]} sedangkan file2: -')

    elif len1 < len2:
        for i in range (panjang, len2):
            count += 1
            print(f'baris ke-{i+1} berbeda, file1: - sedangkan file2: {isi2[i]}')

    print(f"jumlah baris yang beda: {count}")

    handle1.close()
    handle2.close()
except:
    print("file tidak ditemukan")
    