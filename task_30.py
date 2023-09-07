#Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.


def GetInt(str):
    n = int(input(f"Введите {str}: "))
    return n 
def progression(a,d,n):
    progression_list = []
    for i in range(0,n*d , d):
        progression_list.append(a+i)
    return progression_list
print(progression(GetInt("первый элемент прогрессии"),GetInt("разность элементов прогрессии"),GetInt("количество элементов прогрессии")))    

