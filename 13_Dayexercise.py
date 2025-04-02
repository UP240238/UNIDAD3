#Exercises
#1Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos_y_cero = [num for num in numbers if num <= 0]
print(negativos_y_cero)  # [-4, -3, -2, -1, 0]

#2Flatten the following list of lists of lists to a one dimensional list :
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lista_aplanada = [item for sublist in list_of_lists for subsublist in sublist for item in subsublist]
print(lista_aplanada)  
#3Using list comprehension create the following list of tuples:
tuplas = [(x, 1, x, x**2, x**3, x**4, x**5) for x in range(11)]
print(tuplas)

#4Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

result = [[country[0][0].upper(), country[0][0][:3].upper(), country[0][1].upper()] for country in countries]
print(result)  


#5Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_result = [{'country': country[0][0].upper(), 'city': country[0][1].upper()} for country in countries]
print(dict_result)  
#6Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenado = [' '.join(name[0]) for name in names]
print(concatenado)  
#7Write a lambda function which can solve a slope or y-intercept of linear functions.
calcular_slope_y_intercept = lambda x1, y1, x2, y2: ( (y2 - y1) / (x2 - x1), y1 - ((y2 - y1) / (x2 - x1)) * x1 )
pendiente, interseccion = calcular_slope_y_intercept(1, 2, 3, 4)
print(f"Pendiente: {pendiente}, Intersección: {interseccion}")


