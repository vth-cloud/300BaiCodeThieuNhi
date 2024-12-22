a1,b1,c1 = map(int,input("Nhap a1, b1, c1: ").split())
a2,b2,c2 = map(int,input("Nhap a2, b2, c2: ").split())
d = (a1*b2) - (a2*b1)
dx = (c1*b2) - (c2*b1)
dy = (a2*c1) - (a1*c2)
if d != 0:
    x= dx /d
    y= dy /d
    print(x,y)
else:
    print("phuong trinh vo nghiem!")