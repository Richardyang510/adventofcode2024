import copy

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


def find_start(arr: list[list[str]]) -> tuple[int, int]:
    r_max = len(arr)  # going down
    c_max = len(arr[0])  # going across

    # Find starting pos
    for r in range(r_max):
        for c in range(c_max):
            if arr[r][c] == "^":
                return r, c
    
    for rr in arr:
        print(rr)
    
    raise ValueError()


#           U   R   D   L
r_delta = [-1,  0,  1,  0]
c_delta = [ 0,  1,  0, -1]


def p1(arr: list[list[str]]) -> tuple[set[tuple[int, int, int]], bool]:
    # return visited, if guard leaves

    r_max = len(arr)  # going down
    c_max = len(arr[0])  # going across

    visited: set[tuple[int, int, int]] = set()

    r_c, c_c = find_start(arr)
    d_c = 0

    while r_c >= 0 and r_c <= r_max - 1 and c_c >= 0 and c_c <= c_max - 1:

        if (r_c, c_c, d_c) in visited:
            return visited, False
        
        visited.add((r_c, c_c, d_c))
        r_n = r_c + r_delta[d_c]
        c_n = c_c + c_delta[d_c]
        if r_n >= 0 and r_n <= r_max - 1 and c_n >= 0 and c_n <= c_max - 1:
            if arr[r_n][c_n] == "#" or arr[r_n][c_n] == "!":
                d_c = (d_c+1)%4
                continue
                
        r_c = r_n
        c_c = c_n

    return visited, True


def p2(arr: list[list[str]]) -> int:
    n = 0

    r_max = len(arr)  # going down
    c_max = len(arr[0])  # going across

    for r in range(r_max):
        for c in range(c_max):
            if arr[r][c] == ".":
                arr_c = copy.deepcopy(arr)
                arr_c[r][c] = "!"
                v, exits = p1(arr_c)
                if not exits:
                    n += 1

                    # for val in v:
                    #     arr_c[val[0]][val[1]] = "X"
                    # for rr in arr_c:
                    #     print(rr)
    
    return n


inp = ""
with open(f"day06/input{INPUT}.txt") as f:
    for line in f:
        inp += line
arr = to_char_array(inp)
v, _ = p1(arr)
v_p1 = set([(v1, v2) for (v1, v2, v3) in v])
print("p1", len(v_p1))
print("p2", p2(arr))
