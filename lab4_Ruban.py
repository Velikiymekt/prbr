#Task1
n = int(input("Введіть число для першого завдання: "))
print(n >= 100)

#Task2
a = float(input("Введіть перше число для другого завдання: "))
b = float(input("Введіть друге число для другого завдання: "))
if a > b:
    print(a, "більше")
else:
    print(b, "більше")

#Task3
plant = input("Go on, gimme that plant name: ")
if plant == "Spathiphyllum":
    print("HOOOLYY YEEEAAAHHH")
elif plant == "spathiphyllum":
    print("Still good, BUT I NEED BIGGER")
else:
    print ("R U kidding? I SAID TYPE THE Spathiphyllum NOT THE", plant)

#Task4
income = float(input("Отже, зізнавайся, скільки грошей ти заробив, веселий молочник??? "))
if income < 85528:
    tax = (income/100*18) - 556.2
else:
    tax = (income/100*32) + 14839.2
if tax > 0:
    print("Отже в скарбницю з тебе ", round(tax, 2))
else:
    print("Здається... брати з тебе нічого")

#Task5
year = int(input("Введіть рік для перевірки: "))
if year < 1582:
    print("Цей рік взагалі з Юліанського календаря")
elif year % 4 == 0:
    print("Це високосний рік")
else:
    print("Це звичайний рік")

#Task6
secretnumber = 17
print(
"""
+======================================+
| Welcome to WHITE SPACE!              |
| You`ve been living here              |
| for as long, as You can remember.    |
| To escape You just need to guess     |
| the correct SECRET NUMBER            |
| So what`s Your answer?               |
+======================================+
""")
while True:
    guess = int(input())
    if guess == secretnumber:
        print(
            "You managed to escape WHITE SPACE! Your reward is 50 CLAMS"
        )
        break
    else:
        print("WRONG! Try again^^")

#Task7
import time
for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)
    if i == 5:
        print("Ready or not, here I come!")

#Task8
secretword = "chupacabra"
while True:
    word = input("Soo... here we go again. Type the word and let`see can You guess: ")
    if word == secretword:
        print(
            "You`ve managed to quit my beautiful endless loop of word guessing. Okay FINE! I`ll let You go..."
        )
        break

#Task9
userword = input("Type your word for VOWEL EATER to eat vowels: ")
userword = userword.upper()
print("So now You`re left with this: ")
for letter in userword:
    if letter in ('A', 'E', 'I', 'O', 'U'):
        continue
    print(letter)

#Task10
userword = input("Type your word again for VOWEL EATER II to eat vowels: ")
userword = userword.upper()
wordwithoutvowels = ""
for letter in userword:
    if letter in ('A', 'E', 'I', 'O', 'U'):
        continue
    wordwithoutvowels += letter
print("So now You`re left with this: ", wordwithoutvowels)

#Task11
blocks = int(input("Введіть кількість блоків піраМММіди: "))
height = 0
currentlevelblocks = 1
while blocks >= currentlevelblocks:
    blocks -= currentlevelblocks
    height += 1
    currentlevelblocks += 1
print(f"Кількість поверхів: {height}")

#Task12
count = 0
col = int(input("Введіть своє число для алгоритму Коллатца: "))
while col != 1:
    if col % 2 == 0:
        col = col // 2
    else:
        col = col * 3 + 1
    print(col)
    count = count + 1
print(count, "Кроків")