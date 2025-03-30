#Exercise level 1
#1
try:
    
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero.")

nombres = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']
nordic_countries, *resto = nombres[:5], nombres[5:]
print("Países nórdicos:", nordic_countries)
print("Resto de países:", resto)

paises = {
    'Finland': 'Helsinki',
    'Sweden': 'Stockholm',
    'Norway': 'Oslo'
}

for pais, capital in paises.items():
    print(f"La capital de {pais} es {capital}")

otros_paises = ['Estonia', 'Russia']
todos_paises = (*nordic_countries, *otros_paises)
print("Todos los países:", todos_paises)

def mostrar_paises(**pais):
    for nombre, capital in pais.items():
        print(f"La capital de {nombre} es {capital}")

mostrar_paises(**paises)

nordic_countries = nombres[:5]
es, ru = nombres[5:]

print("Países nórdicos:", nordic_countries)
print("Estonia:", es)
print("Rusia:", ru)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

nueva_lista = [*lista1, *lista2]
print("Lista combinada:", nueva_lista)

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

nuevo_dict = {**dict1, **dict2}
print("Diccionario combinado:", nuevo_dict)

paises = ['Finland', 'Sweden', 'Norway']

for index, pais in enumerate(paises):
    print(f"Índice {index}: {pais}")

capitales = ['Helsinki', 'Stockholm', 'Oslo']

for pais, capital in zip(paises, capitales):
    print(f"La capital de {pais} es {capital}")
