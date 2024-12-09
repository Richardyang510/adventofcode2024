INPUT = ""
# INPUT = "_example"


def p1(inp: str) -> int:
    inp = inp.strip()
    fs = []
    blk_id = 0
    for i, c in enumerate(inp):
        if i%2==0:
            # block
            fs += [blk_id] * int(c)
            blk_id += 1
        else:
            # space
            fs += ["."] * int(c)
    # print(fs)

    left = 0
    right = len(fs) - 1

    while left < right:
        if fs[left] != ".":
            left += 1
        elif fs[right] == ".":
            right -= 1
        else:
            fs[left] = fs[right]
            fs[right] = "."

    n = 0
    for i, c in enumerate(fs):
        if c != ".":
            n += i * int(c)

    return n


def print_p2_fs(fs: list[tuple[int, int]]):
    o = ""
    for (v, s) in fs:
        if v >= 0:
            o += str(v) * s
        else:
            o += "." * s
    if INPUT == "_example":
        print(o)


def merge_blks(fs: list[tuple[int, int]]):
    idx = 0
    while idx < len(fs) - 1:
        if fs[idx][0] == -1 and fs[idx + 1][0] == -1:
            fs[idx] = (-1, fs[idx][1] + fs[idx + 1][1])
            del fs[idx+1]
            idx -= 1
        idx += 1



def p2(inp: str) -> int:
    inp = inp.strip()
    fs: list[tuple[int, int]] = []  # val, block_size
    blk_id = 0
    for i, c in enumerate(inp):
        # don't add empty blocks
        if c == "0":
            continue
        if i%2==0:
            # block
            fs.append((blk_id, int(c)))
            blk_id += 1
        else:
            # space
            fs.append((-1, int(c)))
    print_p2_fs(fs)
    # print(fs)

    for blk_id_s in reversed(range(blk_id)):
        # for each block ID, first find its pos
        blk_pos = -1
        blk_size = 0
        for i, (v, s) in enumerate(reversed(fs)):
            if v == blk_id_s:
                blk_pos = len(fs) - i - 1
                blk_size = s
                break
        # print("blk", blk_id_s, "pos", blk_pos, "size", blk_size)
        # search from left to right for any spaces that can fit
        for i, (v, s) in enumerate(fs):
            if v < 0 and s >= blk_size and i < blk_pos:
                # print("found", i, s)
                # replace the block at the end
                fs[blk_pos] = (-1, blk_size)
                # fragment the block at index i
                fs[i] = (blk_id_s, blk_size)
                if s-blk_size > 0:
                    # this is ok since enumerate will go to the pointer at the old i+1
                    # i, new i+1, old i+1
                    # ^           ^
                    # current     next
                    # this probably would have been better as a linked list with a dict for the nodes
                    fs.insert(i + 1, (-1, s-blk_size))
                merge_blks(fs)
                print_p2_fs(fs)
                break

    print_p2_fs(fs)

    n = 0
    idx = 0
    for v, s in fs:
        if v >= 0:
            for idx_d in range(s):
                n += (idx + idx_d) * v
        idx += s

    return n


inp = ""
with open(f"day09/input{INPUT}.txt") as f:
    for line in f:
        inp += line
print("p1", p1(inp))
print("p2", p2(inp))