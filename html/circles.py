from math import pi
def circle(r):
    return pi*(r**2)
radi=[2,0,-3,2+5j,True,"radius"]
message="area of circles with r = {radius} is {area}."
for r in radi:
    a = circle(r)
    print(message.format(radius=r,area=a))