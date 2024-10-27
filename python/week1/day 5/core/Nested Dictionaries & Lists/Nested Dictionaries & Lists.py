#1. Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]
x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30
print("Updated x:", x)
print("Updated students:", students)
print("Updated sports_directory:", sports_directory)
print("Updated z:", z)
#2. Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for dictionary in some_list:
        output = ', '.join(f"{key} - {value}" for key, value in dictionary.items())
        print(output)
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

#3. Get Values From a List of Dictionaries
def Dictionary2(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])
print("First Names:")
Dictionary2('first_name', students)
print("Last Names:")
Dictionary2('last_name', students)


#4. Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{len(value)} {key.upper()}")
        for item in value:
            print(item)
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)


