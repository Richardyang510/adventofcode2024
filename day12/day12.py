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


def calc_regions(arr: list[list[str]]) -> list[list[int]]:
    r_max = len(arr)  # going down
    c_max = len(arr[0])  # going across
    # Second pass
    # find region area
    # keep visited array
    # for each cell, BFS to find all coords in the current region
    # create array regions[r][c] = area of region
    region = [ [-1]*c_max for _ in range(r_max)]
    visited: set[tuple[int, int]] = set()
    
    for r in range(r_max):
        for c in range(c_max):
            if (r, c) in visited:
                continue
            q = [(r, c)]
            curr_region_coords: set[tuple[int, int]] = set()
            while len(q) > 0:
                r_c, c_c = q.pop(0)
                if (r_c, c_c) in visited:
                    continue
                visited.add((r_c, c_c))

                curr_region_coords.add((r_c, c_c))
                curr_region = arr[r_c][c_c]
                for r_d, c_d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    r_next = r_c + r_d
                    c_next = c_c + c_d
                    if r_next >= 0 and r_next <= r_max - 1 and c_next >= 0 and c_next <= c_max - 1:
                        if (r_next, c_next) in visited:
                            continue
                        next_region = arr[r_next][c_next]
                        if next_region == curr_region:
                            q.append((r_next, c_next))

            for region_r, region_c in curr_region_coords:
                region[region_r][region_c] = len(curr_region_coords)
    return region


def calc_price(region: list[list[int]], fence: list[list[int]]) -> int:
    r_max = len(arr)  # going down
    c_max = len(arr[0])  # going across
    # final output is the element-wise product of fence and region
    n = 0
    for r in range(r_max):
        for c in range(c_max):
            n += region[r][c] * fence[r][c]
    return n


def p1(arr: list[list[str]]) -> int:
    r_max = len(arr)  # going down
    c_max = len(arr[0])  # going across

    # Two passes
    # finding fence length:
    #   for each cell, check 4 neighbors
    #   each cell needs 4-N fences, where N is the number of neighbors with same value
    # create array fence[r][c] = number of fences at this region
    fence = [ [-1]*c_max for _ in range(r_max)]

    for r in range(r_max):
        for c in range(c_max):
            curr_region = arr[r][c]
            num_neighbors = 0
            for r_d, c_d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r_next = r + r_d
                c_next = c + c_d
                if r_next >= 0 and r_next <= r_max - 1 and c_next >= 0 and c_next <= c_max - 1:
                    next_region = arr[r_next][c_next]
                    if next_region == curr_region:
                        num_neighbors += 1
            fence[r][c] = (4 - num_neighbors)
    
    region = calc_regions(arr)
    return calc_price(region, fence)


def num_corners(sub_arr: list[list[str]]) -> int:
    # sub_arr is a 3x3 array
    # sub_arr[1][1] is the element of interest
    curr = sub_arr[1][1]
    corners = 0
    if (sub_arr[0][1] == curr) == (sub_arr[1][2] == curr):
        if sub_arr[0][1] != curr: # outside corner
            corners += 1
        elif sub_arr[0][2] != curr: # inside corner
            corners += 1
    if (sub_arr[1][2] == curr) == (sub_arr[2][1] == curr):
        if sub_arr[1][2] != curr:
            corners += 1
        elif sub_arr[2][2] != curr:
            corners += 1
    if (sub_arr[2][1] == curr) == (sub_arr[1][0] == curr):
        if sub_arr[2][1] != curr:
            corners += 1
        elif sub_arr[2][0] != curr:
            corners += 1
    if (sub_arr[1][0] == curr) == (sub_arr[0][1] == curr):
        if sub_arr[1][0] != curr:
            corners += 1
        elif sub_arr[0][0] != curr:
            corners += 1
    return corners


def p2(arr: list[list[str]]) -> int:
    r_max = len(arr)  # going down
    c_max = len(arr[0])  # going across

    # different algo for calculating fence, same for region and price
    fence = [ [-1]*c_max for _ in range(r_max)]

    # Here we want to compute the number of corners
    # The number of sides for a region is equal to the number of corners
    # For each element, find its 3x3 array surrounding that element and check number of corners
    for r in range(r_max):
        for c in range(c_max):
            sub_arr = [ ["."]*3 for _ in range(3)]
            for r_d in range(-1, 2):
                for c_d in range(-1, 2):
                    r_next = r + r_d
                    c_next = c + c_d
                    if r_next >= 0 and r_next <= r_max - 1 and c_next >= 0 and c_next <= c_max - 1:
                        sub_arr[r_d + 1][c_d + 1] = arr[r_next][c_next]
                    else:
                        sub_arr[r_d + 1][c_d + 1] = "."
            fence[r][c] = num_corners(sub_arr)

    region = calc_regions(arr)
    return calc_price(region, fence)


inp = ""
with open(f"day12/input{INPUT}.txt") as f:
    for line in f:
        inp += line

arr = to_char_array(inp)
# for r in arr:
#     print(r)

print("p1", p1(arr))
print("p2", p2(arr))

