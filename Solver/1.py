import math
if __name__ == "__main__":
    s = float(input("Nhap Dien Tich S: "))
    n = 3.141593
    r = float(math.sqrt(s/4/n))
    v = 4/3*n*r**3
    print("The Tich V: ",v)
    pass
