def swap_case(s):
    output = ''
    for char in s :
        if char.islower():
            output += char.upper()
        else:
            output += char.lower()
            
    return output

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
