#Task1
def is_palindrome(text):
    filtered_text = ''.join(char.lower() for char in text if char.isalnum())
    return filtered_text == filtered_text[::-1]

text = input("Введіть слово або фразу для перевірки на паліндромність: ")
if is_palindrome(text):
    print("Так, це паліндром!")
else:
    print("Ні, це не паліндром.")

#Task2
def are_anagrams(text1, text2):
    filtered_text1 = ''.join(char.lower() for char in text1 if char.isalnum())
    filtered_text2 = ''.join(char.lower() for char in text2 if char.isalnum())
    return sorted(filtered_text1) == sorted(filtered_text2)

text1 = input("Введіть перше слово або фразу для перевірки на анаграмність: ")
text2 = input("Введіть друге слово або фразу для перевірки на анаграмність: ")

if are_anagrams(text1, text2):
    print("Введені тексти є анаграмами!")
else:
    print("Введені тексти не є анаграмами.")

#Task3
def calculate_life_number(birth_date):
    life_number = sum(int(digit) for digit in birth_date if digit.isdigit())
    while life_number > 9:
        life_number = sum(int(digit) for digit in str(life_number))
    return life_number

birth_date = input("Введіть свою дату народження у форматі РРРРММДД або ММДДРРРР або ДДММРРРР тощо: ")
life_number = calculate_life_number(birth_date)
print("Ваша цифра життя:", life_number)

#Task4
def are_characters_hidden(first, second):
    index = 0
    for char in first:
        index = second.find(char, index)
        if index == -1:
            return "Ні, тут немає ваших заданих символів"
        index += 1
    return "Так, символи знайдено"

first_string = input("Введіть перший рядок: ").strip()
second_string = input("Введіть другий рядок: ").strip()
result = are_characters_hidden(first_string, second_string)
print(result)

#Task5
def calculate_life_number(date_str):
    while len(date_str) > 1:
        date_str = str(sum(int(char) for char in date_str))
    return int(date_str)

try:
    birth_date = input("Введіть свою дату народження у форматі РРРРММДД або ММДДРРРР або ДДММРРРР тощо, але на цей раз з помилкою: ").strip()
    if not birth_date.isdigit():
        raise ValueError("Дата народження має містити тільки цифри.")
    life_number = calculate_life_number(birth_date)
    print(f"Ваша цифра життя: {life_number}")
except ValueError as e:
    print("Введені дані не є коректними для обчислення.")

#Task6
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: wrong input")

def get_input_in_range():
    lower_limit = get_int("Введіть нижню межу: ")
    upper_limit = get_int("Введіть верхню межу: ")
    if lower_limit >= upper_limit:
        print("Помилка: нижня межа має бути меншою або дорівнювати верхній.")
        return get_input_in_range()
    while True:
        try:
            value = int(input(f"Введіть ціле число між {lower_limit} та {upper_limit}: "))
            if lower_limit <= value <= upper_limit:
                return value
            else:
                print(f"Помилка: введене число виходить за межі ({lower_limit}..{upper_limit})")
        except ValueError:
            print("Помилка введення")

result = get_input_in_range()
print(f"Дякуємо, що ввели коректне число: {result}")
