# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, ras=","):
    people1 = set(str1.split(ras))
    people2 = str2.split(ras)
    new_group = people1.intersection(people2)
    list_new_g = []
    for i in new_group:
        list_new_g.append(i)
    list_new_g.sort()
    return(list_new_g)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group, participants_second_group, '|')