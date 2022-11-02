apples = int(input("Введіть кількість яблук: "))
kids = int(input("Введіть кількість дітей: "))

forOneKid = apples // kids
toBasket = apples % kids

print(f"Діти отримали по {forOneKid} яблук")
print(f"У кошику лишилося {toBasket} яблук")