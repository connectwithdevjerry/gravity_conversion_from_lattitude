from math import sin, pi

lattitude = input("Enter latitude value (e.g 90d 20m 05s): ")

def convertLattitudeToGravity(lattitude):
    degrees, mins, secs = lattitude.split(" ")
    degrees = int(degrees.removesuffix("d"))
    mins = int(mins.removesuffix("m"))/60
    secs = int(secs.removesuffix("s"))/3600

    lattitude = (degrees+mins+secs) * 2 * pi/360

    sin_squared = sin(lattitude) ** 2
    sin_2squared = sin((2 *lattitude)) ** 2

    gravity = 978.049 * (1 + 0.0052884*sin_squared + 0.0000059*sin_2squared )

    return gravity

gravity = convertLattitudeToGravity(lattitude)
print("gravity value is: ", gravity)
