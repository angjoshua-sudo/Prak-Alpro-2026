lista = eval(input("Masukkan key: "))
listb = eval(input("Masukkan value: "))

dictionary = {}

for i in range(len(lista)):
    dictionary[lista[i]] = listb[i]

print(dictionary)
