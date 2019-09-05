def l(n):
    solution = 0
    combs = set()
    for i in range(n+1):
        for j in range(n-i+1):
            combs.add(tuple(sorted((i,j,n-i-j))))

    for i,comb in enumerate(combs):
        solution = max(solution, lll(comb))

    return solution
