dict = {}
dict['abc'] = {}
dict['b'] = {}
dict['c'] = {}
dict['b']['a'] = {}
dict['abc']['name'] = 'Bob'
dict['abc']['age'] = 21
dict['b']['name'] = 'jan'
dict['b']['age'] = 28
print(dict)
x = dict['abc'].pop('age')
suma = int(x) + 100
dict['abc']['age'] = suma
print(dict)
   
