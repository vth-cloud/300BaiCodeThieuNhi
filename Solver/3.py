import math
if __name__ == "__main__":
    xc,yc = map(float,input("nhap toa do tam dtron C: ").split())
    xm,ym = map(float,input("nhap toa do diem m: ").split())
    r = float(input("nhap ban kinh: "))
    cm = float(math.sqrt(((xm-xc)**2)+ ((ym-yc)**2)))
    if cm>r:
        print("M nam ngoai C()")
    elif cm == r:
        print("M nam tren C()")
    else:
        print("M nam trong C()")
    pass