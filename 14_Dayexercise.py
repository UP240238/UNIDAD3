#Exercise level 1
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
#Exercise level 2
#1
countries_upper = list(map(lambda x: x.upper(), countries))
print(countries_upper)

#2
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

#3
names = ["Juan", "Ana", "Pedro", "Maria"]
names_upper = list(map(lambda x: x.upper(), names))
print(names_upper)

#4
countries_with_land = list(filter(lambda x: 'land' in x.lower(), countries))
print(countries_with_land)

#5
countries_six_chars = list(filter(lambda x: len(x) == 6, countries))
print(countries_six_chars)

#6
countries_six_or_more_chars = list(filter(lambda x: len(x) >= 6, countries))
print(countries_six_or_more_chars)

#7
countries_starting_with_E = list(filter(lambda x: x.startswith('E'), countries))
print(countries_starting_with_E)

#8
countries_land_upper = list(
    filter(lambda x: 'LAND' in x, map(lambda x: x.upper(), countries))
)
print(countries_land_upper)

#9
def get_string_lists(lst):
    return [item for item in lst if isinstance(item, str)]

# Ejemplo de uso
mixed_list = countries + [123, 456, "Australia", 789]
only_strings = get_string_lists(mixed_list)
print(only_strings)

#10
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)

#11
country_sentence = reduce(
    lambda x, y: x + ", " + y, countries
) + " are north European countries"
print(country_sentence)

#12
def categorize_countries(countries):
    return [
        country
        for country in countries
        if "land" in country.lower() or "ia" in country.lower() or "island" in country.lower() or "stan" in country.lower()
    ]

categorized_countries = categorize_countries(countries)
print(categorized_countries)

#13
from collections import defaultdict

def countries_by_first_letter(countries):
    letter_dict = defaultdict(int)
    for country in countries:
        first_letter = country[0].upper()
        letter_dict[first_letter] += 1
    return dict(letter_dict)

letter_count = countries_by_first_letter(countries)
print(letter_count)

#14
def get_first_ten_countries(countries):
    return countries[:10]

# Ejemplo de uso
first_ten_countries = get_first_ten_countries(countries)
print(first_ten_countries)

#15
def get_last_ten_countries(countries):
    return countries[-10:]

last_ten_countries = get_last_ten_countries(countries)
print(last_ten_countries)


#Exercise level 3
#1
