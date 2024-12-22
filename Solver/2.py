import math
if __name__ == "__main__":
    xa,ya = map(float,input("nhap toa do diem A: ").split())
    xb,yb = map(float,input("nhap toa do diem B: ").split())
    ab = float(math.sqrt(((xb-xa)**2)+ ((yb-ya)**2)))
    print("|AB|= ",ab)
    pass