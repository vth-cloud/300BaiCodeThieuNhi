def conv(n):
    return [int(num) for num in str(n)]

def sumEven(list):
    tong = 0
    for so in list:
        doub = so * 2
        if doub >= 10:
            tong += doub // 10 + doub % 10
        else:
            tong += doub
    return tong

if __name__ == "__main__":
    while True:
        s = input("SIN (0) De Thoat: ")
        if s == "0":
            print("Thoat chuong trinh.")
            break

        if len(s) == 0 or not s.isdigit():
            print("SIN ko hop le!")
            continue
        checkNum = conv(s)
        # xac dinh so ktra
        chekc = checkNum[-1]
        checkNum = checkNum[:-1]
        s1 = sum(num for idx, num in enumerate(checkNum, start=1) if idx % 2 != 0)

        # tinh s2
        even = [num for idx, num in enumerate(checkNum, start=1) if idx % 2 == 0]
        s2 = sumEven(even)
        total = s1 + s2 + chekc
        if total % 10 == 0:
            print("SIN hop le!")
        else:
            print("SIN ko hop le!")
        # dit con me kho vcl
