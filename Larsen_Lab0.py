import math

list1 = ["roads", "cities", "counties", "states"]
list2 = []

append_str = ".txt"

for x in list1:
    list2.append(str(x) + append_str)
    
print (list2)

x = math.pi
y = 0

while x ** y <= 30000:
    print(x ** y)
    y += 1