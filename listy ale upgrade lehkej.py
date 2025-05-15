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

mojepole.insert(1,"ananas")
print(mojepole)

mojepole2 = ["paprika", "mrkev", "okurka"]
mojepole.extend(mojepole2) #přidá do 1. pole věci z 2. pole
print(mojepole)

mojepole.remove("ananas")
print(mojepole)

mojepole.pop(2)
print(mojepole)

print(mojepole2)
mojepole2.clear()
print(mojepole2)

del mojepole2
#print(mojepole2)

for i in mojepole:
    print(i)    #vypíše postupně celý pole

for i in range(len(mojepole)):
    print(i, mojepole[i])

abeceda = ["A", "F", "D", "C", "Z"]
print(abeceda)
abeceda.sort()
print(abeceda)

abeceda.sort(reverse=True)
print(abeceda)

mojepole.sort(key=str.lower) #Velký písmeno != první v pořadí
print(mojepole)

nums = [100, 50, 65, 82, 23]
nums.sort()
print(nums)

nums.reverse() #otočí pořadí v poli
print(nums)

mojepole2 = mojepole
print(mojepole)
print(mojepole2)

mojepole2[0] = "rajče"
print(mojepole)
print(mojepole2)

copylist = mojepole.copy()
copylist[0] = "pistácie"
print(mojepole)
print(copylist)
