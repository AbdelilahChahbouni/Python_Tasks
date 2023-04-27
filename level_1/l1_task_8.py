# Function Take X , Y And Print All Numbers That Can Be divided By Y From X To 100


#Methode 1:

def numbers_divided_by_y(x , y):
    for item in range(x , 101):
        if item % y == 0:
            print(item)







# Methode 2:

def numbers_divided_by_y2(x , y):
    numbers = [item for item in range( x , 101) if item % y == 0]
    print(numbers)


numbers_divided_by_y(10 , 4)
numbers_divided_by_y2(10 , 4)




