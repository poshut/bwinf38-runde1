#!/usr/bin/python3
import sys
import math
from queue import Queue

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
        v = tuple(sorted(v))
        if v in nodes:
            continue
        nodes.add(v)
        # print("debug: processing", v)
        if 0 in v:
            break
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

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Benutzung:", sys.argv[0], "<lll|l>", "<x,y,z|n>", file=sys.stderr)
        exit(1)
    
    if sys.argv[1] == "lll":
        if len(sys.argv) < 5:
            print("Benutzung:", sys.argv[0], "<lll|l>", "<x,y,z|n>", file=sys.stderr)
            exit(1)
        try:
            x = int(sys.argv[2])
            y = int(sys.argv[3])
            z = int(sys.argv[4])
        except Exception:
            print("Benutzung:", sys.argv[0], "<lll|l>", "<x,y,z|n>", file=sys.stderr)
            exit(1)
        
        if x < 0 or y < 0 or z < 0:
            print("x, y und z dürfen nicht negativ sein!", file=sys.stderr)
            exit(1)

        print(lll((x,y,z)))
    elif sys.argv[1] == "l":
        try:
            n = int(sys.argv[2])
        except ValueError:
            print("Benutzung:", sys.argv[0], "<lll|l>", "<x,y,z|n>", file=sys.stderr)
            exit(1)

        if n < 0:
            print("n darf nicht negativ sein!", file=sys.stderr)
            exit(1)

        print(l(n))
    else:
        print("Benutzung:", sys.argv[0], "<lll|l>", "<x,y,z|n>", file=sys.stderr)
        exit(1)
