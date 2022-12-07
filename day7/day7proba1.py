dict = {
    '/': {
        
    }
}
file = 'input.txt'
f = open(file)
command = []
current_dir = []
new_element = True

for line in f:
    line = line.strip()
    print(line)
    command = line.split(" ")
    id = command[0]    
    if id == '$':                       #komendy
        if command[1] == 'cd':                   #zmiana ścieżki
            if command[2] == '..':
                current_dir.append(current_dir[-2])
                index = len(current_dir)
            else:
                current_dir.append(command[2])
                index = len(current_dir)
            
            
        if command[1] == 'ls':                   #print wszystkie aktualne pliki i ścieżki - nie musze chyba obsługiwać
            if current_dir[-1] != '/':
                for x in dict[current_dir[index - 2]][current_dir[-1]]:
                    print(x)
            else:
                for x in dict[current_dir[0]]:
                    print(x)
    elif id == 'dir':
        if current_dir[-1] != '/':
            # print(current_dir[-1],dict) 
            dict[current_dir[index - 2]][current_dir[-1]][command[1]] = {}
        else:
            dict[current_dir[0]][command[-1]] = {}
            new_element = True
    else:
        print(dict,type(current_dir[-1]),current_dir[-1])
        if new_element == True:
            if current_dir[-1] != '/':
                print(current_dir)
                dict[current_dir[index - 2]][current_dir[-1]]['size'] = int(command[0])
                new_element = False
            else:
                print(current_dir)
                dict[current_dir[-1]]['size'] = int(command[0])
                new_element = False
        else:
            if current_dir[-1] != '/':
                print(current_dir, current_dir[index - 2])
                dict[current_dir[index - 2]][current_dir[-1]]['size'] = int(dict[current_dir[index - 2]][current_dir[-1]].pop('size')) + int(command[0])
            else:
                dict[current_dir[-1]]['size'] = int(dict[current_dir[-1]].pop('size')) + int(command[0])
        
        
    
print(dict)