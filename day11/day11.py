from collections import defaultdict

INPUT = ""
# INPUT = "_example"

def blink(stones: list[int]) -> list[int]:
    i = 0
    while i < len(stones):
        if stones[i] == 0:
            stones[i] = 1
        elif len(str(stones[i])) % 2 == 0:
            s_str = str(stones[i])
            l_str, r_str = s_str[:len(s_str)//2], s_str[len(s_str)//2:]
            stones[i] = int(l_str)
            stones.insert(i + 1, int(r_str))
            i += 1
        else:
            stones[i] *= 2024
        i += 1
    return stones


def p1(inp: str, times: int) -> int:
    stones = list(map(int, inp.strip().split()))
    for i in range(times):
        stones = blink(stones)
    return len(stones)


# memoization: 2D visited array: v[stone_val][num_blinks] = total_num_blinks
v: dict[int, dict[int, int]] = defaultdict(lambda: defaultdict(int))

# traverse using recursion
# return the number of stones after traversal
def blink_dfs(stone_val: int, num_blinks: int) -> int:
    # cache case
    if stone_val in v and num_blinks in v[stone_val]:
        return v[stone_val][num_blinks]

    # base case
    if num_blinks == 0:
        return 1
    
    # recursive case
    n = 0
    if stone_val == 0:
        n += blink_dfs(1, num_blinks-1)
    elif len(str(stone_val)) % 2 == 0:
        s_str = str(stone_val)
        l_str, r_str = s_str[:len(s_str)//2], s_str[len(s_str)//2:]
        n += blink_dfs(int(l_str), num_blinks-1) + blink_dfs(int(r_str), num_blinks-1)
    else:
        n += blink_dfs(stone_val*2024, num_blinks-1)
    
    v[stone_val][num_blinks] = n
    return n


def p2(inp: str, times: int) -> int:
    stones = list(map(int, inp.strip().split()))

    n = 0
    for s in stones:
        n += blink_dfs(s, times)

    return n

inp = ""
with open(f"day11/input{INPUT}.txt") as f:
    for line in f:
        inp += line
print("p1", p1(inp, 25))
print("p2", p2(inp, 75))
