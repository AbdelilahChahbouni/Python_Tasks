#Task : 2 Function Tackes 2 Numbers Print All Numbers Between 1 And 100 Than can be devided on x , y 

# Method : 1

def check_devided_numbers1(num1 , num2):
    for number in range(1 , 101):
        if number % num1 == 0 and number % num2 == 0 :
            print(number)


# Method : 2


def check_devided_numbers2(num1 , num2):
    numbers = [num for num in  range(1 , 101) if num % num1 == 0 and num % num2 == 0]
    print(numbers)



# Call Functions


check_devided_numbers1(3 , 6)
check_devided_numbers2(3 , 6)

