#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
#Согласно википедии, диапозон = интервал = (a , b). Крайние элементы не включаю.
list = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
def GetInt(str):
    n = int(input(f"Введите {str}: "))
    return n 
def minmax(list, a, b):
    if a > b :
        a, b = b, a
    list_of_indexes = []
    for i in range(len(list)):
        if list[i] < b and list[i] > a:
            list_of_indexes.append(i)
    return list_of_indexes
print(list)
print("список индексов:",minmax(list , GetInt("a") , GetInt("b")))        