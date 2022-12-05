file = 'input.txt'
f = open(file)
stack = ['RPCDBG','HVG','NSQDJPM','PSLGDCNM','JBNCPFLS','QBDZVGTS','BZMHFTQ','CMDBF','FCQG']
for line in f:  
    line = line.strip()
    line = line.split(" ")
    first_number = int(line[1])
    second_number = int(line[3])
    third_number = int(line[-1])
    for x in range(first_number):
        removed_element = stack.pop(second_number - 1)
        sliced_element = removed_element[-1]
        first_correct_element = removed_element[:-1]
        stack.insert(second_number - 1,first_correct_element)
        sec_removed_element = stack.pop(third_number - 1)
        stack.insert(third_number - 1,sec_removed_element+sliced_element)
print(stack)