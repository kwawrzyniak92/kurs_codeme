# Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne. Wyświetl różne komunikaty w zależności od rodzaju błędu.


password = input("podaj hasło skladające się z minimum 1 dużej litery oraz cyfr\no dlugości mimumum 8 znaków\n ")
if password.isalpha():
    print("1")
else: print("hasło musi zawierać litery...")

if password.isdigit():
    print("2")
else: print("hasło musi zawierać liczbę...")

if password.isupper():
    print("3")
else: print("hasło musi zawierać 1 dużą litere...")

if len(password) >= 8:
    print("4")
else: print("Zbyt krótkie hasło...")

#pytania:
#
# jakiej metody użyć?
# w jaki sposób zbudować pętle żeby nie wyświetlać print 1 itd...