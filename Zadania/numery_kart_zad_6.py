def is_card_number(number):
    return number.isdecimal() and len(number) in (13,15,16)

def starts_with_correct_digits(number):
    if 51 <= int(number[0:2]) <=55:
        return True
    elif 2221 <= int(number[0:4]) <= 2720:
        return True
    else:
        return False

def show_card_type(number):
    if len(number) in [13,16] and number[0] == "4":
        print("To jest Visa")

    elif len(number) == 16 and starts_with_correct_digits(number):
        print ("To jest Mastercard")

    elif len(number) == 15 and (number[0:2]in ['34', 37]):
        print("To nie jest America Express")
    else: return False`