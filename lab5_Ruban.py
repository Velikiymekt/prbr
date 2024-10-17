#Task1
hat_list = [1, 2, 3, 4, 5]
user_number = int(input("Введіть ціле число для заміни середнього елемента списку в першому завданні: "))
hat_list[2] = user_number
hat_list.pop()
print("Довжина списку:", len(hat_list))

#Task2
user_list = input("Введіть список чисел, розділених пробілами для другого завдання: ")
numbers = [int(x) for x in user_list.split()]
n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print("Відсортований методом бульбашкою список:", numbers)

#Task3
raw_list = input("Введіть список чисел з повторами для третього завдання(розділяються пробілами): ")
numbers = [int(x) for x in raw_list.split()]
unique_numbers = list(set(numbers))
print("Список без дублікатів:", unique_numbers)

#Task4
chessboard = [["_"] * 8 for _ in range(8)]
chessboard[0][0] = "R"
chessboard[0][7] = "R"
chessboard[7][0] = "R"
chessboard[7][7] = "R"
for row in chessboard:
    print(" ".join(row))