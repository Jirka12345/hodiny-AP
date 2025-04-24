mojepole = ["pomeranč", "jablko", "citron", "meloun", "švestka", "kumqat"]
print(mojepole)
print(len(mojepole))
print(mojepole[2])
#print(mojepole[int(input("Zadejte pozici"))])
duplist = mojepole[2:5]
print(mojepole)
print(duplist)

if "jablko" in mojepole:
    print("Jablko tam je")

mojepole[-2] = "Samice hrabáče"
print(mojepole)

mojepole.append("grep")
print(mojepole)