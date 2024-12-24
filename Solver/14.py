def check(m, nhuan):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        return 29 if nhuan else 28
    else:
        return 0

def is_leap_year(year):
    # Kiểm tra năm nhuận
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

while True:
    try:
        dd, mm, yy = map(int, input("Nhập ngày, tháng, năm (dd mm yyyy): ").split())
    except ValueError:
        print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")
        continue
    nhuan = is_leap_year(yy)
    if mm < 1 or mm > 12 or dd < 1 or dd > check(mm, nhuan):
        print("Ngày tháng năm không hợp lệ. Vui lòng nhập lại.")
        continue

    dd += 1
    if dd > check(mm, nhuan): 
        dd = 1
        mm += 1
        if mm > 12:
            mm = 1
            yy += 1

    print(f"Ngày tiếp theo: {dd:02}/{mm:02}/{yy}")
