import re

name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1904303.txt"
handle = open(name)

total = 0

for line in handle:
    temp = re.findall("[0-9]+", line)
    if len(temp) != 0:
        for i in temp:
            total += int(i)

print(total)
