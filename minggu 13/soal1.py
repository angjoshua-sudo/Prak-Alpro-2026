tA = eval(input('tA= '))
pembanding = tA[0]
for i in range(len(tA)):
    if pembanding == tA[i]:
        temp = True
    else:
        temp = False
        break

print()
print(temp)
