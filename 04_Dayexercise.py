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

#Número 1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
Parte1='Thirty'
Parte2='Days'
Parte3='Of'
Parte4='Python'
Espacio=' '
Frase=Parte1+Espacio+Parte2+Espacio+Parte3+Espacio+Parte4
print(Frase)
#Número2  Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
parte1='Coding'
parte2='For'
parte3='All'
espacioo=' '
frase=parte1+espacioo+parte2+espacioo+parte3
print(frase)
#Número3 Declare a variable named company and assign it to an initial value "Coding For All".
company='Coding For All'
#Número4 Print the variable company using print().
print(company)
#Número 5 Print the length of the company string using len() method and print().
lenght_company=len(company)
print(lenght_company)
#Número 6 Change all the characters to uppercase letters using upper() method.
company = "Coding For All"
companyupper = company.upper()
print(companyupper)
#Número7 Change all the characters to lowercase letters using lower() method.
company = "Coding For All"
companylower = company.lower()
print(companylower)
#Número8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
company = "Coding For All"
companycapitalize = company.capitalize()
print(companycapitalize)
company = "Coding For All"
companytitle = company.title()
print(companytitle)
company = "Coding For All"
companyswapcase = company.swapcase()
print(companyswapcase)
#Número9 Cut(slice) out the first word of Coding For All string.
company = "Coding For All"
words = company.split()  
sliced_string = " ".join(words[1:])  
print(sliced_string)
#Número10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
company='Coding For All'
sub_string='Coding'
print(company.index(sub_string)) 
print(company.index(sub_string, 0))
#Número11 Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding','Python'))
#Número 12 Change Python for Everyone to Python for All using the replace method or other methods.
replaceword1=company.replace('Coding','Everyone')
replaceword2=company.replace('All','Python')
print(replaceword1)
print(replaceword2)
#Número13 Split the string 'Coding For All' using space as the separator (split()) .
company='Coding For All'
print(company.split())
#Número 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
apps="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(apps.split(','))
#Número 15  What is the character at index 0 in the string Coding For All.
company='Coding For All'
company0=company[0]
print(company0)
#Número 16  What is the last index of the string Coding For All.
company='Coding For All'
company0=company[13]
print(company0)
#Número17  What character is at index 10 in "Coding For All" string.
company='Coding For All'
company0=company[10]
print(company0)
#Número 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
PY= 'Python For Everyone'
print(PY.split())
PY0=PY[0]
PY1=PY[7]
PY2=PY[11]
print(PY0,PY1,PY2)

#Número 19 Create an acronym or an abbreviation for the name 'Coding For All'.
CAF= 'Coding For All'
print(CAF.split())
CAF0=CAF[0]
CAF1=CAF[7]
CAF2=CAF[11]
print(CAF0,CAF1,CAF2)
#Número 20  Use index to determine the position of the first occurrence of C in Coding For All. 
company='Coding For All'
position=company.index('C')
print(position)
#Número 21 Use index to determine the position of the first occurrence of F in Coding For All.
company='Coding For All People'
find=company.rfind('l')
print(find)
#Número 22  Use rfind to determine the position of the last occurrence of l in Coding For All People.
company='Coding For All People'
find=company.rfind('F')
print(find)
#Número 23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
word='You cannot end a sentence with because because because is a conjunction'
inword=word.index('because')
print(inword)
#Número 24  Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
word='You cannot end a sentence with because because because is a conjunction'
inword=word.rindex('because')
print(inword)
#Número 25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
word='You cannot end a sentence with because because because is a conjunction'
print(word.replace('because', ''))
#Número 26 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
word='You cannot end a sentence with because because because is a conjunction'
inword=word.find('because')
print(inword)
#Número 27 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
word='You cannot end a sentence with because because because is a conjunction'
print(word.replace('because', ''))
#Número 28 Does ''Coding For All' start with a substring Coding?
company='Coding For All'
print(company.startswith('Coding'))
#Númerp 29 Does 'Coding For All' end with a substring coding?
company='Coding For All'
print(company.endswith('coding'))
#Número30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
Company='   Coding For All      '  
print(Company.strip(' '))
#Número 31 Which one of the following variables return True when we use the method isidentifier():
challenge = '30DaysOfPython'
print(challenge.isidentifier())
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) 
#Número 32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
pythonlibraries=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
jpy=' '.join(pythonlibraries)
print(jpy)
#Número 33 Use the new line escape sequence to separate the following sentences
text = "I am enjoying this challenge.\nI just wonder what is next"
print(text)
#Número 34 Use a tab escape sequence to write the following lines.
text1='Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki'
print(text1)
#Número 35 Use the string formatting method to display the following:
radio = 10
area = 3.14 * radio ** 2
F='The area of a circle with radius {} is {} meters square.'.format(radio,area)
print(F)
#Número 36 Make the following using string formatting methods:
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
