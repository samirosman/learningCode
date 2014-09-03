import time
def timer(mlimit):
    for m in range(0, 60):
        if m == mlimit:
            print ("take a break \a")
            break
        else:
            for s in range(0, 60):
                time.sleep(1)
                print ("\a Elapsed time : %s:%s" % (m, s),)

limit = 52
timer(limit)
