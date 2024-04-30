distancia= 0
tiempo=0
velocidad=0
def velocidad_mru(distancia, tiempo):
    return distancia/tiempo

def distancia_mru(velocidad, tiempo):
    return velocidad*tiempo

def tiempo_mru(distancia, velocidad):
    return distancia/velocidad

def area_mate(base, altura):
    return base*altura

def volumen_mate(longitud, ancho, altura):
    return longitud*ancho*altura

def perimetro_mate(lado1, lado2, lado3, lado4):
    return lado1+lado2+lado3+lado4

def gramos_moles(masa, masamolar):
    return masa/masamolar

def concentración_molar(molesoluto, volumensolución):
    return molesoluto/volumensolución

print("Bienvenido al conversor")
print("1. Velocidad, 2. Distancia, 3. Tiempo, 4. Area, 5. Volumen, 6. Perimetro, 7. Gramos a Moles")

opcion=input("¿Qué tipo de conversión quiere realizar?")

if opcion == "1":
    velocidad=float(input("Ingrese velocidad"))
    tiempo=float(input("Ingrese tiempo"))
    print('Tu velocidad MRU es: {0}m/s'.format(velocidad_mru(distancia,tiempo)))

elif opcion == "2":
    velocidad=float(input("Ingrese velocidad"))
    tiempo=float(input("Ingrese tiempo"))
    print('Tu distancia MRU es: {0}metros'.format(distancia_mru(velocidad,tiempo)))

elif opcion == "3":
    distancia=float(input("Ingrese distancia"))
    velocidad=float(input("Ingrese velocidad"))
    print('Tu tiempo MRU es: {0}segundos'.format(tiempo_mru(distancia,velocidad)))

elif opcion == "4":
    base=float(input("Ingrese base"))
    altura=float(input("Ingrese altura"))
    print('Tu altura es: {0}metros'.format(area_mate(base,altura)))

elif opcion == "5":
    longitud=float(input("Ingrese longitud"))
    ancho=float(input("Ingrese ancho"))
    altura=float(input("Ingrese altura"))
    print('Tu volumen es: {0}mts cubicos'.format(volumen_mate(longitud,ancho,altura)))

elif opcion == "6":
    lado1=float(input("Ingrese lado"))
    lado2=float(input("Ingrese segundo lado"))
    lado3=float(input("Ingrese tercer lado"))
    lado4=float(input("Ingrese cuarto lado")) 
    print('Tu perimetro es: {0}mts cuadrados'.format(perimetro_mate(lado1,lado2,lado3,lado4)))

elif opcion == "7":
    masa=float(input("Ingrese masa"))
    masamolar=float(input("Ingrese masa Molar"))
    print('Tus Moles son: {0}n'.format(gramos_moles(masa,masamolar)))

elif opcion == "8":
    masa=float(input("Ingrese masa"))
    masamolar=float(input("Ingrese masa Molar"))
    print('Tus Moles son: {0}n'.format(gramos_moles(masa,masamolar)))




