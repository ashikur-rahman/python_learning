n= 5
edges=[[0,1],[1,2],[2,3],[1,4]]
start = 0
end = 3


from collections import deque, defaultdict 


def shortest_route(n, edges, start, end):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    print("GRAPH:", dict(graph))

    q= deque([(start,0)])
    visited = set([start])
    print("INIT: q =", q, "visited =", visited)

    while q:
        node, dist = q.popleft()
        print("\nPOP:", node, "dist =", dist, "q =", q)

        if node == end:
            print("REACHED END:", end, "with distance", dist)
            return dist

        for nei in graph[node]:
            print("  CHECK neighbor:", nei)
            if nei not in visited:
                visited.add(nei)
                q.append((nei, dist+1))
                print("   -> ADD nei:", nei, "new q =", q, "visited =", visited)

    return -1

print (shortest_route(n,edges,start,end))