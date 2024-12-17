INPUT = ""
# INPUT = "_example"

def p1(reg: list[int], program: list[int]) -> list[int]:
    instruction_ptr = 0
    output = []
    while instruction_ptr < len(program):
        opcode = program[instruction_ptr]
        operand = program[instruction_ptr + 1]

        if int(operand) <= 3:
            combo = operand
        elif int(operand) <= 6:
            combo = reg[operand - 4]

        match opcode:
            case 0: # adv - A = A / pow(2, combo operand)
                reg[0] = reg[0] // pow(2, combo)
            case 1: # bxl - B = B ^ literal operand
                reg[1] = reg[1] ^ operand
            case 2: # bst - B = combo % 8
                reg[1] = combo % 8
            case 3: # jnz - no-op if A == 0, else jump to literal
                if int(reg[0]) > 0:
                    instruction_ptr = operand
                    continue
            case 4: # bxc - B = B ^ C
                reg[1] = reg[1] ^ reg[2]
            case 5: # out - add combo % 8 to output
                output.append(combo % 8)
            case 6: # bdv, B = A / combo operand
                reg[1] = reg[0] // pow(2, combo)
            case 7: # bdv, C = A / combo operand
                reg[2] = reg[0] // pow(2, combo)
            case _:
                raise ValueError()
        
        instruction_ptr += 2

    return output


def p2():
    for i in range(0,117441):
        reg_m = reg.copy()
        reg_m[0] = i
        output = p1(reg_m, program)
        if output == program:
            print(i)


reg: list[int] = [0, 0, 0]
program: list[int] = []
with open(f"day17/input{INPUT}.txt") as f:
    for i, line in enumerate(f):
        if i < 3:
            reg[i] = int(line.strip().split()[-1])
        if i == 4:
            program = list(map(int, line.strip().split()[-1].split(",")))

print("p1", ",".join(list(map(str, p1(reg.copy(), program)))))
print("p2")
p2()
