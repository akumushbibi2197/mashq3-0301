#1-misol
n = int(input("Nechta element chiqarilsin: "))

a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#2-misol
n = int(input("N sonini kiriting: "))

print("Tub sonlar:")
for son in range(2, n + 1):
    tub = True
    for i in range(2, son):
        if son % i == 0:
            tub = False
            break
    if tub:
        print(son, end=" ")

#3-misol
sonlar = input("Sonlarni bo‘sh joy bilan kiriting: ")
royxat = list(map(int, sonlar.split()))

royxat.sort()
print("Saralangan ro‘yxat:", royxat)

#4-misol
sonlar = input("Sonlarni bo‘sh joy bilan kiriting: ")
royxat = list(map(int, sonlar.split()))

eng_kop = max(set(royxat), key=royxat.count)
print("Eng ko‘p uchraydigan element:", eng_kop)

#5-misol
jumla = input("Jumla kiriting: ")
sozlar = jumla.split()
print("So‘zlar soni:", len(sozlar))
