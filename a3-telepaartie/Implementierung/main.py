from queue import Queue
import math

def lll(v):
    """
    Breadth-First-Search durchführen, um LLL zu finden.
    """
    done = False
    v = tuple(sorted(v))

    q = Queue()
    q.put((v, 0))

    nodes = set()

    while True:
        v, steps = q.get()
        if v in nodes:
            continue
        nodes.add(v)
        # print("debug: processing", v)
        if 0 in v:
            break
        v = tuple(sorted(v))
        q.put(((2*v[0], v[1]-v[0], v[2]), steps+1))
        q.put(((2*v[0], v[1], v[2]-v[0]), steps+1))
        q.put(((v[0], 2*v[1], v[2]-v[1]), steps+1))

    return steps

def l(n):
    solution = 0
    combs = set()
    for i in range(n+1):
        for j in range(n-i+1):
            combs.add(tuple(sorted((i,j,n-i-j))))

    for i,comb in enumerate(combs):
        solution = max(solution, lll(comb))

    return solution

print(l(100))