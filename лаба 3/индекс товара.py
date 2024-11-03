# TODO Напишите функцию для поиска индекса товара
def find1(list_, x):
    t = False
    list1_ = []
    for i in list_:
        if i != x:
            list1_.append(i)
        else:
            t = True
            break
    index = len(list1_)
    if t is True:
        return index






items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find1(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
