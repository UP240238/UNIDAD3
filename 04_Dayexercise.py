letter = 'P'                
print(letter)               
print(len(letter))          
greeting = 'Hello, World!'  
print(greeting)            
print(len(greeting))       
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)
string='''Hola. 
Hello.
 Hallo.
   Bonjuor'''
print(string)
o='''uno
dos
tres
cuatro
cinco'''
print(o)
first_name = 'Aldo'
last_name = 'Reynoso'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) 
print(len(first_name)) 
print(len(last_name))   
print(len(first_name) > len(last_name)) 
print(len(full_name)) 

nombre='Aldo'
print('Mi nombre es %s' %nombre)
edad=18
print('Tengo %d'%edad)
altura=1.73
print('Mi altura es %f metros' %altura)
pi = 3.14159265359
print("El valor de pi es %.3f" % pi)
print("Mi nombre es %s, tengo %d años y mido %.2f metros." % (nombre, edad, altura))
texto = "Python es increíble"
print(texto[0:9])
print(texto[:6])
print(texto[7:])

texto = "Hola mi nombre es aldo reynoso gonzalez"
invertido = texto[::-1]
print(invertido)
texto = "  hola Mundo  "
print(texto.upper())      # "  HOLA MUNDO  "
print(texto.lower())      # "  hola mundo  "
print(texto.capitalize()) # "  hola mundo  "
print(texto.title())      # "  Hola Mundo  "
print(texto.strip())      # "hola Mundo"  (sin espacios extra)
texto = "Python es genial"
print(texto.find("es"))    # 7
print(texto.index("genial"))  # 10
print(texto.replace("genial", "fácil"))  # "Python es fácil"
texto = "Python3"
print(texto.startswith("Py"))  # True
print(texto.endswith("3"))     # True
print(texto.isalpha())         # False (contiene un número)
print("123".isdigit())         # True
print("Hola123".isalnum())     # True
texto = "manzana,pera,uva"
frutas = texto.split(",")  # ['manzana', 'pera', 'uva']
print(frutas)

nueva_cadena = " - ".join(frutas)
print(nueva_cadena)  # "manzana - pera - uva"

#Número 1
Parte1='Thirty'
Parte2='Days'
Parte3='Of'
Parte4='Python'
Espacio=' '
Frase=Parte1+Espacio+Parte2+Espacio+Parte3+Espacio+Parte4
print(Frase)
#Número2 
parte1='Coding'
parte2='For'
parte3='All'
espacioo=' '
frase=parte1+espacioo+parte2+espacioo+parte3
print(frase)
#Número3
company='Coding For All'
#Número4 
print(company)
#Número 5
lenght_company=len(company)
print(lenght_company)
#Número 6
company = "Coding For All"
companyupper = company.upper()
print(companyupper)
#Número7
company = "Coding For All"
companylower = company.lower()
print(companylower)
#Número8 
company = "Coding For All"
companycapitalize = company.capitalize()
print(companycapitalize)
company = "Coding For All"
companytitle = company.title()
print(companytitle)
company = "Coding For All"
companyswapcase = company.swapcase()
print(companyswapcase)
#Número9 
company = "Coding For All"
words = company.split()  
sliced_string = " ".join(words[1:])  
print(sliced_string)
#Número10
company='Coding For All'
sub_string='Coding'
print(company.index(sub_string)) 
print(company.index(sub_string, 0))
#Número11
print(company.replace('Coding','Python'))
#Número 12
replaceword1=company.replace('Coding','Everyone')
replaceword2=company.replace('All','Python')
print(replaceword1)
print(replaceword2)
#Número13 
company='Coding For All'
print(company.split())
#Número 14 
apps="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(apps.split(','))
#Número 15 
company='Coding For All'
company0=company[0]
print(company0)
#Número 16 
company='Coding For All'
company0=company[13]
print(company0)
#Número17 
company='Coding For All'
company0=company[10]
print(company0)
#Número 18
PY= 'Python For Everyone'
print(PY.split())
PY0=PY[0]
PY1=PY[7]
PY2=PY[11]
print(PY0,PY1,PY2)

#Número 19 
CAF= 'Coding For All'
print(CAF.split())
CAF0=CAF[0]
CAF1=CAF[7]
CAF2=CAF[11]
print(CAF0,CAF1,CAF2)
#Número 20 
company='Coding For All'
position=company.index('C')
print(position)
#Número 21 
company='Coding For All People'
find=company.rfind('l')
print(find)
#Número 22
company='Coding For All People'
find=company.rfind('F')
print(find)
#Número 23 
word='You cannot end a sentence with because because because is a conjunction'
inword=word.index('because')
print(inword)
#Número 24 
word='You cannot end a sentence with because because because is a conjunction'
inword=word.rindex('because')
print(inword)
#Número 25 
word='You cannot end a sentence with because because because is a conjunction'
print(word.replace('because', ''))
#Número 26 
word='You cannot end a sentence with because because because is a conjunction'
inword=word.find('because')
print(inword)
#Número 27 
word='You cannot end a sentence with because because because is a conjunction'
print(word.replace('because', ''))
#Número 28 
company='Coding For All'
print(company.startswith('Coding'))
#Númerp 29 
company='Coding For All'
print(company.endswith('coding'))
#Número30 
Company='   Coding For All      '  
print(Company.strip(' '))
#Número 31 
challenge = '30DaysOfPython'
print(challenge.isidentifier())
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) 
#Número 32 
pythonlibraries=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
jpy=' '.join(pythonlibraries)
print(jpy)
#Número 33 
text = "I am enjoying this challenge.\nI just wonder what is next"
print(text)
#Número 34 
text1='Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki'
print(text1)
#Número 35 
radio = 10
area = 3.14 * radio ** 2
F='The area of a circle with radius {} is {} meters square.'.format(radio,area)
print(F)
#Número 36 
a=8
b=6
suma=a+b
resta=a-b
multiplicación=a*b
división=a/b
porcetaje=a%b
Division =a//b
Exponentes=a**b
S='La suma de {} mas {} es{} '.format(a,b,suma)
R='La resta de {} mas {} es {}'.format(a,b,resta)
M='La multiplicaion de {} mas {} es {}'.format(a,b,multiplicación)
d='La division de {} mas {} es {}'.format(a,b,división)
P='El porcentaje de {} mas {} es {}'.format(a,b,porcetaje)
D='La Divison de {} mas {} es {}'.format(a,b,Division)
E='La potencia de {}  a la  {} es {}'.format(a,b,Exponentes)
print(S)
print(R)
print(M)
print(d)
print(P)
print(D)
print(E)
