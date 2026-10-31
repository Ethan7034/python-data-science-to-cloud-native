# Q3: Supplies Counter
# Read n delivery records, then q item-name queries.
# Print the accumulated quantity for each query, or 0 for a missing item.
# Write your solution below. Use a dictionary and loops.
n = int(input())
dic = {}
for i in range(n):
    line = input().split()
    item = line[0]
    quantity = int(line[1])
    if item in dic:
        dic[item] += quantity
    else:
        dic[item] = quantity
q = int(input())
final = ""
for j in range(q):
    query = input()
    if query in dic:
        final = final + str(dic[query]) + "\n"
    else:
        final = final + "0\n"
print(final, end="")