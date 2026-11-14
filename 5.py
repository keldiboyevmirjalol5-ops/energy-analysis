import json
with open("Imtihon/inventar.json","r")as file:
    inventar=json.load(file)
    for item in inventar:
        print("Nom: ",item["nom"])
        print("Jami: ",item["jami"])
        print("Band: ",item["band"])
    try:
        item["band"]=int(item["band"])
    except ValueError:
            item["band"]=0
    except Exception as e:
        print("Xato yuz berdi:", e)
with open("Imtihon/mavjud_kitoblar.json","w")as f:
    data=json.dump(inventar,f)
    print("Malumot yozildi✅")
    f.close()