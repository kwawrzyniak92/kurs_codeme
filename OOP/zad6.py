# Utwórz klasę Pracownik.
#
# Pracownik ma stanowisko, wynagrodzenie, imie, nazwisko, staz pracy.
#
# Pracownik powinen miec roczne podwyżki wg. dowolnie wymyślonego sposobu liczenia.
# Pracownik powinen odprowadzać podatek o wysokoci zależnej od swoich zarobków oraz minimalną składkę zdrowotną.
#
# Pracownik powinien mieć pole typu boolowskiego zawierające status studenta.
# Jeśli pracownik jest studentem jego składka zdrowotna wynosi 0%.
#
# Wszyscy pracownicy mają wspólną nazwę firmy. Spółgłoski imienia i nazwiska wraz z nazwą firmy .com tworzą adres mailowy. Np.
#
# Adam Kowalski Love Python Company
#
# email -> smkwlsk@lovepythoncompany.com

class Employe:
    company = "THE CODE INC"
    def __init__(self, job, salary, name, second_name, experience  ):
        self.name = name
        self.second_name = second_name
        self.job = job
        self.salary = salary
        self.experience = experience

    

p1 = employe("Jan", "Kowalski", "QA",4500, 1.5)