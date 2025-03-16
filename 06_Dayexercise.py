#Excersise level 1
#1
tuple=()
#2
Tuple=('carlos','ana','karla')
#3
sum_tuples=tuple+Tuple
print(sum_tuples)
#4
print(len(sum_tuples))
#5
family_members=list(Tuple)
family_members.append('pepe')
family_members.append('ximena')
print(family_members)
#Exercises 2
#1
print(family_members[0:2],'They are parents')
print(family_members[2:],'They are siblings')
#2
tuple_fruits=('apple','banana','mango','orange','pineaple','strawberry')
tuple_animals=('cow','chicken','pig','fish')
tuple_vegetables=('carrot','cucumber','letuce','toamtoe','potato')
food_stuff_tp=tuple_fruits+tuple_animals+tuple_vegetables
print(food_stuff_tp)
#3
food_stuff_lt=list(food_stuff_tp)
#4
slice=len(food_stuff_lt)//2
print(slice)
#5
print(food_stuff_tp[0:3])
print(food_stuff_tp[12:])
#6
del food_stuff_tp
#7 
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia'in nordic_countries)
print('Iceland'in nordic_countries)