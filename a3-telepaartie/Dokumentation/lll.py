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
