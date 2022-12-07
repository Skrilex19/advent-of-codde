d = {}
file = 'input.txt'
f = open(file)
current_file = []
index = 0
for line in f:
    line = line.strip()
    command = line.split(" ")
    id = command[0]    
    if id == '$':                       #komendy
        if command[1] == 'cd':                   #zmiana ścieżki
            # current_file i value
            if command[2] == '..':
                current_file.pop()
            elif command[2] == '/':
                current_file.append(command[2] + str(index))
                d[current_file[-1]] = 0
            else:
                current_file.append(command[2] + str(index))
                d[current_file[-1]] = 0
    elif command[0] == "dir":
        continue
    else:
        for x in current_file:
            d[x] = int(command[0]) + d[x]
    index += 1
suma = 0
print(d)
for key in d:
    if d[key] <= 100000:
        suma += d[key]
print(suma)

