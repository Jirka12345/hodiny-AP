import random
cards=list(range(1,33))
shuffled=[]
n=len(cards)
counter = 0

while n > 1:
    n -= 1
    i=random.randint(0,n)
    cards[i], cards[n] = cards[n], cards[i]
    print(i,n,sep="||")
    print(cards)
    counter += 1
print(counter)