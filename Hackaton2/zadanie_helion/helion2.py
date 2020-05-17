def menu():
    choice = int(input("Podaj jakiego typu jest podany link\n 1 - strona główna \n 2 - strona produktu \n 3 - strona promocji \n 4 - koszyk \5 link do kategorii\n\n"))
    if choice == 1:
        ref_link = page_link
        print(ref_link)
    elif choice == 2:
        ref_link = user_link.replace("https://helion.pl/", page_link)
        print(ref_link)
    else:
        print("koniec")


client_number = int(input("Podaj numer klienta\n"))
user_link = input("podaj link do produktu\n")
page_link = f"https://helion.pl/view/{client_number}/"
ref_link = []
menu()