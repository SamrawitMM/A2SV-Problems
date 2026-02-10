cost, budget, amount = map(int, input().split())


total_cost = sum([ i*cost for i in range(1, amount+1)])

if total_cost > budget:
    print(total_cost - budget)
else:
    print(0)
