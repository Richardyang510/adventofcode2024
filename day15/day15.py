INPUT = ""
INPUT = "_example"

move_to_delta = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}

def to_char_array(inp: str) -> list[list[str]]:
    out = []
    for r in inp.strip().split("\n"):
        r_char = []
        for c in r.strip():
            r_char.extend(c)
        out.append(r_char)
    return out


def print_grid(grid: list[list[str]]):
    for r in grid:
        print("".join(r))
    print()


def find_robot(grid: list[list[str]]) -> tuple[int, int]:
    for r, s_r in enumerate(grid):
        for c, s_c in enumerate(s_r):
            if s_c == "@":
                return r,c
    return 0, 0


def push_block(grid: list[list[str]], r: int, c: int, move: str):
    # recursively push
    # for example we have > with
    # ..@OO.#
    # first look at @O, then look one right (recursion)
    # look at OO, then look one right (recursion)
    # look at O., base case
    # swap on the way back

    # In the case of
    # ....@O#
    # look at @O, then look one right
    # look at O#, base case

    r_d, c_d = move_to_delta[move]
    r_n = r + r_d
    c_n = c + c_d

    # Base case: can move
    if grid[r_n][c_n] == ".":
        grid[r_n][c_n] = grid[r][c]
        grid[r][c] = "."
        return
    # Base case 2: cannot move
    elif grid[r_n][c_n] == "#":
        return
    
    # Recursive case, push the next pair
    push_block(grid, r_n, c_n, move)

    # Push on the return
    if grid[r_n][c_n] == ".":
        grid[r_n][c_n] = grid[r][c]
        grid[r][c] = "."


def push_block2(grid: list[list[str]], r: int, c: int, move: str):
    # Similar logic to p1, but we need to look 2 spaces ahead
    # For up and down, need to look at left and right space

    r_d, c_d = move_to_delta[move]
    r_n = r + r_d
    c_n = c + c_d

    if move == "<" or move == ">" or grid[r][c] == "@":
        # same logic as before

        # Base case: can move
        if grid[r_n][c_n] == ".":
            grid[r_n][c_n] = grid[r][c]
            grid[r][c] = "."
            return
        # Base case 2: cannot move
        elif grid[r_n][c_n] == "#":
            return
        
        # Recursive case, push the next pair
        push_block2(grid, r_n, c_n, move)

        # Push on the return
        if grid[r_n][c_n] == ".":
            grid[r_n][c_n] = grid[r][c]
            grid[r][c] = "."
    
    else:
        # this is a box trying to move up or down
        # now we need to consider two cells

        c_box_side_d = 1 if grid[r][c] == "[" else -1
        
        r_n_left = r_n
        c_n_left = c_n
        r_n_right = r_n
        c_n_right = c_n + c_box_side_d

        # Base case: can move if both are empty
        if grid[r_n_left][c_n_left] == "." and grid[r_n_right][c_n_right] == ".":
            grid[r_n_left][c_n_left] = "["
            grid[r_n_right][c_n_right] = "]"
            grid[r][c] = "."
            grid[r][c+c_box_side_d] = "."
            return
        
        # Base case 2: cannot move if either is wall
        if grid[r_n_left][c_n_left] == "#" or grid[r_n_right][c_n_right] == "#":
            return
    
        # Recursive case, push the next pair (both left and right)
        push_block2(grid, r_n_left, c_n_left, move)

        # Push on the return
        if grid[r_n_left][c_n_left] == "." and grid[r_n_right][c_n_right] == ".":
            grid[r_n_left][c_n_left] = "["
            grid[r_n_right][c_n_right] = "]"
            grid[r][c] = "."
            grid[r][c+c_box_side_d] = "."


def score(grid: list[list[str]]) -> int:
    n = 0
    for r, r_s in enumerate(grid):
        for c, c_s in enumerate(r_s):
            if c_s == "O" or c_s == "[":
                n += r * 100 + c
    return n


def p1(grid: list[list[str]], moves: str, interactive: bool = False) -> int:
    if interactive:
        print_grid(grid)
    
    for i, m in enumerate(moves):
        r, c = find_robot(grid)
        push_block(grid, r, c, m)

        if interactive:
            input()
            print(i, m)
            print_grid(grid)
    
    print_grid(grid)

    return score(grid)


def p2(grid: list[list[str]], moves: str, interactive: bool = False) -> int:
    if interactive:
        print_grid(grid)
    
    for i, m in enumerate(moves):
        r, c = find_robot(grid)
        push_block2(grid, r, c, m)

        if interactive:
            input()
            print(i, m)
            print_grid(grid)
    
    print_grid(grid)

    return score(grid)


grid_inp = ""
moves = ""
is_grid_inp = True
with open(f"day15/input{INPUT}.txt") as f:
    for line in f:
        if len(line.strip()) == 0:
            is_grid_inp = False
            continue
        
        if is_grid_inp:
            grid_inp += line
        
        else:
            moves += line.strip()

grid = to_char_array(grid_inp)

# print("p1", p1(grid, moves))
print("p2", p2(grid, moves, True))