INPUT = ""
# INPUT = "_example"

def to_char_array(inp: str) -> list[list[str]]:
    out = []
    for r in inp.split("\n"):
        r_char = []
        for c in r.strip():
            r_char.extend(c)
        out.append(r_char)
    return out


def bfs(arr: list[list[str]], r_start: int, c_start: int) -> tuple[int, int]:
    r_max = len(arr)  # going down
    c_max = len(arr[0])  # going across
    q: list[tuple[int, int]] = [(r_start, c_start)]
    visited: set[tuple[int, int]] = set()
    highest: set[tuple[int, int]] = set()
    paths = 0

    while len(q) > 0:
        r, c = q.pop(0)
        v = int(arr[r][c])
        visited.add((r, c))
        if arr[r][c] == "9":
            highest.add((r, c))
            paths += 1
        for r_d, c_d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r_next = r + r_d
            c_next = c + c_d
            if r_next >= 0 and r_next <= r_max - 1 and c_next >= 0 and c_next <= c_max - 1:
                v_next = arr[r_next][c_next]
                if v_next == ".":
                    continue
                if (r_next, c_next) in visited:
                    continue
                v_next = int(v_next)
                if v_next == v + 1:
                    q.append((r_next, c_next))
    
    return len(highest), paths


def get_trail_heads(arr: list[list[str]]) -> list[tuple[int, int]]:
    r_max = len(arr)  # going down
    c_max = len(arr[0])  # going across

    # find all trail heads
    trail_heads: list[tuple[int, int]] = []

    for r in range(r_max):
        for c in range(c_max):
            if arr[r][c] == "0":
                trail_heads.append((r, c))

    return trail_heads   


def p1(arr: list[list[str]]) -> tuple[int, int]:
    n1 = 0
    n2 = 0
    trail_heads = get_trail_heads(arr)
    # for each trail head, bfs and keep track of how many unique 9's are visible
    for r_t, c_t in trail_heads:
        uniq_9s, paths = bfs(arr, r_t, c_t)
        n1 += uniq_9s
        n2 += paths
    return n1, n2


inp = ""
with open(f"day10/input{INPUT}.txt") as f:
    for line in f:
        inp += line

arr = to_char_array(inp)
# for r in arr:
#     print(r)

uniq_9s, paths = p1(arr)
print("p1", uniq_9s)
print("p2", paths)
