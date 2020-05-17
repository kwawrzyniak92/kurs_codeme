# funkcja obliczająca BMI <- waga, wzrost
def calculate_bmi(weight, height):
    return weight /height ** 2

# funkcja podająca wartość
def get_state(bmi):
    if bmi < 18:
        return "Niedowaga"

    elif bmi < 25:
        return "Norma"
    elif bmi < 30:
        return "Nadwaga"
    else:
        return "Otylosc"