log = " hall-a, HALL-B, hall-a, , hall-c, HALL-B, hall-a "
bolimlar=log.split(",")
tozalangan=[]
for bolim in bolimlar:
    bolim=bolim.strip().upper()
    if bolim:
        tozalangan.append(bolim)
noyob=set(tozalangan)
print("Tozalangan: ",",".join(tozalangan))
print("Noyob bolimlar: ",len(noyob))