# Temprature Converter 

def temp_converter():

    print("\n" +"*********** Temprature Converter From Fahrenheit  To Celcius And Back *************" + "\n")
    flag = True
    while flag:
        chose_unite = input("Enter 1 Or 2 : \n 1 - Fahrenheit To Celcius \n 2 - Celcius To Fahrenheit \n >> ")
        if chose_unite == "1":
            f = input("Enter The Temprature in Fahrenheit Unite ")
            result = (float(f) - 32) * 5/9
            print(f"{result:.2f} C")
        elif chose_unite == "2":
            c = input("Enter The Temprature in Celcius Unite ")
            result = (float(c) * 9/5) + 32
            print(f"{result:.2f} F")

        flag = input("You Want To Continue y Or n  ")
        if flag == "n": flag = False


temp_converter()

