haroratlar = [-20, -19, -17, -16, -18, -21, -15, -14, -20]
xavfli=0
jami=0
for harorat in haroratlar:
    if harorat-18:
        xavfli+=1
        jami+=harorat
        ortacha=jami/xavfli
        print("Xavfli harorat: ", harorat)
        print("O'rtacha xavfli harorat: ", round(ortacha,2))