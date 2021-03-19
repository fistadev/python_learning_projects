# Exercise: remove duplicates on a list, count original list and list without duplicates

countries = [
    "Brazil",
    "Italia",
    "USA",
    "Brazil",
    "Norway",
    "Brazil",
    "Brazil",
    "Italy",
    "Norway",
    "Norway",
    "USA",
    "Mexico",
    "Portugal",
    "France",
    "France"
]
uniques = []
for country in countries:
    if country not in uniques:
        uniques.append(country)
print(uniques)
print(f'{len(countries)} countries')
print(f'{len(uniques)} unique countries')