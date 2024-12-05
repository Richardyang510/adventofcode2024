import re

def _extract_mul(op: str) -> int:
    v = list(map(int, op[4: -1].split(",")))
    l = v[0]
    r = v[1]
    return l*r

def p1(inp: str) -> int:
    matches = re.findall("mul\\([\\d]+,[\\d]+\\)", inp)
    s = 0
    for op in matches:
        s += _extract_mul(op)
    return s

def p2(inp: str) -> int:
    matches: list[str] = re.findall("(mul\\([\\d]+,[\\d]+\\))|(do\\(\\))|(don't\\(\\))", inp)
    s = 0
    enabled = True
    for mul_op, do_op, dont_op in matches:
        if do_op == "do()":
            enabled = True
        elif dont_op == "don't()":
            enabled = False
        elif enabled and mul_op:
            s += _extract_mul(mul_op)
    return s

# example
txt = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
print("example p1", p1(txt))

s = 0
inp = ""
with open(f"day03/input.txt") as f:
    for line in f:
        inp += line
s = p1(inp)
print("p1", s)

# example
txt2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
print("example p2", p2(txt2))

s = 0
inp = ""
with open(f"day03/input.txt") as f:
    for line in f:
        inp += line
s = p2(inp)
print("p2", s)