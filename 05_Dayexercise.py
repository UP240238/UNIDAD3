#1 Declare an empty list
list=[]
#2 Declare a list with more than 5 items
List=['mango','pera','banana','sandia','fresa']
#3 Find the length of your list
print(len(List))
#4 Get the first item, the middle item and the last item of the list
first_item=List[0]
middle_item=List[2]
last_item=List[4]
print(first_item)
print(middle_item)
print(last_item)
#5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=['Aldo','18','1.70','single','Av.Luisa Fernandez Villa no 77']
#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
#7 Print the list using print()
print(it_companies)
#8Print the number of companies in the list
print(len(it_companies))
#9 Print the first, middle and last company
first_company=it_companies[0]
middle_company=it_companies[3]
last_company=it_companies[6]
print(first_company)
print(middle_company)
print(last_company)
#10 Print the list after modifying one of the companies
it_companies[4]='HBO'
print(it_companies)
#11 Add an IT company to it_companies
it_companies.append('Tesla')
print(it_companies)
#12 nsert an IT company in the middle of the companies list
it_companies.insert(3,'Tesla')
print(it_companies)
#13Change one of the it_companies names to uppercase (IBM excluded!)
#14 Join the it_companies with a string '#;  '
it_companies_str = "#;  ".join(it_companies)
print(it_companies_str)
#15 Check if a certain company exists in the it_companies list.
Chekingitems='Certain'in it_companies
print(Chekingitems)
#16Sort the list using sort() method
it_companies.sort()
print(it_companies)
#17 Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)
#18Slice out the first 3 companies from the list
sublist = it_companies[0:3]
print(sublist)
#19Slice out the last 3 companies from the list
Sublast = it_companies[5:8]
print(Sublast)
#20 Slice out the middle IT company or companies from the list
Submiddle = it_companies[4:5]
print(Submiddle)
#21 Remove the first IT company from the list
it_companies.remove('Tesla')
print(it_companies)
#22Remove the middle IT company or companies from the list
it_companies.remove('HBO')
print(it_companies)
#23Remove the last IT company from the list
it_companies.remove('Amazon')
print(it_companies)
#24Remove all IT companies from the list
it_companies.clear()
print(it_companies)
#25 Destroy the IT companies list
del it_companies
#26Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joinlists=front_end+back_end
print(joinlists)
#27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
fullstack=joinlists.copy()
fullstack.insert(5,'Python')
fullstack.insert(6,'SQL')
print(fullstack)
#Exercises nivel 2 
#1 Find the middle country(ies) in the countries list
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

min_age = min(ages)
max_age = max(ages)
print("Min age:", min_age)
print("Max age:", max_age)
#2 Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
mid_index = len(countries) // 2
print(mid_index)
del countries[:3]
print(countries)
