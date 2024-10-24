from calendar import month

#Task1
print("Перше завдання:\n")
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
test_years = [1900, 2000, 2004, 2100, 2400, 2024, 1800]
expected_results = [False, True, True, False, True, True, False]
all_correct = True
for i in range(len(test_years)):
    result = is_leap_year(test_years[i])
    if result != expected_results[i]:
        print(f"Помилка! Рік {test_years[i]} повернув {result}, а очікувалося {expected_results[i]}")
        all_correct = False
if all_correct:
    print("Усі результати правильні")
else:
    print("Є неправильні результати неправильні")

#Task2
print("Друге завдання:\n")
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        return 29
    else:
        return month_days[month - 1]
print(days_in_month(2024, 2))
print(days_in_month(2023, 2))
print(days_in_month(2023, 11))

#Task3
print("Третє завдання:\n")
def day_of_year(year, month, day):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        month_days[1] = 29
    if month < 1 or month > 12:
        return None
    if day < 1 or day > month_days[month - 1]:
        return None
    return sum(month_days[:month - 1]) + day
print(day_of_year(2024, 3, 1))
print(day_of_year(2023, 12, 31))
print(day_of_year(2024, 2, 29))
print(day_of_year(2023, 2, 29))
print(day_of_year(2023, 13, 5))

#Task4
print("Четверте завдання:\n")
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

#Task5
print("П'яте завдання:\n")
def liters_100km_to_miles_gallon(liters):
    miles_per_galon = 235.21 / liters
    return miles_per_galon
def miles_gallon_to_liters_100km(miles):
    liters_per_100km = 235.21 / miles
    return liters_per_100km
lpk_value = 8.5
mpg = liters_100km_to_miles_gallon(lpk_value)
print(f"{lpk_value} л/100 км дорівнює {mpg:.2f} MPG")
mpg_value = 30
lpk_value = miles_gallon_to_liters_100km(mpg_value)
print(f"{mpg_value} MPG дорівнює {lpk_value:.2f} л/100 км")

#Task6
print("Шосте завдання:\n")
def is_a_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a
print(is_a_triangle(3, 4, 5))
print(is_a_triangle(1, 10, 12))

#Task7
print("Сьоме завдання:\n")
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    a, b, c = sorted([a, b, c])
    return a**2 + b**2 == c**2
print(is_a_right_triangle(3, 4, 5))
print(is_a_right_triangle(5, 12, 13))
print(is_a_right_triangle(1, 2, 3))