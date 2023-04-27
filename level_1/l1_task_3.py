# Fuction Tackes 2 Numbers and Print Multiplication From y To x

# Methode 1:

def multiplication(x , y):
    for num in range(x , y+1):
        for num2 in range(11):
            print(num * num2)
        print("*" * 10)

# Methode 2:

def multiplication2(x , y):
    mulNums = [num * num2 for num in range(x , y) for num2 in range(11)]
    for nums in mulNums:
       print(nums)






multiplication(1 , 10)
multiplication2(1 , 5)



