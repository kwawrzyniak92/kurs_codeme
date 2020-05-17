ciag = input("podaj jakieś zdanie ")
mala_litera = 0
duza_litera = 0
cyfra = 0
inne = 0

for l in ciag:
    if l.islower():
        mala_litera += 1
    if l.isupper():
        duza_litera += 1
    if l.isdecimal():
        cyfra += 1
    if not l.isalnum():
        inne += 1
    print(f"Malych - {mala_litera},",
          f"Duzych - {duza_litera},",
          f"Cyfry - {cyfra},",
          f"Symbole - {inne},",)
