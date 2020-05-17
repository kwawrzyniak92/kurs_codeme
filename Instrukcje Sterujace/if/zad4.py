# Utwórz zmienną przechowującą dowolny ciąg znaków.
# Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.


your_string = "abrakadabra"
if len(your_string) > 5 and "a" in your_string:
    print(your_string)
    new_string = your_string.replace("a", "z")
    print(new_string)
else: print("Podany ciąg wyrazów jest nieprawidłowy ")
