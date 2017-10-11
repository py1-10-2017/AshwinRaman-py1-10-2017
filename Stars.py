def draw_stars(x):
    for i in range (0,len(x)):
        print "*" * x[i]

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)


def draw_stars2(x):
    for i in range (0,len(x)):
        if isinstance(x[i], int):
            print "*" * x[i]
        elif isinstance(x[i],str):
            print x[i][0:1].lower()

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars2(x)
