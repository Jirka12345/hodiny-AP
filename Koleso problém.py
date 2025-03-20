num = int(input("Zadejte přirozené číslo"))
counter = 0 #počet kroků

while num != 1:
    if num%2 == 0:
        num = num = 2 #jestli to číslo má zbytek tak se vydělí dvěma.
    else:
        num = (num * 3) + 1 #jestli zbyde něco jinýho než 0 tak se vynásobí třema a přičte se jednička
    counter += 1 #přičte se krok
    print(num)
    
print("Pro vyřešení problému bylo potřeba " + str(counter) + "kroků")