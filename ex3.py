UAH = int(input("Введіть ціну(гривні): "))
KOP = int(input("Введіть ціну(копійки): "))

howManyPencils = int(input("Введіть кількість олівців: "))

price = UAH + KOP / 100
price *= howManyPencils

priceUAH = int(price)
priceKOP = int((price - priceUAH) * 100)

print(f"{priceUAH} гривень")
print(f"{priceKOP} копійок")