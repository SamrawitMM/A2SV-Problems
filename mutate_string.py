def mutate_string(string, position, character):
    string_list = list(string)
    
    output = "".join(string_list[:position] + list(character) + string_list[position+1:len(string_list)])

    return output
  
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
