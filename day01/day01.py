INPUT = ""
# INPUT = "_example"

list_left = []
list_right = []

with open(f"day01/input{INPUT}.txt") as f:
    for line in f:
        v = line.strip().split()
        l = v[0]
        r = v[1]
        list_left.append(l)
        list_right.append(r)

list_left = sorted(list_left)
list_right = sorted(list_right)

s = 0
for left, right in zip(list_left, list_right):
    s += abs(int(left)-int(right))
print("p1", s)

# p2
s = 0
for v in list_left:
    num_occur = list_right.count(v)
    s += int(v) * num_occur
print("p2", s)