# 1▹ Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
# # (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
# # Następnie powitaj każdą osobę na liście.


names=input("podaj imiona odzielone spacją ")
sort_names= names.split(" ")
for i in (sort_names):
    print("Witaj" ,i)
