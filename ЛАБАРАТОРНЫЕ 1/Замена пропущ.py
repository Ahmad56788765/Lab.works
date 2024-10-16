numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

len__nubers = len(numbers)
numbers[4] = 0
sum__numbers = sum(numbers)
sred_arifm = sum__numbers/len__nubers
numbers[4] = sred_arifm
print("Измененный список:", numbers)
