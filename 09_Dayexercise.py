#Exercise level 1
#1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
edad = int(input("Ingresa tu edad: "))  

if edad >= 18:
    print("Tienes la edad suficiente para aprender a conducir.")
else:
    años_faltantes = 18 - edad
    print(f"Te faltan {años_faltantes} años para poder aprender a conducir.")

    #2 Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
mi_edad = int(input("Ingresa tu edad: "))
tu_edad = int(input("Ingresa la otra edad: "))  
if mi_edad > tu_edad:
    diferencia = mi_edad - tu_edad
    if diferencia == 1:
        print(f"Soy mayor que tú por {diferencia} año")  
    else:
        print(f"Soy mayor que tú por {diferencia} años")
elif tu_edad > mi_edad:
    diferencia = tu_edad - mi_edad
    if diferencia == 1:
        print(f"Eres mayor que yo por {diferencia} año")
    else:
        print(f"Eres mayor que yo por {diferencia} años")
else:
    print("Tenemos la misma edad")


#3 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
#1Write a code which gives grade to students according to theirs scores:
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

if a > b:
    print(f"{a} es mayor que {b}.")
elif a < b:
    print(f"{a} es menor que {b}.")
else:
    print(f"{a} es igual a {b}.")

#Exercise level 2 Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
def asignar_calificacion(puntaje):
    if 80 <= puntaje <= 100:
        return "A"
    elif 70 <= puntaje <= 89:
        return "B"
    elif 60 <= puntaje <= 69:
        return "C"
    elif 50 <= puntaje <= 59:
        return "D"
    elif 0 <= puntaje <= 49:
        return "F"
    else:
        return "Puntaje fuera de rango"
        
        
        
puntaje = float(input("Introduce el puntaje del estudiante: "))
calificacion = asignar_calificacion(puntaje)
print(f"La calificación del estudiante es: {calificacion}")

#2The following list contains some fruits:
def determinar_estacion(mes):
    mes = mes.lower()  
    if mes in ['septiembre', 'octubre', 'noviembre']:
        return "Otoño"
    elif mes in ['diciembre', 'enero', 'febrero']:
        return "Invierno"
    elif mes in ['marzo', 'abril', 'mayo']:
        return "Primavera"
    elif mes in ['junio', 'julio', 'agosto']:
        return "Verano"
    else:
        return "Mes no válido"


mes = input("Introduce el mes: ")
estacion = determinar_estacion(mes)
print(f"La estación correspondiente es: {estacion}")

#3The following list contains some fruits:
frutas = ['banana', 'naranja', 'mango', 'sandia']

def agregar_fruta(fruta):
    if fruta in frutas:
        print("Esa fruta ya existe en la lista")
    else:
        frutas.append(fruta)
        print("Lista modificada:", frutas)


fruta_a_agregar = input("Introduce la fruta que deseas agregar: ").lower()  
agregar_fruta(fruta_a_agregar)

#Exercise level 3
persona = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Tarea 1Here we have a person dictionary. Feel free to modify it!
if 'skills' in persona:
    lista_habilidades = persona['skills']
    habilidad_media = lista_habilidades[len(lista_habilidades) // 2]
    print(f"La habilidad del medio es: {habilidad_media}")

# Tarea 2
if 'skills' in persona and 'Python' in persona['skills']:
    print("La persona tiene la habilidad de Python.")

# Tarea 3
if 'skills' in persona:
    habilidades = persona['skills']
    if 'JavaScript' in habilidades and 'React' in habilidades and len(habilidades) == 2:
        print("Él es un desarrollador front end")
    elif 'Node' in habilidades and 'Python' in habilidades and 'MongoDB' in habilidades:
        print("Él es un desarrollador back end")
    elif 'React' in habilidades and 'Node' in habilidades and 'MongoDB' in habilidades:
        print("Él es un desarrollador fullstack")
    else:
        print("Título desconocido")

# Tarea 4
if persona['is_married'] and persona['country'] == 'Finland':
    print(f"{persona['first_name']} {persona['last_name']} está casado y vive en Finlandia.")
    