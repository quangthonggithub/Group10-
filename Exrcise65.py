import math


x1 = float(input("Enter the x part of the coordinate: "))
y1 = float(input("Enter the y part of the coordinate: "))
a=x1
b=y1

chu_vi = 0

while True:
    x2_str = input("Enter the x part of the coordinate: ")
    
    if x2_str == "":
        break

    x2 = float(x2_str)
    y2 = float(input("Enter the x part of the coordinate: "))
    
   
    chu_vi += math.sqrt((x2 - x1) * 2 + (y2 - y1) * 2)

    
    x1 = x2
    y1 = y2
chu_vi +=  math.sqrt((x2 - a) * 2 + (y2 - b) * 2)
print(f"The perimeter of that polygon is ",chu_vi)