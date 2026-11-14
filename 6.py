import csv

natija = {}

with open("Imtihon/qatnov.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for qator in reader:
        yonalish = qator["yonalish"]
        yolovchi = int(qator["yolovchi"])

        if yonalish in natija:
            natija[yonalish] += yolovchi
        else:
            natija[yonalish] = yolovchi

for yonalish, jami in natija.items():
    print(f"{yonalish}-yo‘nalish: {jami} nafar")