#Збираємо данні
s1 = int(input("Введіть відстань першого відрізку: "))
s2 = int(input("Введіть відстань другого відрізку: "))
s3 = int(input("Введіть відстань третього відрізку: "))
s4 = int(input("Введіть відстань четвертого відрізку: "))
print()
v1 = int(input("Введіть швидкість першого відрізку: "))
v2 = int(input("Введіть швидкість другого відрізку: "))
v3 = int(input("Введіть швидкість третього відрізку: "))
v4 = int(input("Введіть швидкість четвертого відрізку: "))
print()
t = int(input("Введіть час зупинки: "))


#Обролеяємо данні
t1 = s1 / v1
t2 = s2 / v2
t3 = s3 / v3
t4 = s4 / v4

totalTime = t1 + t2 + t3 + t4 + t

#Виводимо данні
print(f"На поїздку було витрачено {totalTime} годин")