#Exercises Level 1
#1 Writ a function which generates a six digit/character random_user_id
import random
import string

def random_user_id():
    caracteres = string.ascii_letters + string.digits 
    return ''.join(random.choice(caracteres) for _ in range(6))


print(random_user_id())  

#2 Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
import random
import string

def user_id_gen_by_user():
    # Pedir al usuario el número de caracteres y el número de IDs
    num_caracteres = int(input("Número de caracteres: "))
    num_ids = int(input("Número de IDs a generar: "))
    
    caracteres = string.ascii_letters + string.digits  # Letras (mayúsculas y minúsculas) y números
    
    ids = []
    for _ in range(num_ids):
        user_id = ''.join(random.choice(caracteres) for _ in range(num_caracteres))
        ids.append(user_id)
    
    return '\n'.join(ids)

print(user_id_gen_by_user())  
#3 Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
import random

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
print(rgb_color_gen())  

#Exercises Level 2
#1  Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random

def list_of_hexa_colors(n):
    colores_hex = []
    for _ in range(n):
        color = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))  
        colores_hex.append(color)
    return colores_hex

print(list_of_hexa_colors(5))  
#2 Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
import random

def list_of_rgb_colors(n):
    colores_rgb = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colores_rgb.append(f"rgb({r},{g},{b})")
    return colores_rgb


print(list_of_rgb_colors(5)) 

#3Write a function generate_colors which can generate any number of hexa or rgb colors.
import random

def generate_colors(tipo, n):
    colores = []
    if tipo == 'hexa':
        for _ in range(n):
            color = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))
            colores.append(color)
    elif tipo == 'rgb':
        for _ in range(n):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            colores.append(f"rgb({r},{g},{b})")
    return colores

print(generate_colors('hexa', 3))  
print(generate_colors('rgb', 1))  

#Exercises Level 3
#1 Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

mi_lista = [1, 2, 3, 4, 5]
print(shuffle_list(mi_lista))  
#2 Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
import random

def generar_numeros_unicos():
    numeros = random.sample(range(10), 7)  
    return numeros

print(generar_numeros_unicos()) 
