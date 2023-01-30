import random

# Dictionaries— dict = {'key1':'value1', 'key2':'value2', 'key3':'value3', ...}
# school_data.json is a list of dictionaries (values of list entries can be any python object)
# methods are functions applied to objects (appended with a ".")
emptyDict = {}
phonebook = {'Chris': '555−1111',
             'Katie': '555−2222',
             'Joanne': '555−3333'}

myDict = dict(m=8, n=9)
print(f"Number of key-calue paires: {len(phonebook)}")


# Key error: no match for the key you chose (case sensitive)
# Dictionary keys have to be unique (no repeating key values)
# Dictionaries are mutable (you can edit the values)
name = 'chris'
if name in phonebook:
    print(phonebook[name])
else:
    print('name not found')

try:
    print(phonebook[name])
except KeyError:
    print('name not found')

print(phonebook['Chris'])

print(phonebook)
phonebook['Chris'] = '555-4444'
phonebook['Joe'] = '555-0123'
print(phonebook)

print(phonebook['Chris'])
del phonebook['Chris']

for key in phonebook:
    print(key, ': ', phonebook[key])

for value in phonebook.values():
    print(value)

for k, v in phonebook.items():
    print(f'the key is {k} and the value is {v}')

for ph_tuple in phonebook.items():
    print(ph_tuples)

name = 'Katie'
phonebook.get(name, 'key not found')

print(phonebook)
phonebook.clear()
print(phonebook)

remove = phonebook.pop('Katie', 'not found')
print(remove)

a = phonebook.popitem()
print(a)
print(phonebook)

print(phonebook[random.choice(list(phonebook))])
