#Exercise level 1 
#1
def sumar_dos_numeros(a, b):
    return a + b

print(sumar_dos_numeros(3, 5)) 

#2
import math

def area_de_circulo(r):
    return math.pi * r * r

print(area_de_circulo(5))  

#3
def sumar_todos_los_numeros(*args):
    if all(isinstance(arg, (int, float)) for arg in args):
        return sum(args)
    else:
        return "Error: Todos los elementos deben ser números."

print(sumar_todos_los_numeros(1, 2, 3)) 
print(sumar_todos_los_numeros(1, "dos", 3))  

#4
def convertir_celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print(convertir_celsius_a_fahrenheit(25)) 


#5
def verificar_estacion(mes):
    estaciones = {
        "Diciembre": "Invierno", "Enero": "Invierno", "Febrero": "Invierno",
        "Marzo": "Primavera", "Abril": "Primavera", "Mayo": "Primavera",
        "Junio": "Verano", "Julio": "Verano", "Agosto": "Verano",
        "Septiembre": "Otoño", "Octubre": "Otoño", "Noviembre": "Otoño"
    }
    return estaciones.get(mes, "Mes no válido")

print(verificar_estacion("Marzo"))  

#6
def calcular_pendiente(m, x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "La pendiente es indefinida (línea vertical)."
    return (y2 - y1) / (x2 - x1)
print(calcular_pendiente(2, 1, 2, 3, 4)) 


#7
import math

def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return (raiz1, raiz2)
    elif discriminante == 0:
        raiz = -b / (2 * a)
        return (raiz,)
    else:
        return "No hay raíces reales"

print(resolver_ecuacion_cuadratica(1, -3, 2))  

#8
def imprimir_lista(lst):
    for item in lst:
        print(item)

imprimir_lista([1, 2, 3])
#9
def invertir_lista(lst):
    lista_invertida = []
    for i in range(len(lst)-1, -1, -1):
        lista_invertida.append(lst[i])
    return lista_invertida

print(invertir_lista([1, 2, 3, 4, 5]))  

#10
def capitalizar_items_lista(lst):
    return [item.capitalize() for item in lst]

print(capitalizar_items_lista(["manzana", "banana", "cereza"]))  
#11
def agregar_item(lst, item):
    lst.append(item)
    return lst
alimentos = ['Papas', 'Tomates', 'Mangos', 'Leche']
print(agregar_item(alimentos, 'Carne'))  
#12
def eliminar_item(lst, item):
    if item in lst:
        lst.remove(item)
    else:
        return "El ítem no se encuentra en la lista."
    return lst
alimentos = ['Papas', 'Tomates', 'Mangos', 'Leche']
print(eliminar_item(alimentos, 'Mangos'))  
#13
def suma_de_numeros(n):
    return sum(range(1, n + 1))
print(suma_de_numeros(5)) 

#14
def suma_de_impares(n):
    return sum(i for i in range(1, n + 1) if i % 2 != 0)
print(suma_de_impares(5))
#15 
def suma_de_pares(n):
    return sum(i for i in range(1, n + 1) if i % 2 == 0)
print(suma_de_pares(5))
