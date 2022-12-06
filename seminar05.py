# 35. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найдите это число.

path = "C://GitHub//geekbrains//007_python//007_PY_S05//text.txt"
with open(path, "r") as file:
    ri = file.readline()

list = list(map(int, ri.split()))
error = list[0]
for i in range(1, len(list)):
    if list[i] - 1 != list[i - 1]:
        error = list[i - 1] + 1

print(f"{list} -> {error}")





# 1. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# *Пример:* 
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
    

# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = "вап вап кн г кур енш ен ыаап г68 ц к н ш енгр ыаымфы"
text.split()

newText = list(filter(lambda i: 'а' not in i and "б" not in i and "в" not in i, text.split()))
print(newText)