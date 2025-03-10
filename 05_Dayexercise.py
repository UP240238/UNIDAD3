#1
list=[]
#2
List=['mango','pera','banana','sandia','fresa']
#3
print(len(List))
#4
first_item=List[0]
middle_item=List[2]
last_item=List[4]
print(first_item)
print(middle_item)
print(last_item)
#5
mixed_data_types=['Aldo','18','1.70','single','Av.Luisa Fernandez Villa no 77']
#6
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
#7 
print(it_companies)
#8
print(len(it_companies))
#9
first_company=it_companies[0]
middle_company=it_companies[3]
last_company=it_companies[6]
print(first_company)
print(middle_company)
print(last_company)
#10
it_companies[4]='HBO'
print(it_companies)
#11
it_companies.append('Tesla')
print(it_companies)
#12
it_companies.insert(3,'Tesla')
print(it_companies)
#13

#14
it_companies_str = "#;  ".join(it_companies)
print(it_companies_str)
#15
Chekingitems='Certain'in it_companies
print(Chekingitems)
#16
it_companies.sort()
print(it_companies)
#17
it_companies.sort(reverse=True)
print(it_companies)
#18
sublist = it_companies[0:3]
print(sublist)
#19
Sublast = it_companies[5:8]
print(Sublast)
#20 
Submiddle = it_companies[4:5]
print(Submiddle)
#21 
it_companies.remove('Tesla')
print(it_companies)
#22
it_companies.remove('HBO')
print(it_companies)
#23
it_companies.remove('Amazon')
print(it_companies)
#24
it_companies.clear()
print(it_companies)
#25 
del it_companies
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joinlists=front_end+back_end
print(joinlists)
#27 
fullstack=joinlists.copy()
fullstack.insert(5,'Python')
fullstack.insert(6,'SQL')
print(fullstack)
#Exercises nivel 2 
#1 
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

min_age = min(ages)
max_age = max(ages)
print("Min age:", min_age)
print("Max age:", max_age)


