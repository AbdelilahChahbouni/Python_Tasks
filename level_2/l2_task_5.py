
# Print A List Containt Len of Each Element in The List Using [Normal List , List Comprehension , Fonctional Programming]


names = ["mahmoud" , "farida" , "ali" , "ahmed" , "mohamed" , "taha" , "nour"]

# Using Normal List

def names_filter(names):
    new_names = []
    for name in names:
         new_names.append(len(name))
    return new_names


print(names_filter(names))

# Using List Comprehension

def names_filter2(names):
    new_names = [len(name) for name in names ]
    return new_names

print(names_filter2(names))

# Using Fonctional Programming

def func(name):
    return len(name)

print(list(map(func , names)))
