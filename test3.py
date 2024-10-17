
def case2(liste):
    if len(liste) > 0:
        toplam = 0
        for i in liste:
            toplam += i
        return toplam / len(liste)
    else:
        print("Liste hatalı")
        return 0

liste = [1,2,3,45,7,24]
sonuc = case2([])
print(f"ortalama : {sonuc}")    