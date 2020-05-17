fahr = 0
while fahr <= 200:
    celc = 5/9 * (fahr -32)
    celc = round(celc, 2)
    print( f"Temp {fahr} F to {celc} stC" )
    fahr += 20
