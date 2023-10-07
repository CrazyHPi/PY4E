import re

# one line version
print(sum([int(i) for i in re.findall("[0-9]+", open("regex_sum_1904303.txt").read())]))
