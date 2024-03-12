import string
import random

lenght_ = int(input('Type the number of characters you want in your password: '))

special_characters = ['!', '@', '#', '$', '%', '&', '*']
numbers_ = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)
count = 0


while count < lenght_:
    count += 1
    list_all = special_characters * 2 + numbers_ + alphabet_upper + alphabet_lower
    print(random.choice(list_all), end='')
