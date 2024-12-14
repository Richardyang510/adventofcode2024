INPUT = ""
# INPUT = "_example"

# x, y, dx, dy
type Robot = tuple[int, int, int, int]

times = 100000

if INPUT == "":
    width = 101
    height = 103
else:
    width = 11
    height = 7


def p1(inp: list[Robot]) -> int:
    final_pos: list[tuple[int, int]] = []
    for x, y, dx, dy in inp:
        x = (x+(times*dx))%width
        y = (y+(times*dy))%height
        final_pos.append((x, y))
    
    # print(final_pos)
    
    tl, tr, bl, br = 0, 0, 0, 0

    for x, y in final_pos:
        if x < width // 2:
            if y < height // 2:
                tl += 1
            elif y > height // 2:
                bl += 1
        elif x > width // 2:
            if y < height // 2:
                tr += 1
            elif y > height // 2:
                br += 1
    return tl * tr * bl * br


def p2(inp: list[Robot], interactive = False):
    for i in range(times):
        img: list[list[int]] = [[0 for _ in range(height)] for _ in range(width)]
        for j, (x, y, dx, dy) in enumerate(inp):
            x = (x+dx)%width
            y = (y+dy)%height
            img[x][y] += 1
            inp[j] = (x, y, dx, dy)
        
        # theres probably 10 robots in a row in the picture right...?
        has_sign = False
        img_print = []
        for r in img:
            r_s = ''.join('.' if x == 0 else '#' for x in r)
            img_print.append(r_s)
            if '##########' in r_s:
                has_sign = True
        
        if has_sign:
            if interactive:
                print(i+1)
                for r in img_print:
                    print(r)
                print()
                input()
            else:
                return i+1


inp: list[Robot] = []
with open(f"day14/input{INPUT}.txt") as f:
    for line in f:
        p = line.split()[0]
        v = line.split()[1]

        x = int(p[2:].split(",")[0])
        y = int(p[2:].split(",")[1])
        dx = int(v[2:].split(",")[0])
        dy = int(v[2:].split(",")[1])

        inp.append((x, y, dx, dy))

print("p1", p1(inp))
print("p2", p2(inp))