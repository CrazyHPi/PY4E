# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

totalConf = 0
counter = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    totalConf += float(line[line.find(":") + 1:].strip(" "))
    counter += 1

fh.close()

print("Average spam confidence:", totalConf / counter)
