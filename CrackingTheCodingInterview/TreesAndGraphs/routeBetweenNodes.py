from Graph import Graph

def routeBetweenNodes(graph, source, destination):
    queue = list()
    
    if source in graph.elements:
        queue.append(source)
    else:
        return False

    if source == destination:
        return True

    visited = set()
    visited.add(source)

    while queue:
        node = queue.pop(0)
        if destination in graph.elements[node]:
            return True 
        for next_node in graph.elements[node]:
            if next_node not in visited:
                queue.append(next_node)
                visited.add(next_node)

    return False


g = Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
g.addEdge(2, 4)

print(routeBetweenNodes(g, 3, 2))

