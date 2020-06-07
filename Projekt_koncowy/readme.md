#Generator konfiguracji usług
Skrypt generuje konfigurację usługi na podstawie bazy danych zawartej w pliku excell

##### 1.Instrukcja uruchomienia
  - uzupełnij dane w pliku `clients_db.xlsx`
 - uruchom plik skrypt.py
 - postępuj zgodnie z informacjami w skrypcie
 - po wykonaniu skryptu na ekranie wyświetli się gotowa konfiguracja do wklejenia na urządzenia sieciowe
 - konfiguracja zostanie również zapisana w folderze `Services` w katalogu programu
 
 ##### 2. Biblioteki użyte w programie
 - #####Jinja2
    biblioteka wykorzystana do stworzenia szablonu i wygenerowania gotowego pliku konfiguracji
    pełna dokumentacja rozszerzenia dostępna pod adrsem `https://palletsprojects.com/p/jinja/`
    
 - #####openpyxl
    biliboteka służy do wczytywania plików w formacie XLSX, w tym projekcie pozwala na bezpośrednie ściąganie danych z komórek pliku. 
    pełna dokumentacja rozszerzenia dostępna pod adresem `https://openpyxl.readthedocs.io/en/stable/tutorial.html`
##### 3. Planowane rozszerzenie funkcjonalności
Możliwe rozszerzenie funkcjonalności pliku to dodanie kolejnych typów urządzeń i generowanie dla nich konfiguracji, dodanie możliwości wprowadzania danych ręcznie a nie przez arkusz XLSX, zamiana arkusza na bazę liteSQL,
połączenie wygenerowanego szablonu z finkcjonalnościami Ansible (pełna automatyzacja konfiguracji).