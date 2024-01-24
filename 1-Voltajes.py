#codigo que me permita ingresar 5 voltajes y a partir de su promedio determinar si es un voltaje alto o correcto
v1 = int(input("ingrese el primer voltaje\n"))
v2 = int(input("ingrese el segundo voltaje\n"))
v3 = int(input("ingrese el tercer voltaje\n"))
v4 = int(input("ingrese el cuarto voltaje\n"))
v5 = int(input("ingrese el quinto voltaje\n"))
prom = (v1 + v2 + v3 + v4 + v5)/5
if(prom > 220):
    print("ALTO VOLTAJE")
else:
    print("VOLTAJE CORRECTO")