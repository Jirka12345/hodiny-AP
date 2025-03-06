while True: #cyklus který bude porbíhat pořád
    cislo = input("Zadejte číslo: ")
    if cislo .isdigit():
        max = int(cislo)
        break
    else:
        print("Nezadali ste číslo")

while input("Pro ukončení zadejte písmeno K ") != "K":
    cislo = input("Zadejte číslo ")
    if cislo.lstrip("-") .isdigit():
        cislo = int(cislo)
        if max < cislo:
            max = cislo
    else:
        print("Nezadali jste číslo")

print("Největší zadané číslo bylo " + str(max))