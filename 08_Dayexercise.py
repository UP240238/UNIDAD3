#1Create an empty dictionary called dog
dog={

}
#2Add name, color, breed, legs, age to the dog dictionary
dog={"Name":"Firulais",
     "Color":"White",
     "Breed":"Husky",
     "Legs":"Four" ,
     "Age": 5
}
#3Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary     
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
#4Get the length of the student dictionary
print(len(student_dictionary))
#5 Get the value of skills and check the data type, it should be a list
skills = student_dictionary["Skills"]
print("Skills:", skills)
print("Tipo de dato:", type(skills))
#6 Modify the skills values by adding one or two skills
student_dictionary['Skills'].append('HTML')
print(student_dictionary)
#7Get the dictionary keys as a list
key= list(student_dictionary.keys())
print(key)
#8Get the dictionary values as a list
studentlist=(student_dictionary)
print(studentlist)
#9Change the dictionary to a list of tuples using items() method
student_tuples = list(studentlist.items())
print(student_tuples)
#10Delete one of the items in the dictionary
del student_dictionary["Skills"]
print(student_dictionary)
#11Delete one of the dictionaries
del student_dictionary
