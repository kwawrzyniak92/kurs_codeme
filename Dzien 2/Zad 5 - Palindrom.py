palindrom = "Kobyla ma maly bok"
palindrom = palindrom.replace(" ", "") #usuniecie spacji z tekstu
palindrom = palindrom.lower()
print(palindrom)
print(palindrom == palindrom [::-1])

