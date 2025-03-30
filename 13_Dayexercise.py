#Exercises
#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos_y_cero = [num for num in numbers if num <= 0]
print(negativos_y_cero)  # [-4, -3, -2, -1, 0]

#2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lista_aplanada = [item for sublist in list_of_lists for subsublist in sublist for item in subsublist]
print(lista_aplanada)  
#3
tuplas = [(x, 1, x, x**2, x**3, x**4, x**5) for x in range(11)]
print(tuplas)

#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

result = [[country[0][0].upper(), country[0][0][:3].upper(), country[0][1].upper()] for country in countries]
print(result)  


#5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_result = [{'country': country[0][0].upper(), 'city': country[0][1].upper()} for country in countries]
print(dict_result)  
#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenado = [' '.join(name[0]) for name in names]
print(concatenado)  
#7
calcular_slope_y_intercept = lambda x1, y1, x2, y2: ( (y2 - y1) / (x2 - x1), y1 - ((y2 - y1) / (x2 - x1)) * x1 )
pendiente, interseccion = calcular_slope_y_intercept(1, 2, 3, 4)
print(f"Pendiente: {pendiente}, Intersección: {interseccion}")


