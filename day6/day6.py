file = 'input.txt'
f = open(file)
arr = []
index = 0
y = 0
z = 4
wynik = 0
for line in f:
    for q in line:
        for x in range(y,z):
            arr.append(line[x])
        print(arr)
        arr = list(dict.fromkeys(arr))
        print(arr)
        if len(arr) < 4:
            arr.clear()
            y = y + 1
            z = z + 1 
        else:
            wynik = wynik + index + 4
            arr.clear()
            break
        if len(line) + 1 == z:
            break
        index = index + 1
print(arr)
print(wynik)