import random

def show_quote(text):
    id = random.randrange(0, 20)
    print('*' * 90)
    print(quotes[id].center(90))
    print('*' * 90)

with open ('cytaty.txt', 'r') as fopen:
    quotes = fopen.readlines()

show_quote(quotes)

