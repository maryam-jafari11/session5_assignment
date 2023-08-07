import math
a = int(input("inter a :"))
b = int(input("inter b :"))
c = int(input("inter c :"))

delta = math.pow(b, 2) - (4*a*c)
print("delta is %s for a:%s b: %s, c: %s" %(delta, a, b, c,))

if delta > 0 : 
    x1 = -b + math.sqrt(delta) / (2*a)
    x2 = -b - math.sqrt(delta) / (2*a)
    print(x1,"and",  x2, "are answers of equation")
elif delta <0 : 
    print("your quadratic equation not have a real answer")
elif delta == 0 :     
    x1 = (-b) / (2*a)
    print("answer is", x1)

