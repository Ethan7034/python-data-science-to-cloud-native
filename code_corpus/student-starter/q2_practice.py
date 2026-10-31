# Q2: Practice Log
# Read n, then n space-separated practice-minute values on the next line.
# Print total minutes, days meeting the 30-minute target, and remaining minutes.
# Write your solution below. Use a list and a loop.
n = int(input())
time_list = list(map(int,input().split()))
time_total = sum(time_list)
t_days = 0
for k in time_list:
    if k>= 30:
        t_days += 1
remain = [max(0,30 - k) for k in time_list]
print(time_total)
print(t_days)
print(*remain)