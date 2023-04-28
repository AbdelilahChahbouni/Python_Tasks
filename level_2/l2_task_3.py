 
# Get Names Contain Start With "t" in The List Using [Normal List , List Comprehension , Fonctional Programming]


names = ["mahmouda" , "farida" , "ali" , "ahmed" , "mohamed" , "taha" , "nour" , "tarik"]

# Using Normal List

def names_filter(names):
    new_names = []
    for name in names:
        if name.startswith("t") == True:
            new_names.append(name)
    return new_names


print(names_filter(names))

# Using List Comprehension

def names_filter2(names):
    new_names = [name for name in names if name.startswith("t") == True]
    return new_names

print(names_filter2(names))

# Using Fonctional Programming

def func(name):
    if name.startswith("t") == True:
        return name

print(list(filter(func , names)))
