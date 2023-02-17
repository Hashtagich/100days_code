# Задание №1
number = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
square_number = [i ** 2 for i in number]
print(square_number)
# Задание №2
square_number_2 = [i for i in number if i ** 2 % 2 == 0]
print(square_number_2)

# Задание №3
text_1 = [1, 2, 3, 4, '5', '6', '7', 8, 9, 10, 11, 12, 13, 3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]
text_2 = ['1', '2', 3, '4', 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 3, 6, 13, 5, 7, 89, 12, 3, 33, 34, '1', 344, 42]
result = [i for i in text_1 if i in text_2]
print(result)
