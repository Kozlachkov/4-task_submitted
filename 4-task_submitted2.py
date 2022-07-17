#Задача 2
#Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, 
# вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
with open("4-task_submitted2.txt", "r", encoding='utf-8') as file:    
    full_file = file.read()
    list_of_rows = full_file.split("\n")
people={}
qty_people=len(list_of_rows)
for i in range(len(list_of_rows)):
    s=list_of_rows[i].split() 
    people[s[0]]=float(s[1])
sum=0    
print("сотрудники, у котрых ЗП < 20 т.р.: ")  
for person in people.items():
    sum+=float(person[1])
    if person[1]<20000: 
       print(person[0])
print("средняя ЗП по больнице: ", sum/qty_people)    