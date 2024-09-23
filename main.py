# Дополнительное практическое задание по модулю:
# "Базовые структуры данных"

students = {'Johnny','Bilbo','Steve','Khedrik','Aaron'}
grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = sorted(students)
print('Sorted students',students)
grades = list(map(lambda x: sum(x)/len(x),grades))
print('Среднее значение оценок:',grades)
dict_students=dict(zip(students,grades))
print('Result',dict_students)