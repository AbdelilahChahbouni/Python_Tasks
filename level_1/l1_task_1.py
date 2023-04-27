# Task 1 : Fuction tackes 2 numbers x , y and print 2 lists containing th2 odd and the even numbers in range x , y

# Method: 1

def get_odd_even_numbers1(start_number , end_number):
    odd_numbers = []
    even_numbers = []
    for number in range(start_number , end_number+1):
        if number % 2 == 0 :
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    print(f"the odd numbers list : {odd_numbers} and even numbers list : {even_numbers}" )


# Method : 2

def get_odd_even_numbers2(start_number , end_number):
    odd_list= [num for num in range(start_number , end_number+1) if num % 2 != 0]
    even_list = [num for num in range(start_number , end_number+1) if num % 2 == 0]
    print(f"the odd numbers list : {odd_list} and even numbers list : {even_list}" )










get_odd_even_numbers1(1 , 10)
get_odd_even_numbers2(1 , 10)



