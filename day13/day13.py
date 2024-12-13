# each button is pressed at most 100 times
TIMES_MAX = 1000

INPUT = ""
# INPUT = "_example"


def read_input(inp: str) -> list[tuple[int, int, int, int, int, int]]:
    cases: list[tuple[int, int, int, int, int, int]] = []
    a_x, a_y, b_x, b_y, p_x, p_y = 0, 0, 0, 0, 0, 0
    for s in inp.split("\n"):
        if s.startswith("Button A"):
            a_x = int(s.split()[2].split("+")[1].removesuffix(','))
            a_y = int(s.split()[3].split("+")[1])
        elif s.startswith("Button B"):
            b_x = int(s.split()[2].split("+")[1].removesuffix(','))
            b_y = int(s.split()[3].split("+")[1])
        elif s.startswith("Prize"):
            p_x = int(s.split()[1].split("=")[1].removesuffix(','))
            p_y = int(s.split()[2].split("=")[1])
            cases.append((a_x, a_y, b_x, b_y, p_x, p_y))
    return cases


def p1_slow(inp: str) -> int:
    n = 0
    cases = read_input(inp)
    for a_x, a_y, b_x, b_y, p_x, p_y in cases:
        print(a_x, a_y, b_x, b_y, p_x, p_y)
        # tabulation approach
        # see minimum coin change

        # dp[x][y] = the minimum number of tokens to reach X=x and Y=y
        # inputs seemed to be capped around 20k, 20k*20k is 200M which is doable in memory
        # nvm it is not
        dp: list[list[int]] = [[TIMES_MAX for _ in range(p_y + 1)] for _ in range(p_x + 1)]
        # takes 0 tokens to get to x=0, y=0
        dp[0][0] = 0
        for x in range(1, p_x + 1):
            for y in range(1, p_y + 1):
                if dp[0][67] == 1:
                    return 1
                # Try A
                if x - a_x >= 0 and y - a_y >= 0:
                    dp[x][y] = min(dp[x][y], dp[x-a_x][y-a_y] + 3)
                # Try B
                if x - b_x >= 0 and y - b_y >= 0:
                    dp[x][y] = min(dp[x][y], dp[x-b_x][y-b_y] + 1)
                
        
        print(dp[p_x][p_y])
        break

    return 0


def coin_change(s, a, b) -> set[tuple[int, int]]:
    # dp[i] = list of num_A, num_B to reach X=i or Y=i
    dp = [set() for _ in range(s + 1)]
    dp[0].add((0, 0))

    for i in range(1, s + 1):
        if i - a >= 0:
            for num_a, num_b in dp[i-a]:
                if num_a != TIMES_MAX and num_b != TIMES_MAX:
                    dp[i].add((num_a + 1, num_b))
        if i - b >= 0:
            for num_a, num_b in dp[i-b]:
                if num_a != TIMES_MAX and num_b != TIMES_MAX:
                    dp[i].add((num_a, num_b + 1))
    
    return dp[s]


def p1(inp: str) -> int:
    # different approach
    # treat X and Y as separate problems
    # use traditional coin change approach on X and Y independently, then see if any of the answers match
    n = 0
    cases = read_input(inp)
    for a_x, a_y, b_x, b_y, p_x, p_y in cases:
        # print(a_x, a_y, b_x, b_y, p_x, p_y)
        x_sol = coin_change(p_x, a_x, b_x)
        y_sol = coin_change(p_y, a_y, b_y)
        sol = x_sol.intersection(y_sol)
        best = TIMES_MAX
        for s_a, s_b in sol:
            best = min(best, 3*s_a + s_b)
        if best != TIMES_MAX:
            n += best

    return n


def p2(inp: str) -> int:
    # using math...
    n = 0
    cases = read_input(inp)
    for a_x, a_y, b_x, b_y, p_x, p_y in cases:
        p_x += 10000000000000
        p_y += 10000000000000
        n_b = float(p_y * a_x - p_x * a_y) / float(b_y * a_x - a_y * b_x)
        n_a = float(p_x - n_b * b_x) / float(a_x)
        if n_a.is_integer() and n_b.is_integer():
            n += int(3*n_a + n_b)
    
    return n


inp = ""
with open(f"day13/input{INPUT}.txt") as f:
    for line in f:
        inp += line
print("p1", p1(inp))
print("p2", p2(inp))