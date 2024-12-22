import random
t1 = 0
t2 = 0
while True:
    s = input("Nhap ky tu (bao-da-keo), ky tu khac đe thoat: ")
    if s not in ['bao', 'da', 'keo']: 
        print("Thoát chương trình.")
        break
    quocdung = random.choice(["bao", "da", "keo"])
    if (quocdung == "bao" and s== "keo") or (quocdung == "da" and s =="bao") or (quocdung=="keo" and s =="da"):
        t1 +=1
    if (s == "bao" and quocdung == "keo") or (s == "da" and quocdung == "bao") or (s=="keo" and quocdung=="da"):
        t2 += 1
    print("Computer: ",quocdung)
    print("Ty so human - computer: ",t1,"-",t2)


    
