INPUT = ""
#INPUT = "_example"

inp = ""
with open(f"day07/input{INPUT}.txt") as f:
    for line in f:
        inp += line

def _genbin(n, combs, ops, bs = []):
    if len(bs) == n:
        combs.append(bs)
    else:
        for o in ops:
            bs2 = bs.copy()
            bs2.append(o)
            _genbin(n, combs, ops, bs2)

def genbin(n, ops = ["+", "*"]):
    combs = []
    _genbin(n, combs, ops, [])
    return combs

def p1(inp: str, is_p2: bool = False) -> int:
    n = 0
    for line in inp.split("\n"):
        tot = int(line.split(":")[0])
        vals = list(map(int, line.split(":")[1][1:].split(" ")))

        if is_p2:
            op_combs = genbin(len(vals) - 1, ["+", "*", "|"])
        else:
            op_combs = genbin(len(vals) - 1)

        for op in op_combs:
            calc_tot = vals[0]
            for v, o in zip(vals[1:], op):
                if o == "+":
                    calc_tot += v
                elif o == "*":
                    calc_tot *= v
                elif is_p2 and o == "|":
                    calc_tot = int(str(calc_tot) + str(v))
            if calc_tot == tot:
                n += tot
                break

    return n

print("p1", p1(inp))
print("p2", p1(inp, True))