verse1 = "bottles of beer on the wall.\n"
verse2 = "bottles of beer. \nTake one down, pass it around."
verse3 = "\nbottle of beer on the wall."

for n in range(99, 2, -1):
    if n > 2:
        print ("%d %s %d %s" % (n, verse1, n, verse2))
        n -= 1
        print ("%d %s" % (n, verse1))
    if n == 1:
        print ("%d %s" % (n, verse3))
    if n == 0:
        print ("%d %s" % (n, verse1))
