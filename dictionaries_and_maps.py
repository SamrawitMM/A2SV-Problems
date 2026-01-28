
phonebook = {}
phonebook_length = int(input())
for _ in range(phonebook_length):
    name, phone_number = input().split()
    phonebook[name] = phone_number
    
    
while True:
    try:
        query = input()
        if query in phonebook:
            print(query+"="+phonebook[query])
        else:
            print('Not found')
    except EOFError:
        break
