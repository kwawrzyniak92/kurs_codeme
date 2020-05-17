import csv
#wczytanie pliku z listą linków od użytkownika
user_link = []
print("##################################################")
print(" ###### SKRYPT GENERUJE LINKI AFILIACYJNE ######\n ########### DLA GRUPY HELION.PL ###############")
print("##################################################")
print("przed uruchomieniem skryptu dodaj linki do pliku linki.csv!")

with open('linki.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=" ") # zamiana znaku końca linii z "," na |
#pętla która "zapisuje" linki do listy
    for row in reader:
        link = row[0]
        user_link.append(link)
#print(user_link)
print("krok [1/3] - wczytywanie linków z pliku linki.csv\n\n")
client_number = input("PODAJ SWÓJ NUMER KLIENTA \n")
# zamiana linku na nowy
new_link = []
for i in user_link:
    if i.startswith("https://helion.pl/"):
        new_elem = i.replace("https://helion.pl/",f"https://helion.pl/view/{client_number}/")
    elif i.startswith("https://videopoint.pl/"):
        new_elem = i.replace("https://videopoint.pl/", f"https://videopoint.pl/view/{client_number}/")
    elif i.startswith("https://ebookpoint.pl/"):
        new_elem = i.replace("https://ebookpoint.pl/",f"https://ebookpoint.pl/view/{client_number}/")
    #print(new_elem)
    else:
        print("link do złego serwisu. Sprawdź plik linki.csv...")
# zapis reflinka do nowej tablicy
    new_link.append(new_elem)
#print(new_link)
print ("krok [2/3] - konwersja linków")
#zapis list do pliku CSV
with open("reflink.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(zip(user_link, new_link))
print (f"krok [3/3] - linki afiliacyjne dla użytkownika o numerze {client_number} wygenerowane w pliku reflink.csv")