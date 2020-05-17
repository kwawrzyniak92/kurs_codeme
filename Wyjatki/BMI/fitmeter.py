import bmi

def fix_units(user_input, unit):
    if unit in user_input:
        container = ''
        for char in user_input:
            if char.isnumeric() or char == '.':
                container += char
        return float(container)
    else:
        return -1

weight = input("Podaj wage [kg]:")
try:
    float(weight)
except ValueError:
    print('value error')
    w = fix_units(weight, 'kg')

    if w == -1:
        print('Wartosc nieprawidlowa')
else:
    w = float(weight)

print(w)

height = input("Podaj wzrost [m]:")

try:
    float(height)
except  ValueError as e:
    print(e)
    h = fix_units(height, 'm')

    if h == -1:
        print ('Wartość nieprawidłowa')

    # if 'kg' in weight:
    #     tmp_weight = ""
    #     for char in weight:
    #         if char.isnumeric() or char == '.':
    #             tmp_weight = tmp_weight + char
    #         w = float(tmp_weight)
    #     else:
    #         print('Wartość jest nieprawidłowa')
else:
    h = float(height)




result_bmi = bmi.calculate_bmi(w, h)
state = bmi.get_state(result_bmi)
print(state)

filename = state.lower() + '.txt'
with open(filename) as fopen:
    tip = fopen.read()

print(tip)