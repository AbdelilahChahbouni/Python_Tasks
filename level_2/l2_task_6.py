# Unpack The List :

names = ["mahmoud" , "farida" , "ali" , "ahmed" , "mohamed" , "taha" , "nour"]

# 1- a = First Index And b = Rest Of The List

a , *b = names

print(a , b)

# 2- a = First Index And b = Last Index

a , *_ , b = names

print(a , b)

# 3- a = First Index b = Second Index

a , b , *_ = names


print(a , b)

