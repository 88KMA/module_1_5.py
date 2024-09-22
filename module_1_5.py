immutable_var = 1, 2, 3, True, 'Name', ['apple', 'coconut', 'peach']
print(immutable_var)
immutable_var[3] = False #программа выдает ошибку, т.к. переменной immutable_var присвоен кортеж. Элементы кортежа менять нельзя, а это значит, что элементы переменной immutable_var тоже изменить не получится. Но мы можем изменить элементы списка, который явлается элементом кортежа: "['apple', 'coconut', 'peach']", командой приведенной ниже в коде программы. И чтобы увидеть результат, нам нужно удалить команду: "immutable_var[3] = False", которая вызывает ошибку.
immutable_var[5][2] = False
print(immutable_var)
