input_example = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def to_char_array(inp: str) -> list[list[str]]:
    out = []
    for r in inp.split("\n"):
        r_char = []
        for c in r.strip():
            r_char.extend(c)
        out.append(r_char)
    return out


#           U   D   L   R  UL  UR  DL  DR
r_delta = [-1,  1,  0,  0, -1, -1,  1, 1]
c_delta = [ 0,  0, -1,  1, -1,  1, -1, 1]
XMAS = "XMAS"


def p1(inp: str) -> int:
    n = 0

    arr = to_char_array(inp)

    # for r in arr:
    #     print(r)

    r_max = len(arr)  # going down
    c_max = len(arr[0])  # going across

    # print(r_max, c_max)

    for r in range(r_max):
        for c in range(c_max):
            # optimization, make sure we start on X
            if arr[r][c] != "X":
                continue
            # for each element, check each dir
            for d in range(len(r_delta)):
                # make sure we are still in range
                r_new = r + 3*r_delta[d]
                c_new = c + 3*c_delta[d]
                if r_new < 0 or c_new < 0 or r_new > r_max - 1 or c_new > c_max - 1:
                    continue
                # we are in range, check that the letters match
                matches = 1
                for i, l in enumerate(XMAS):
                    if arr[r+i*r_delta[d]][c+i*c_delta[d]] != l:
                        matches = 0
                        break
                n += matches
        
    return n


def p2(inp: str) -> int:
    n = 0

    arr = to_char_array(inp)

    r_max = len(arr)  # going down
    c_max = len(arr[0])  # going across

    for r in range(r_max):
        for c in range(c_max):
            # optimization, make sure we start on A
            if arr[r][c] != "A":
                continue
            # check that there is space to the left, right, up, and down
            if r == 0 or r == r_max - 1 or c == 0 or c == c_max - 1:
                continue
            tl = arr[r-1][c-1]
            tr = arr[r-1][c+1]
            bl = arr[r+1][c-1]
            br = arr[r+1][c+1]

            if ((tl == "M" and br == "S") or (tl == "S" and br == "M")) and \
               ((tr == "M" and bl == "S") or (tr == "S" and bl == "M")):
                n += 1
        
    return n


inp = ""
with open(f"day04/input.txt") as f:
    for line in f:
        inp += line


print("p1 example", p1(input_example))
print("p1", p1(inp))
print("p2 example", p2(input_example))
print("p1", p2(inp))