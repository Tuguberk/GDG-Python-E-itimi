def case1(sayi):
    if sayi < 0:
        print("negatif")
    elif sayi == 0:
        print("sıfır")
    else:
        print("pozitif")

sayi = int(input("bir sayı gir: "))
case1(sayi)
case1(-8)