#Exercises level 1 
#1Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age= [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
print(len(A))
print(len(B))
print(len(age))
#2Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
#3 Insert multiple IT companies at once to the set it_companies
new_companies={'TikTok','Samsung','Uber','Nike','Adidas'}
it_companies.update(new_companies)
print(it_companies)
#4Remove one of the companies from the set it_companies
it_companies.discard('Nike')
print(it_companies)
#5What is the difference between remove and discard
#La diferencia entre remove y discard es que remove te genera u error si lo que quieres eliminar no esta en el set y discard no marca el error
#Exercise2
#1 Join A and B
AB=A.union(B)
print(AB)
#2Find A intersection B
AB= A&B
print(AB)
#3Is A subset of B
print(A.issubset(B))
#4Are A and B disjoint sets
print(A.isdisjoint(B))
#5Join A with B and B with A
union_AB = A.union(B)
union_BA = B.union(A)
#6What is the symmetric difference between A and B
sym_diff_2 = A.symmetric_difference(B)
print(sym_diff_2)
#7Delete the sets completely
del it_companies
del A
del B
del age
#Exercise level 3 
#1Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age= [22, 19, 24, 25, 26, 24, 25, 24]
age_set=set(age)
listlen=len(age)
setlen=(age_set)
#2Explain the difference between the following data types: string, list, tuple and set
#La diferencia es que str es una secuencia de caracteres , la lista es una coleccion ordenada y se puede modificar, la tupla es lo mismo que la lista pero esta es inmutable que no se pude modificar 
#3I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
unique_words = set(sentence.split())
print(len(unique_words))

