kodlar = [" UZ-2026-AB1234 ", "UZ-26-AB1234", "UZ-2026-aB1234"]
def tekshirish(kod):
    kod=kod.strip()
    qismlar=kod.split("-")
    if len(qismlar)==3:
        davlat=qismlar[0]
        yil=qismlar[1]
        seriya=qismlar[2]

        if (davlat=="UZ" and
        len(yil)==4 and yil.isdigit() and
        len(seriya)==6 and 
        seriya[:2].isalpha() and 
        seriya[:2].isupper() and
        seriya[2:].isdigit()):
            return f"{kod} - To'g'ri"
    return f"{kod} - Noto'g'ri"
for kod in kodlar:
    print(tekshirish(kod))