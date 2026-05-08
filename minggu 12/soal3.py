file = input("Masukkan nama file: ")
try:
    handle = open(file)
except:
    print("File tidak ditemukan")
    exit()

mail = {}

for line in handle:
    if line.startswith("From "):
        kata = line.split()
        email = kata[1]
        mail[email] = mail.get(email, 0) + 1
    
print(mail)
