import string
alphabet = list(string.ascii_letters)
file = 'input.txt'
f = open(file)

# for i in alphabet:
  
#     a = a + 1
suma = 0
for line in f:
    line = line.strip()
    first = line[:len(line)//2]
    second = line[len(line)//2:]
    first = set(first)
    first = sorted(first)
    second = set(second)
    second = sorted(second)
    
    for x in first:
        for y in second:
            # print('x = ',x)
            # print('y = ',y)
            if x == y:
                a = 1
                print(x,y)
                for z in alphabet:
                    # print(suma)
                    if z == y:
                        suma = suma + a
                    a = a + 1
print(suma)
# pomsyl 1 wjebac to do tablicy a potem posortowac i usunąć powtarzające sie elementy
# DZIALA!!!11