if __name__ == '__main__':
    N = int(input())
    inputs = []
    result = []
  
    for _ in range(N):
        inputs = list(input().split())
      
        if inputs[0] == 'insert':
            index = int(inputs[1])
            value = int(inputs[2])
            result.insert(index, value)
          
        if inputs[0] == 'print':
            print(result)
          
        if inputs[0] == 'remove':
            value = int(inputs[1])
            result.remove(value)
          
        if inputs[0] == 'append':
            value = int(inputs[1])
            result.append(value)
          
        if inputs[0] == 'pop':
            result.pop()
          
        if inputs[0] == 'sort':
            result.sort()
          
        if inputs[0] == 'reverse':
            result.reverse()
