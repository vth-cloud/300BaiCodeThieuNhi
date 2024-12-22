if __name__ == "__main__":
    a,b,c = map(int,input().split())
    list = [a,b,c]
    list.sort()
    print("tang dan:",*list)
    pass