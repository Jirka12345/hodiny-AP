print("Zadejte první číslo")
y = int(input())
print("Zadejte druhé číslo")
x = int(input())
if x > y: 
    print(str(x) + " je větší než " + str(y))
elif x==y:
     print("čísla jsou stejná")
else:
    print(str(x) + " je menší než " + str(y))