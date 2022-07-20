import random
letter_count = int(input("How many letters you want in your password?: \n"))
number_count = int(input("How many numbers you want in your password?: \n"))
symbol_count = int(input("How many symbols you want in your password?: \n"))
letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z " \
          "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ".split(" ")
numbers = "1 2 3 4 5 6 7 8 9 0".split(" ")
symbols = "! @ # $ % ^ & *".split(" ")
len_letters = len(letters)
len_numbers = len(numbers)
len_symbols = len(symbols)
password_list = []
for i in range(0, letter_count):
    a = random.randrange(0, len_letters)
    password_list += letters[a]
for i in range(0, number_count):
    b = random.randrange(0, len_numbers)
    password_list += numbers[b]
for i in range(0, symbol_count):
    c = random.randrange(0,len_symbols)
    password_list += symbols[c]
random.shuffle(password_list)
length = len(password_list)
password = ""
for i in range(0, length):
    password += password_list[i]
print(f"Heres your new generated password: {password}")
