import random
win = 0
lose = 0
opakovani = int(input("Zadejte počet opakování, které chcete simulovat "))
for i in range(opakovani):
    print(i)
    car = random.randint(1,3)
    playerchoice = random.randint(1,3)
    while True:
        montyschoice = random.randint(1,3)
        if montyschoice != car and montyschoice != playerchoice:
            break
    #print(car, playerchoice, montyschoice)
    playersold = playerchoice
    while True:
        playerchoice = random.randint(1,3)
        if playerchoice != montyschoice and playerchoice != playersold:
            break
    if playerchoice == car:
        win += 1
    else:
        lose += 1
print(f"Hráč prohrál v {lose} případech a zvítězil v {win} případech \nto znamená že zvítězil v {((win/opakovani) * 100):.2f} % případů a prohrál v {((lose/opakovani) * 100):.2f} % případů.")