#Exercises level 1 
#1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age= [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
print(len(A))
print(len(B))
print(len(age))
#2
it_companies.add('Twitter')
print(it_companies)
#3 
new_companies={'TikTok','Samsung','Uber','Nike','Adidas'}
it_companies.update(new_companies)
print(it_companies)
#4
it_companies.discard('Nike')
print(it_companies)
#5
#La diferencia entre remove y discard es que remove te genera u error si lo que quieres eliminar no esta en el set y discard no marca el error
#Exercise2
AB=A.union(B)
print(AB)
#2
AB= A&B
print(AB)
#3
print(A.issubset(B))
#4
print(A.isdisjoint(B))
#5
union_AB = A.union(B)
union_BA = B.union(A)
#6
sym_diff_2 = A.symmetric_difference(B)
print(sym_diff_2)
#7
del it_companies
del A
del B
del age
#Exercise level 3 
age_set=set(age)
listlen=len(age)
setlen=(age_set)
#2
#La diferencia es que str es una secuencia de caracteres , la lista es una coleccion ordenada y se puede modificar, la tupla es lo mismo que la lista pero esta es inmutable que no se pude modificar 
#3
sentence = "I am a teacher and I love to inspire and teach people"
unique_words = set(sentence.split())
print(len(unique_words))

