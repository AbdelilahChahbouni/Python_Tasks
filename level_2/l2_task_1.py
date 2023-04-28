# Transform Names To UpperCase Using Normal List , List Comprehension , Fonctional Programming

names = ["mahmouda" , "farida" , "ali" , "ahmed" , "mohamed" , "taha"]

# Using Normal List

def transform_to_uppercase(names):
    new_names = []
    for name in names:
        new_names.append(name.upper())
    return new_names

print(transform_to_uppercase(names))


# Using List Comprehension

def transform_to_uppercase2(names):
    new_names = [name.upper() for name in names ]
    return new_names


print(transform_to_uppercase2(names))


# Using Fonctional Programming

def func(name):
    return name.upper()

new_names = map(func, names)

print(list(new_names))



