cyfra_zycia = input("Podaj cyfre zycia: ")
while len(cyfra_zycia) > 1:
    suma = 0
    for cyfra in cyfra_zycia:
        suma += int(cyfra)
        print(cyfra)
        data = str(suma)
        print("Twoja Liczba Zycia: " + suma)