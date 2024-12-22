import math

if __name__ == "__main__":
    x_minute = int(input("Nhập góc tính bằng phút: "))  
    x_degree = x_minute / 60
    gocnum = x_degree % 360
    if 0 <= gocnum < 90:
        quadrant = 1
    elif 90 <= gocnum < 180:
        quadrant = 2
    elif 180 <= gocnum < 270:
        quadrant = 3
    else:
        quadrant = 4
    
    x_radian = math.radians(gocnum)
    cos_x = math.cos(x_radian)
    print(f"{x_minute} phut thuoc goc {quadrant} cua vong tron.")
    print(f"cos(x) = {cos_x:.6f}")
