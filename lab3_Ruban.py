#Task1
import math
def gaussian(x, mu, sigma):
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sigma) ** 2)
x = 1.0
mu = 0.0
sigma = 1.0
result = gaussian(x, mu, sigma)
print(f"Результат функції Гауса: {result}")

#Task2
john = 3
mary = 5
adam = 6
totalapple = john + mary + adam
print(john,",",mary,",",adam)
print("Загальна кількість яблук =",totalapple)

#Task3
kilometers = 12.25
miles = 7.38
miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers*0.62
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#Task4
x1 = input("Введіть свій x для четвертого завдання: ")
x1 = float(x1)
y = 3*math.cbrt(x1)-2*math.sqrt(x1)+math.pow(3, x1)-1
print("y =", y)

#Task5
a = 2 #Number of hours
seconds = 3600 #Number of seconds in 1 hour
print("Hours: ", a) #Printing the number of hours

#Task6
a=float(input("Введіть змінну a для шостого завдання: "))
b=float(input("Введіть змінну b для шостого завдання: "))
print("a + b = ", a+b)
print("a i b = ", a-b)
print("a * b = ", a*b)
print("a / b = ", a/b)
print("Is that all? Not even close")

#Task7
def fractal_division(x, depth):
    if depth == 0:
        return x
    else:
        return x + 1 / fractal_division(x, depth - 1)
x2 = float(input("Введіть свій x для сьомого завдання: "))
depth = int(input("Введіть кількість ітерацій для сьомого завдання: ")) #Yep, I modified this so U can choose the number of iterations of that.. interesting sequence
y = 1 / fractal_division(x2, depth)
print(f"y = {y}")

#Task8
hours = int(input("Введіть години для восьмого завдання (від 0 до 23): "))
minutes = int(input("Введіть хвилини для восьмого завдання (від 0 до 59): "))
add_minutes = int(input("Введіть довжину події у хвилинах для восьмого завдання: "))
total_minutes = minutes + add_minutes
new_hours = (hours + total_minutes // 60) % 24
new_minutes = total_minutes % 60
print(f"Итоговое время: {new_hours:02d}:{new_minutes:02d}")
