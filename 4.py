xizmatlar = {
    "diagnostika": 50000,
    "tozalash": 80000,
    "sozlash": 40000,
    "almashtirish": 120000
}
def hisobla(*args, **kwargs):
    jami=0
    for xizmat in args:
        jami+=xizmatlar[xizmat]
    chegirma=kwargs["chegirma"]
    mijoz=kwargs["mijoz"]

    tolov=jami-(jami*chegirma)

    print("Mijoz:", mijoz)
    print("Jami:", jami)
    print("Chegirma:", chegirma, "%")
    print("To'lov:", tolov)

hisobla("diagnostika",
    "tozalash",
    "sozlash",
    mijoz="Nodira",
    chegirma=10)

