n= 5
edges=[[0,1],[1,2],[2,3],[1,4]]
start = 0
end = 3


from collections import deque, defaultdict 

def shortest_route(n,edges,start,end):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    q= deque([(start,0)])
    visited =set([start])

    while q:
        node, dist = q.popleft()

        if node ==end:
            return dist
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append((nei,dist+1))
    return -1

print (shortest_route(n,edges,start,end))