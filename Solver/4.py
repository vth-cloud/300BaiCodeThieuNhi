if __name__ == "__main__":
    while True:
        a,b,c = map(float,input("nhap 3 canh a,b,c: ").split())
        if a <= 0 or b <= 0 or c <= 0:
            print("Vui lòng nhập lại!")
        else:
            break
    if a==b==c:
        print("Tam Giac Deu")
    elif a==b or b==c or a==c:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
            print("Đây là tam giác vuông cân.")
        else:
            print("Đây là tam giác cân.")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
            print("Đây là tam giác vuông.")
    else:
            print("Đây là tam giác thường.")
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    print("Dien Tich S: ",s)

    pass