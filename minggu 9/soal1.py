kata_1 = input("Masukkan kata 1: ")
kata_2 = input("Masukkan kata 2: ")

kata_1 = ''.join([i for i in kata_1 if i.isalpha()])
kata_1 = kata_1.lower()
kata_2 = ''.join([i for i in kata_2 if i.isalpha()])
kata_2 = kata_2.lower()

if sorted(kata_1) == sorted(kata_2):
    print("kata 1 dan kata 2 adalah anagram.")
else:
    print("kata 1 dan kata 2 bukan anagram.")
