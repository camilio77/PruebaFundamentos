#codigo que permite calcular el area de un triangulo equilatero y la muestra siempre y cuando el area sea menor a 1000
base = float(input("ingrese la base del tiangulo\n"))
altura = float(input("ingrese la altura del tiangulo\n"))
area = (base * altura) / 2
if(area > 1000):
    print("Datos no validos")
else:
    print(f"el area del triangulo es {area}")