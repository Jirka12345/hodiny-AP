i = 1
end = int(input("Zadjete číslo jehož faktoriál chcete "))
faktorial = 1
for i in range(end):
    i = i + 1
    faktorial = int(faktorial * i)
    print("Faktorial = " + str(faktorial))