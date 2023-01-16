# this code almost work
def computepay(hours, rate):
    if hours > 40:
        pay = 1.5 * rate * (hours - 40.0) + (40 * rate)
    else:
        pay = hours * rate
    return pay
                
sh = input("Enter hours:")
sr = input("Enter rate:")
fh = float(sh)
fr = float(sr)

pay = computepay(fh, fr)

print("Pay",pay)