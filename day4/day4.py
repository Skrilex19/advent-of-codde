file = 'input.txt'
uno = [] 
dos = []
wynik = 0
f = open(file)
for line in f:
    line = line.strip()
    first_elf, second_elf = line.split(",") 
    # print(first_elf,second_elf)
    a, b = first_elf.split("-")
    c, d = second_elf.split("-")
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    # print(a,b,c,d)
    for x in range(b - a + 1):
        uno.append(a)
        a = a + 1
    for y in range(d - c + 1):
         dos.append(c)
         c = c + 1
    if(uno[0] >= dos[0] and uno[-1] <= dos[-1] or uno[0] <= dos[0] and uno[-1] >= dos[-1]):
        wynik = wynik + 1
        # print(wynik)
        # print(uno)
        # print(dos)  
        uno.clear()
        dos.clear()
    else:
        uno.clear()
        dos.clear()

print(wynik)