max = 0
for i in range(10):
    print("Zadejte číslo")
    cislo = int(input())
    if cislo > max:
        max = cislo
print("Největší zadané číslo bylo " + str(max))