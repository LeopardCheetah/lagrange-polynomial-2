import sys # exits code

print("this program will hopefully find a line that passes through N points")
print("only integer coordinates please :)")
# todo: accept fractions
point_count = input("How many points will you input?\n")

try:
    point_count = int(point_count)
    print()
except:
    print("That is not an integer number of points!")
    sys.exit(1)
    # program is terminated

if point_count < 0:
    print("You cannot input a negative amount of points")
    sys.exit(1)


x_coords = []
y_coords = []
for i in range(point_count):
    print(f"Enter the x and y coordinates of the {i+1}th number please (seperated by a space): ")
    x, y = input().split()
    x_coords.append(int(x))
    y_coords.append(int(y))
    # check that it is a legtimiate function (1 does not map to 2 and 3)

    if len(x_coords) != len(set(x_coords)):
        #not a function, overlap
        print("the point that was entered makes an equation impossible (not a function)")
        sys.exit(1)

print(x_coords, y_coords)

# some base cases

if point_count == 0:
    print("y = 0")
    sys.exit(0)

if point_count == 1:
    print(f"y = {y_coords[0]}")
    sys.exit(0)