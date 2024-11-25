#Task1
def mysplit(string):
    string = string.strip()
    if string == "":
        return []
    result = []
    word = ""
    for char in string:
        if char.isspace():
            if word:
                result.append(word)
                word = ""
        else:
            word += char
    if word:
        result.append(word)

    return result

print(mysplit(
    "To be or not to be, that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

#Task2
def display_digit(digit):
    segments = {
        '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
        '1': ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
        '2': [" *** ", "    *", " *** ", "*    ", "*****"],
        '3': [" *** ", "    *", " *** ", "    *", " *** "],
        '4': ["   * ", "  ** ", " * * ", "*****", "   * "],
        '5': ["*****", "*    ", " *** ", "    *", " *** "],
        '6': [" *** ", "*    ", "**** ", "*   *", " *** "],
        '7': ["*****", "    *", "   * ", "  *  ", "  *  "],
        '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
        '9': [" *** ", "*   *", " ****", "    *", " *** "],
    }
    return segments.get(digit,
                        ["     ", "     ", "     ", "     ", "     "])

def display_number(number):
    digits = str(number)
    rows = [""] * 5
    for digit in digits:
        digit_rows = display_digit(digit)
        for i in range(5):
            rows[i] += digit_rows[i] + "  "
    for row in rows:
        print(row)

num = input("Введіть цифри для відображення на семисегментному дисплеї: ")
display_number(num)

#Task3
def caesar_cipher(message, shift=1):
    encrypted_message = ""
    for char in message:
        if 'A' <= char <= 'Z' or char == ' ':
            new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encrypted_message += new_char
        else:
            raise ValueError("Повідомлення може містити лише великі латинські літери!")
    return encrypted_message

try:
    message = input("Введіть повідомлення для зашифрування(лише великі латинські літери): ").upper()
    encrypted = caesar_cipher(message)
    print("Зашифроване повідомлення:", encrypted)
except ValueError as e:
    print(e)

#Task4
def caesar_decipher(encrypted_message, shift=1):
    decrypted_message = ""
    for char in encrypted_message:
        if 'A' <= char <= 'Z' or char == ' ':
            new_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            decrypted_message += new_char
        else:
            raise ValueError("Повідомлення може містити лише великі латинські літери!")

    return decrypted_message

try:
    encrypted_message = input("Введіть повідомлення для розшифрування(лише великі латинські літери): ").upper()
    decrypted = caesar_decipher(encrypted_message)
    print("Розшифроване повідомлення:", decrypted)
except ValueError as e:
    print(e)
