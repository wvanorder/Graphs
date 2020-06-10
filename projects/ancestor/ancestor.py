
import sys
sys.path.append('..')

from graph.util import Stack


def get_parents(graph, starting_node):
    if starting_node in graph:
        return graph[starting_node]
    else:
        return []


def earliest_ancestor(ancestors, starting_node):
    graph = {}
    stack = Stack()

    stack.push([starting_node])

    longest_path = 1
    ancestor = None
    
    for parent, child in ancestors:
        graph[child] = graph.get(child, [])
        graph[child].append(parent)

    while stack.size() > 0:
        path = stack.pop()
        v = path[-1]
        if len(path) > longest_path:
            longest_path = len(path)
            ancestor = v
        if len(path) == longest_path and ancestor:
            ancestor = v if v < ancestor else ancestor
        for parent in get_parents(graph, v):
            path_copy = path.copy()
            path_copy.append(parent)
            stack.push(path_copy)
    
    return ancestor if ancestor else -1