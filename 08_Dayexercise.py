#1
dog={

}
#2
dog={"Name":"Firulais",
     "Color":"White",
     "Breed":"Husky",
     "Legs":"Four" ,
     "Age": 5
}
#3
student_dictionary={"First name":"Aldo",
                    "Last name ":"Reynoso ",
                    "Gender":"Male",
                    "Age":18 ,
                    "Marital Status":"Single",
                    "Skills":["Python","Videogames"],
                    "Country":"México",
                    "City":"Aguascalientes",
                    "Address":"Av.Luisa Fernandez Villa no 77"

}
print(student_dictionary)
#4
print(len(student_dictionary))
#5
skills = student_dictionary["Skills"]
print("Skills:", skills)
print("Tipo de dato:", type(skills))
#6
student_dictionary['Skills'].append('HTML')
print(student_dictionary)
#7
key= list(student_dictionary.keys())
print(key)
#8
studentlist=(student_dictionary)
print(studentlist)
#9
student_tuples = list(studentlist.items())
print(student_tuples)
#10
del student_dictionary["Skills"]
print(student_dictionary)
#11
del student_dictionary
