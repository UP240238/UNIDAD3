#Exercises: Level 1
#1Iterate 0 to 10 using for loop, do the same using while loop.


for i in range(11): 
    print(i)

#2Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10,-1,-1):
    print(i)

#3Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(1, 8):  
    print('#' * i)
    
    #4 Use nested loops to create the following:
    for i in range(8):  
     for j in range(8):  
        print('#', end=' ')  
    print()

    #5 Print the following pattern:
    for i in range(11):  
     print(f"{i} x {i} = {i * i}")

     #6 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
     lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for item in lista:
    print(item)

    #7 Use for loop to iterate from 0 to 100 and print only even numbers
    for i in range(100,-1,-2):
     print(i)

  #8Use for loop to iterate from 0 to 100 and print only odd numbers
     for i in range(100,-1,-3):
      print(i)


 #Exercises: Level 2
 #1Use for loop to iterate from 0 to 100 and print the sum of all numbers.
total=0

for i in range(101): 
    total +=   i
print(total)
#2Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
par_sum = 0  
imp_sum = 0   

for i in range(101):  
    if i % 2 == 0:  
        par_sum += i
    else:  
        imp_sum += i

        print(imp_sum)
        print(par_sum)
        
        #Exercises: Level 3
        #1Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

        countries = [
    'Afganistán', 'Albania', 'Argelia', 'Andorra', 'Angola', 'Antigua y Barbuda', 'Argentina', 'Armenia', 'Australia',
    'Austria', 'Azerbaiyán', 'Bahamas', 'Bahréin', 'Bangladés', 'Barbados', 'Bielorrusia', 'Bélgica', 'Belice', 'Benín',
    'Bután', 'Bolivia', 'Bosnia y Herzegovina', 'Botsuana', 'Brasil', 'Brunéi', 'Bulgaria', 'Burkina Faso', 'Burundí',
    'Camboya', 'Camerún', 'Canadá', 'Cabo Verde', 'República Centroafricana', 'Chad', 'Chile', 'China', 'Colombia', 'Comoras',
    'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Costa de Marfil", 'Croacia', 'Cuba', 'Chipre', 'República Checa', 'Dinamarca',
    'Yibuti', 'Dominica', 'República Dominicana', 'Timor Oriental (Timor Timur)', 'Ecuador', 'Egipto', 'El Salvador', 'Guinea Ecuatorial',
    'Eritrea', 'Estonia', 'Etiopía', 'Fiyi', 'Finlandia', 'Francia', 'Gabón', 'Gambia', 'Georgia', 'Alemania', 'Ghana', 'Grecia',
    'Granada', 'Guatemala', 'Guinea', 'Guinea-Bisáu', 'Guyana', 'Haití', 'Honduras', 'Hungría', 'Islandia', 'India', 'Indonesia',
    'Irán', 'Irak', 'Irlanda', 'Israel', 'Italia', 'Jamaica', 'Japón', 'Jordania', 'Kazajistán', 'Kenia', 'Kiribati', 'Corea del Norte',
    'Corea del Sur', 'Kuwait', 'Kirguistán', 'Laos', 'Letonia', 'Líbano', 'Lesoto', 'Liberia', 'Libia', 'Liechtenstein', 'Lituania',
    'Luxemburgo', 'Macedonia', 'Madagascar', 'Malawi', 'Malasia', 'Maldivas', 'Malí', 'Malta', 'Islas Marshall', 'Mauritania',
    'Mauricio', 'México', 'Micronesia', 'Moldavia', 'Mónaco', 'Mongolia', 'Marruecos', 'Mozambique', 'Birmania', 'Namibia', 'Nauru',
    'Nepal', 'Países Bajos', 'Nueva Zelanda', 'Nicaragua', 'Níger', 'Nigeria', 'Noruega', 'Omán', 'Pakistán', 'Palau', 'Panamá',
    'Papúa Nueva Guinea', 'Paraguay', 'Perú', 'Filipinas', 'Polonia', 'Portugal', 'Catar', 'Rumanía', 'Rusia', 'Ruanda',
    'San Cristóbal y Nieves', 'Santa Lucía', 'San Vicente', 'Samoa', 'San Marino', 'Santo Tomé y Príncipe', 'Arabia Saudita', 'Senegal',
    'Serbia y Montenegro', 'Seychelles', 'Sierra Leona', 'Singapur', 'Eslovaquia', 'Eslovenia', 'Islas Salomón', 'Somalia',
    'Sudáfrica', 'España', 'Sri Lanka', 'Sudán', 'Surinam', 'Suazilandia', 'Suecia', 'Suiza', 'Siria', 'Taiwán', 'Tayikistán',
    'Tanzania', 'Tailandia', 'Togo', 'Tonga', 'Trinidad y Tobago', 'Túnez', 'Turquía', 'Turkmenistán', 'Tuvalu', 'Uganda', 'Ucrania',
    'Emiratos Árabes Unidos', 'Reino Unido', 'Estados Unidos', 'Uruguay', 'Uzbekistán', 'Vanuatu', 'Ciudad del Vaticano', 'Venezuela',
    'Vietnam', 'Yemen', 'Zambia', 'Zimbabue',
]
countries_with_land = [country for country in countries if 'land' in country.lower()]

print(countries_with_land)

#2his is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.


fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])
print(reversed_fruits)