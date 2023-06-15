#Se desea calcular la distancia recorrida (m) por un móvil que tiene velocidad 
#constante (m/s) durante un tiempo t (s), considerar que es un MRU (Movimiento
#Rectilíneo Uniforme). Fórmula de distancia: d = v . t

#Input
velocidad=float(input("Ingrese la velocidad en metros: "))
tiempo=float(input("Ingrese el tiempo en segundos: "))

#Proceso
distancia=velocidad*tiempo

#Output
print("La distancia recorrida es: ", distancia)
