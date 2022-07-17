#Задача 1 
# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.
with open("4-task_submitted.txt", "r", encoding='utf-8') as file:    
    full_file = file.read()
    list_of_elements = full_file.split()
list_of_elements = list(map(int, list_of_elements))   
list_of_elements.sort()
i=0
while i+1!=list_of_elements[-1]:
    if list_of_elements[i]+1!=list_of_elements[i+1]:
        list_of_elements.insert(i+1,list_of_elements[i]+1)
    i+=1
print(list_of_elements) 
