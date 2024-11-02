#Task1
lessernumbers = [10, 3, 15, 7, 20, 5, 8]
numbers_tuple = tuple(lessernumbers)
n = int(input("Введіть число n для першого завдання: "))
lesserresult = [num for num in numbers_tuple if num < n]
print("Числа менші за", n, ":", lesserresult)

#Task2
tuple_of_strings = ("Бог", "Мудрість", "Спасіння")
stringsresult = ",".join(tuple_of_strings)
print(stringsresult)

#Task3
library = {
    "1984": {
        "Автор": "Джордж Оруелл",
        "Рік": 1949,
        "Кількість сторінок": 328
    },
    "Так казав Заратустра": {
        "Автор": "Фрідріх Ніцше",
        "Рік": 1885,
        "Кількість сторінок": 320
    },
    "Берсерк": {
        "Автор": "Кентаро Міура",
        "Рік": 1989,
        "Кількість сторінок": 392
    }
}
book_name = input("Введіть назву книги: ")
if book_name in library:
    book_info = library[book_name]
    print(f"Інформація про книгу '{book_name}':")
    print(f"Автор: {book_info['Автор']}")
    print(f"Рік видання: {book_info['Рік']}")
    print(f"Кількість сторінок: {book_info['Кількість сторінок']}")
else:
    print("Такої книги немає в бібліотеці.")

#Task4
students = {
    "Гарагуля": ("Денис", 20, "ІЕЛІІТ"),
    "Богомаз": ("Артур", 18, "ФПГІСН"),
    "Дубовик": ("Ольга", 20, "ФЕУ")
}
surname = input("Введіть прізвище студента: ")
if surname in students:
    name, age, faculty = students[surname]
    print(f"Інформація про студента '{surname}':")
    print(f"Ім'я: {name}")
    print(f"Вік: {age}")
    print(f"Факультет: {faculty}")
else:
    print("Студента з таким прізвищем немає в базі.")

#Task5
phone_book = {
    "Олександр": ["+380501234567", "+380671234567"],
    "Марія": ["+380631234567"],
    "Іван": ["+380931234567", "+380991234567"]
}
def add_phone_number(contact_name, phone_number):
    if contact_name in phone_book:
        phone_book[contact_name].append(phone_number)
    else:
        phone_book[contact_name] = [phone_number]
    print(f"Додано номер {phone_number} до контакту '{contact_name}'.")
contact_name = input("Введіть ім'я контакту: ")
phone_number = input("Введіть номер телефону для додавання: ")
add_phone_number(contact_name, phone_number)
print("\nТелефонна книга:")
for contact, numbers in phone_book.items():
    print(f"{contact}: {', '.join(numbers)}")
