if __name__ == "__main__":
    a,b,c = map(float,input().split())
    delta = b**2 - (4*a*c)
    x2 = (-b+(delta**0.5))/2*a
    x1 = (-b-(delta**0.5))/2*a
    print("x1 =",x1)
    print("x2 =",x2)
    pass