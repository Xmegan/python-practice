range1 = int(input("Please insert the first number of list: "))
range2 = int(input("Please insert the second number of list: "))
total = range(range1,range2)
print("You have chosen range from " + str(range1) + " to " + str(range2))
num = int(input("Now please insert a divisor: "))
new = []

for x in total:
    divisor = x%num
if divisor == 0:
    new.append(x)

print(new)