d = {}
file = 'input.txt'
f = open(file)
current_file = []
index = 0
for line in f:
    line = line.strip()
    command = line.split(" ")
    id = command[0]    
    if id == '$':                       
        if command[1] == 'cd':                   
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
arr = []
required_space = 30000000
nie_to_clear = 70000000 - d['/0']
to_clear = required_space - nie_to_clear

for key in d:
    if d[key] > to_clear:
        arr.append(d[key])
        suma = 0
arr.sort()
print(arr[0])

 


