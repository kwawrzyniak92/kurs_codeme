# Utwórz zmienną przechowującą dowolny ciąg znaków.
# Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

my_string="abrakadabra"
if len(my_string)>5 and my_string.count("a") > 0:
   my_string=my_string.replace("a","z")
   print(my_string)
else: print("napis jest za krótki lub nie zawiera litery a...")