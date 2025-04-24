while True:
    prani = input("S jakým tvarem si přejete pracovat? ")
    strana1 = 0
    strana2 = 0
    strana3 = 0
    if prani == "čtverec":
        strana1 = input("Zadejte délku strany ")
        operace = input("Jakou operaci si přejete provést? ")
        if operace == "obsah":
            octverce = int(strana1) * int(strana1)
            print("Obsah = ", int(octverce))
        elif operace == "obvod":
            obctverce = 4 * int(strana1)
            print("Obvod = ", int(obctverce))
    elif prani == "obdelník":
        strana1 = input("Zadejte délku strany a. ")
        strana2 = input("Zadejte délku strany b. ")
        operace = input("Jakou operaci si přejete provést? ")
        if operace == "obsah":
            oobdelniku = int(strana1) * int(strana2)
            print("Obsah = ", int(oobdelniku))
        elif operace == "obvod":
            obobdelniku = 2 * (int(strana1) + int(strana2))
            print("Obvod = ", obobdelniku)
    elif prani == "trojúhelník":
        strana1 = input("Zadejte délku strany a. ")
        strana2 = input("Zadejte délku strany b. ")
        strana3 = input("Zadejte délku strany c. ")
        if (int(strana1) + int(strana2)) > int(strana3) or (int(strana2) + int(strana3)) > int(strana1) or (int(strana1) + int(strana3)) > int(strana2):
            print("Trojúhelník lze narýsovat")
        else:
            print("Trojúhelník nelze narýsovat")
    else:
        print("Chybné zadání!")
    konec = input("Přejete si pokračovat? Pro pokračování stiskněte enter ")
    if konec == "ne":
        break