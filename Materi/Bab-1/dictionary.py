banner = {}

banner['title'] = 'Dictionary'
banner['description'] = 'A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.'
banner['syntax'] = 'x = {key1 : value1, key2 : value2}'


for key, value in banner.items():
    print(f'{key}: {value}')
print('\n')
# How can you check if a key 'age' exists in a dictionary 'person'?

person = {
    'name': 'John',
    'age': 23,
}

print(key('age').exists(person))

