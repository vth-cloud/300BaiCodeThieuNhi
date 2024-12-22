def calS(x1, y1, x2, y2, x3, y3):
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

def point_position_in_triangle():
    print("Enter coordinates of triangle vertices:")
    xA, yA = map(float, input("A(xA, yA): ").split())
    xB, yB = map(float, input("B(xB, yB): ").split())
    xC, yC = map(float, input("C(xC, yC): ").split())
    xM, yM = map(float, input("M(xM, yM): ").split())
    area_ABC = calS(xA, yA, xB, yB, xC, yC)
    area_MAB = calS(xM, yM, xA, yA, xB, yB)
    area_MBC = calS(xM, yM, xB, yB, xC, yC)
    area_MCA = calS(xM, yM, xC, yC, xA, yA)
    total_area = area_MAB + area_MBC + area_MCA

    if abs(total_area - area_ABC) < 1e-6:
        if area_MAB == 0 or area_MBC == 0 or area_MCA == 0:
            print("M nam tren canh tam giac ABC")
        else:
            print("M nam trong canh tam giac ABC")
    else:
        print("M nam ngoai tam giac ABC")

# Run the function
point_position_in_triangle()
