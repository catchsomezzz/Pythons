# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count = 0
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    startpos = line.find(":")
    digits = line[startpos+1:]
    fdigits = float(digits)
    total = fdigits+ total
    count = count +1
average = total/ count
print("Average spam confidence:",average)