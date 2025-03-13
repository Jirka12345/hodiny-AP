while True:
    cislo1 = int(input("Zadejte první číslo "))
    cislo2 = int(input("Zadejte druhé číslo "))
    print("1. Součet 2. Součin, 3. Rozdíl, 4.")
    operace = int(input("Vyberte číslo operace, kterou chcete použít "))
    match operace:
        case 1:
            soucet = cislo1 + cislo2
            print("Součet = " + str(soucet))
        case 2:
            soucin = cislo1 * cislo2
            print("Součin = " + str(soucin))
        case 3:
            rozdil = cislo1 - cislo2
            print("Rozdíl = " + str(rozdil))
        case 4:
            if cislo2 == 0:
                print("Nelze dělit nulou")
            else:
                podil = cislo1 / cislo2
                print("Podíl = " + str(podil))
    konec = str(input("Přejete si ukončin program ? "))
    if konec == "Y" or konec == "y":
        print("Program ukončen")
        break
    