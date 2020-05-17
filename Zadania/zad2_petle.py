# 2▹ Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# # # # Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

#metoda ze slicem
# user_text=input("Podaj dowolny tekst \n")
# s=slice(1,20,2)
# print(user_text[s])

#metoda z petlą
user_text=input("Podaj dowolny tekst \n")
for i in user_text:
        print(user_text[1::2])
