global jug_name, capacity
jug_name = [0,0]
capacity = [4,3]

def fill(jug_name,x,y):
    if(jug_name == 'A'):
        x = 4
        return x,y
    if (jug_name == 'B'):
        y = 3
        return x, y

def empty(jug_name,x,y):
    if (jug_name == 'A'):
        x = 0
        return x, y
    if (jug_name == 'B'):
        y = 0
        return x, y

def transfer(jug_name,x,y):
    if (jug_name == 'A'):
        z = (capacity[0] - x)
        if(z < y):
            x = 4
            y = y - z
            return x, y
        if(z >= y):
            x = x + y
            y = 0
            return x, y
    if (jug_name == 'B'):
        z = (capacity[1] - y)
        if (z < x):
            y = 3
            x = x - z
            return x, y
        if (z >= x):
            y = x + y
            x = 0
            return x, y

x = y = 0
while(True):
        print("1.Enter 1 for fill\n"
              "2.Enter 2 for empty\n"
              "3.Enter 3 for transfer\n"
              "4.Enter 4 for display\n")
        n= int(input("Enter number: "))
        if(n == 4):
            print(x,",",y,"\n")
        jug_name = input("Enter 'A' or 'B': ")

        if(n == 1):
            if(x == 4 and y == 3):
                print("A and B are already full\n")
            if(jug_name == 'A'):
                if(x == 4):
                    print("A is already full\n")
                if(x == 0):
                    x, y = fill(jug_name,x,y)
                if(0<x<4):
                    print("Can't fill\n")

            else:
                if(y == 3):
                    print("B is already fill")
                if(y == 0):
                    x, y = fill(jug_name,x,y)
                if(0<y<3):
                    print("Can't fill\n")

        if(n == 2):
            if (x == 0 and y == 0):
                print("A and B are already empty\n")
            if (jug_name == 'A'):
                if (x == 0):
                    print("A is already empty\n")
                if (0 < x <= 4):
                    x, y = empty(jug_name,x,y)

            else:
                if (y == 0):
                    print("B is already empty")
                if (0 < y <= 3):
                    x, y = empty(jug_name,x,y)

        if (n == 3):
            if (x == 4 and y == 3):
                print("Can't transfer\n")
            if (jug_name == 'A'):
                if (x == 4):
                    print("Can't transfer\n")
                if (0 <= x < 4):
                    x, y = transfer(jug_name,x,y)

            else:
                if (y == 3):
                    print("Can't transfer\n")
                if (0 <= y < 3):
                    x, y = transfer(jug_name,x,y)

fill(jug_name,x,y)
empty(jug_name,x,y)
transfer(jug_name,x,y)
