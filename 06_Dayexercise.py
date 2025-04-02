#Excersise level 1
#1Create an empty tuple
tuple=()
#2Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
Tuple=('carlos','ana','karla')
#3Join brothers and sisters tuples and assign it to siblings
sum_tuples=tuple+Tuple
print(sum_tuples)
#4How many siblings do you have?
print(len(sum_tuples))
#5Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members=list(Tuple)
family_members.append('pepe')
family_members.append('ximena')
print(family_members)
#Exercises 2
#1Unpack siblings and parents from family_members
print(family_members[0:2],'They are parents')
print(family_members[2:],'They are siblings')
#2Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
tuple_fruits=('apple','banana','mango','orange','pineaple','strawberry')
tuple_animals=('cow','chicken','pig','fish')
tuple_vegetables=('carrot','cucumber','letuce','toamtoe','potato')
food_stuff_tp=tuple_fruits+tuple_animals+tuple_vegetables
print(food_stuff_tp)
#3Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt=list(food_stuff_tp)
#4Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
slice=len(food_stuff_lt)//2
print(slice)
#5Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_tp[0:3])
print(food_stuff_tp[12:])
#6Delete the food_staff_tp tuple completely
del food_stuff_tp
#7 Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia'in nordic_countries)
print('Iceland'in nordic_countries)