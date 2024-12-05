INPUT = ""
# INPUT = "_example"

def is_safe(report: list[int]) -> int:
    report_d = []
    for i in range(len(report) - 1):
        report_d.append(report[i] - report[i+1])
    
    if all(l >= 1 and l <= 3 for l in report_d) or all(l <= -1 and l >= -3 for l in report_d):
        return 1
    return 0

s = 0
with open(f"day02/input{INPUT}.txt") as f:
    for line in f:
        report = list(map(int, line.strip().split()))
        s += is_safe(report)

print("p1", s)

# n^3 solution for p2 but I have CPU
s = 0
with open(f"day02/input{INPUT}.txt") as f:
    for line in f:
        report = list(map(int, line.strip().split()))
        # Iterate over all combinations of removing a single element
        s_report = 0
        for skip_idx in range(len(report)):
            skipped_report = [l for i, l in enumerate(report) if i != skip_idx]
            s_report = is_safe(skipped_report)
            if s_report >= 1:
                break
        s += s_report
print("p2", s)
