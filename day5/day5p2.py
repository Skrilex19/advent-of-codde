file = 'input.txt'
f = open(file)
stack = ['RPCDBG','HVG','NSQDJPM','PSLGDCNM','JBNCPFLS','QBDZVGTS','BZMHFTQ','CMDBF','FCQG']
for line in f:
    print(stack)
    line = line.strip()
    line = line.split(" ")
    first_number = int(line[1])
    second_number = int(line[3])
    third_number = int(line[-1])
    print(first_number,second_number,third_number)
    print(stack)
    removed_element = stack.pop(second_number - 1) # wycinam caly index
    sliced_element = ''
    for x in range(-first_number,0):
        sliced_element = sliced_element + removed_element[x] # przygotowuje stringa do insertowania
    first_correct_element = removed_element[:-first_number] #wycinam je
    stack.insert(second_number - 1, first_correct_element)   
    sec_removed_element = stack.pop(third_number - 1)
    stack.insert(third_number - 1, sec_removed_element + sliced_element)   
    print(stack)
print(stack)