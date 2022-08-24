from random import random
element = int(input('Введите количество элементов для формирования входного списка: '))
spisok = [int(random() * 1000) for i in range(1, element+1)]
print('Входый список:', spisok)
add = int(int(input('Введите элемент для добавления в список: ')))
spisok.append(add)
print('Новый список: ', spisok)
spisok.sort()
print('Отсортированный список по возрастанию: ', spisok)

def BinarySearchMin(spisok, add):
    first = 0
    last = len(spisok) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if spisok[mid] == add:
            index = mid
        else:
            if add < spisok[mid]:
                last = mid -1
            else:
                first = mid +1
    return  index -1

def BinarySearchMax(spisok, add):
    first = 0
    last = len(spisok) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if spisok[mid] == add:
            index = mid
        else:
            if add < spisok[mid]:
                last = mid -1
            else:
                first = mid +1
    return  index +1

index_0 = BinarySearchMin(spisok, add)

index_1 = BinarySearchMax(spisok, add)

if index_0 == -1:
     print('Введенный элемент наименьший в списке, его позиция =', index_0 +1)
else:
    print('Номер позиции элемента меньше введенного =', index_0)

if index_1 == len(spisok):
     print('Введенный элемент наибольший в списке, его позиция =', index_1 -1)
else:
    print('Номер позиции элемента больше введенного =', index_1)
