# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#  Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

dcmum = ""
bnnum = int(input("Введите число: "))
while bnnum != 0:
    dcmum = str(bnnum%2) + dcmum
    bnnum //=2
print(dcmum)