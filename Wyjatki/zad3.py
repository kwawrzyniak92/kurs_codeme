
 # Stwórz listę 10 elementową (różne typy!).
 # Pozwól użytkownikowi podać dowolny index. Podziel 1 przez liczbę pod indexem wybranym przez użytkownika. Obsłuż błędy.

import sys
elem_list = [10, "cos", "15", 0, ["1","2"], {3,2,1},"zero","1"]
try:
    user_number = int(input("podaj liczbe: "))
    dzielenie = elem_list[1 / user_number]
except (TypeError, ValueError) as message:
    print('Exception message:', message)
except Exception:
     print(sys.exc_info()[0].__name__)
else:
    print("Wynik to ", dzielenie)
