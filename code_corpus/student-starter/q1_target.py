# Q1: Practice Target
# Read three lines: name, target, completed.
# Print the name, remaining minutes, and DONE or KEEP GOING.
# Write your solution below. Use input(), print(), and if/else.
name = input()
target = int(input())
completed = int(input())
print(name)
if completed < target:
    remain = target - completed
    print(remain)
    print("KEEP GOING")
else:
    print(0)
    print("DONE")