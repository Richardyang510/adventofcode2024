from collections import defaultdict

nodes = defaultdict(list)

INPUT = ""
# INPUT = "_example"

with open(f"day05/input{INPUT}.txt") as f:
    for line in f:
        v = line.strip().split("|")
        # l must occur before r
        # represent using a DAG
        l = v[0]
        r = v[1]
        nodes[l].append(r)

# print(nodes)


def check(l: list[str]) -> bool:
    if len(l) == 1:
        return True
    curr_n = l[0]
    next_n = l[1]
    if curr_n not in nodes: 
        return False
    if next_n not in nodes[curr_n]:
        return False
    return check(l[1:])


wrong_inputs = []

with open(f"day05/check{INPUT}.txt") as f:
    s = 0
    for line in f:
        n = line.strip().split(",")
        if(check(n)):
            s += int(n[int(len(n)/2)])
        # used for p2
        else:
            wrong_inputs.append(n)

print("p1:", s)

# p2, reduce nodes to be the graph representing the nodes in the input specifically
# then use topological sort to put them in order


def top_dfs(v: str, g: dict[str, list[str]], visited: dict[str, bool], stack: list[str]):
    visited[v] = True
    for n in g[v]:
        if not visited[n]:
            top_dfs(n, g, visited, stack)
    stack.insert(0, v)


def top(g: dict[str, list[str]]) -> list[str]:
    visited = defaultdict(bool)
    stack = []

    for v in g:
        if not visited[v]:
            top_dfs(v, g, visited, stack)
    
    return stack


s = 0
for i in wrong_inputs:
    # filter the keys and values in nodes
    # nodes_i is a subgraph containing only the input nodes
    nodes_i = {k: [v2 for v2 in v if v2 in i] for k, v in nodes.items() if k in i}

    # sometimes a node only exists on the RHS, add those
    for v in i:
        if v not in nodes_i:
            nodes_i[v] = []

    # now perform topological sort
    stack = top(nodes_i)

    # accumulate ans
    s += int(stack[int(len(stack)/2)])

print("p2:", s)
