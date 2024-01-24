#codigo que solicita 3 voltajes distintos, saca su promedio y los cataloga entre voltaje correcto, alto voltaje y peligro
i = 2
j = 1
while(i > j):
    v1 = int(input("ingrese el primer voltaje\n"))
    v2 = int(input("ingrese el segundo voltaje\n"))
    v3 = int(input("ingrese el tercer voltaje\n"))
    if(v1 == v2 or v2 == v3 or v1 == v3):
        print("\ningrese voltajes distintos\n")
    else:
        j = 3

prom = (v1 + v2 + v3) / 3
if(prom < 115):
    print("Voltaje correcto")
elif(prom >= 115 and prom < 220):
    print("Alto voltaje")
else:
    print("PELIGRO")