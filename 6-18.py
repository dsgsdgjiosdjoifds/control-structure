# Let x and y denote the coordinates of a point on the plane.
# Write a program that determines in which quadrant of the coordinate system the point P(x, y) is located or on which axis it is located, or that it is located in the position (0,0) of the coordinate system.

x = 5
y = 2

quadrant = "first (top right)"
if x == 0 and y == 0:
    print(f"Point P({x},{y}) is located in the center of the coordinate system")
elif x < 0 and y >= 0:
    quadrant = "second (top left)"
elif x < 0 and y < 0:
    quadrant = "third (bottom left)"
elif x > 0 and y < 0:
    quadrant = "fourth (bottom right)"

print(f"Point P({x},{y}) is in the {quadrant} quadrant of the coordinate system")