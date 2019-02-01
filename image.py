#Colin Hosking
import math

file = open("image.ppm","w")
head = "P3"
dimensions = "800 800"
maxval = "255"

file.write(head + "\n" + dimensions + "\n" + maxval + "\n")

def dist(x1,y1,x2,y2):
    sqx = math.pow(x1-x2,2)
    sqy = math.pow(y1-y2,2)
    return math.pow(sqx + sqy,.5)

for y in range(0,800):
    for x in range(0,800):
        R = int(math.floor(( x / 800.0 ) * 255))
        G = int(math.floor(( y / 800.0 ) * 255))
        B = 0

        if (x % 10 == 0):
            R = int(math.floor(( dist(x,y,0,0) / 1132 ) * 255))
            B = int(math.floor(( dist(x,y,401,401) / 566 ) * 255))
        if (y % 10 == 0):
            R = int(math.floor(( dist(x,y,800,800) / 1132 ) * 255))
            B = int(math.floor(( dist(x,y,401,401) / 566 ) * 255))
        if (y%10 == x%10):
            G = 127
        if (-y%10 == x%10):
            G = 127
        file.write(str(R) + " " + str(G) + " " + str(B) + " ")
    file.write("\n")

file.close()
