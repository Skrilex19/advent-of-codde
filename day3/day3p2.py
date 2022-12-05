import string
alphabet = list(string.ascii_letters)
file = 'input.txt'
f = open(file)
new = 1
old_line = []
new_line = []
suma = 0
for line in f:
    line = line.strip()
    line = set(line)
    line = sorted(line)
    if new == 1:
        old_line.clear()
        for x in line:
            old_line.append(x)
        new = new + 1
    elif new == 2:
        new_line.clear()
        for x in line:
            new_line.append(x)
        new = new + 1
    elif new == 3:  
        new = 1
        print("spot4:",new)
        print(*old_line, sep = "")
        print(*new_line, sep = "")
        print(*line, sep = "")
        for x in old_line:
            for y in new_line:
                if x == y:
                    for q in line:
                        if q == y:
                            a = 1
                            for z in alphabet:
                                if z == q:
                                    print(x,y,q,z)
                                    suma = suma + a
                                    print(a,suma)
                                a = a + 1
print(suma)
# pomsyl 1 wjebac to do tablicy a potem posortowac i usunąć powtarzające sie elementy
# DZIALA!!!11