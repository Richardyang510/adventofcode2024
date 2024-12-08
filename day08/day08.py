from collections import defaultdict
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

def p1(arr: list[list[str]], uniq_l: str, is_p2 = False) -> int:
    r_max = len(arr)  # going down
    c_max = len(arr[0])  # going across

    pos: dict[str, list[tuple[int, int]]] = defaultdict(list)

    # arr_out = copy.deepcopy(arr)

    antinodes: set[tuple[int, int]] = set()

    # index all positions of antenna
    for r in range(r_max):
        for c in range(c_max):
            if arr[r][c] != ".":
                pos[arr[r][c]].append((r, c))

    for l in uniq_l:
        if l == ".":
            continue
        # print(l, pos[l])
        # iterate over all possible pair combos
        for l_idx1 in range(len(pos[l])):
            for l_idx2 in range(len(pos[l])):
                if l_idx1 == l_idx2:
                    continue
                # compute rise and run of the two antenna
                rise = pos[l][l_idx1][0] - pos[l][l_idx2][0]
                run = pos[l][l_idx1][1] - pos[l][l_idx2][1]
                # add the rise and run to the first idx
                new_r = pos[l][l_idx1][0] + rise
                new_c = pos[l][l_idx1][1] + run
                # p2: add the location of the antenna as well
                if is_p2:
                    antinodes.add(pos[l][l_idx1])
                    antinodes.add(pos[l][l_idx2])

                # check the location is within bounds
                while new_r >= 0 and new_r < r_max and new_c >= 0 and new_c < c_max:
                    # arr_out[new_r][new_c] = "#"
                    antinodes.add((new_r, new_c))

                    if not is_p2:
                        break
                
                    # p2: keep adding values until we go OOB
                    new_r += rise
                    new_c += run

    # for r in arr_out:
    #     print("".join(r))

    return len(antinodes)


inp = ""
with open(f"day08/input{INPUT}.txt") as f:
    for line in f:
        inp += line

uniq_letters = ''.join(set(inp.replace("\n", ""))).strip()
# print(uniq_letters)

arr = to_char_array(inp)
# for r in arr:
#     print(r)

print("p1", p1(arr, uniq_letters))
print("p2", p1(arr, uniq_letters, True))
