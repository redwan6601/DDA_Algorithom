import matplotlib.pyplot as plt
from matplotlib import pyplot
def  DDA(x0, y0, xn, yn):
    dx=abs(xn-x0)
    dy=abs(yn-y0)
    m=dy/dx #slope
    n=max(dx,dy) #step
    xp=x0
    yp=y0
    xlist=[xp]
    ylist=[yp]

    for i in range(n):
        if m<1:
            xp=xp+1
            yp=yp+m
        elif m==1:
            xp=xp+1
            yp=yp+1
        elif m>1:
            xp=xp+1/m
            yp=yp+1
        print("x=",  xp, end=", ") #original
        print("y=", yp, end="\n ")
        xlist.append(round(xp))
        ylist.append(round(yp))
    print(xlist)
    print(ylist)
    plt.plot(xlist, ylist, linestyle="--",marker="+")
    plt.show()


#main
x0=int(input("insert x0:\n"))
y0=int(input("insert x0:\n"))

xn=int(input("insert x0:\n"))
yn=int(input("insert x0:\n"))
DDA(x0, y0, xn, yn)
