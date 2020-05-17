print("OPINIE O KSIAZCE GOT")
opinia1=float(input("Jakie wrażenia w skali 1-10 masz po przeczytaniu ksiażki GOT "))
opinia2=float(input("W skali od 1-10 jak podobała się Tobie kreacja głównych bochaterów "))
opinia3=float(input("Jak bardzo polecił być tę książke znajomemu? (1 - wcale 10 - napewno) "))
srednia=float((opinia1 + opinia2 + opinia3)/3)
print("srednia = " + str(srednia))
if srednia > 7:
    print("bardzo dobry")
elif srednia <= 4:
    print("nie warta uwagi")
elif srednia <=7:
    print("przecietna")

