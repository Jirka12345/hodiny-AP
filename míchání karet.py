import random
cards=list(range(1,33))
shuffled = []
n=len(cards)
counter = 0
while n: #pokud se n = 0 tak je to false
    i=random.randint(0,len(cards)-1) #vezme random číslo z velikosti proměný "cards"
    counter +=1
    if (cards[i] != 0):
        shuffled.append(cards[i]) #vezme to random číslo z "i" a dá ho do "shuffled"
        cards[i]=0
        n-=1
print(cards)
print(shuffled)
print(counter)