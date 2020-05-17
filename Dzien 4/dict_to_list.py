list_to_dict= [
    ["dzien dobry", "bonjour"],
    ["ziemniaki", "pomme de terre"],
    ["dziekuje", "merci"],
    ]

slownik_fr = dict(list_to_dict)

print(slownik_fr)
print(slownik_fr['dziekuje'])

for k, v in slownik_fr.items():
    print(f"{k} - tlumaczenie: {v}")