#sprawdzenie czy to jest karta
#sprawdzenie czy to jest prawidlowy numer karty (ilość cyfr 13, 16 lub 15)

def card_check(number):
    return number.isdecimal() and len(number) in [13, 15, 16]

card_number = input('Podaj numer karty ')
#sprawdzenie czy wiza - poczatek od 4
if len(card_number) in [13, 16] and card_number[0] == '4'
    print("To jest Visa ")





#sprawdzenie czy mastercard - poczatek 51 - 55 lub 2221 do 2720

#sprawdzenie czy American express - poczatek 34 lub 37 i 15 znaków