# this code almost work
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        innum = int(num)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest = innum
    elif largest < innum:
        largest = innum
    if smallest is None:
        smallest = innum
    elif smallest > innum:
        smallest = innum

print("Maximum is", largest)
print("Minimum is", smallest)