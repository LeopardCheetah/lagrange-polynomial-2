"""
import sympy

x, y = symbols('x y')

exp = sympy.expand((X+Y)**2)
  
print(exp)
"""
import sympy

print('simple polynomial finder, more reliable than matrices (at least more reliable than last time)')

#number of points the p goes through 
pointnum = int(input('how many points will you enter?'))

xcoordinates = []
ycoordinates = []

for i in range(pointnum):
    x, y = input('give me the x and y coordinates of number ', (i+1)).split()
    xcoordinates.append(int(x))
    ycoordinates.append(int(y))
    
#the nth point's coordinates are listed in (xcoordinates[n-1], ycoordinates[n-1])

a = symbols('a')
poly = ''

for j in xcoordinates:
    topstr = ''
    topstr
