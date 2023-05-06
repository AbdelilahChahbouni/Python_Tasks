# Temprature Converter

# Methode 1: 
def temp_converter():

    print("\n" +"*********** Temprature Converter From Fahrenheit  To Celcius And Back *************" + "\n")
    flag = True
    while flag:
        chose_unite = input("Enter 1 Or 2 : \n 1 - Fahrenheit To Celcius \n 2 - Celcius To Fahrenheit \n >> ")
        if chose_unite == "1":
            f = input("Enter The Temprature Value :  ")
            result = (float(f) - 32) * 5/9
            print(f"{f} F = {result:.2f} C")
        elif chose_unite == "2":
            c = input("Enter The Temprature Value :  ")
            result = (float(c) * 9/5) + 32
            print(f"{c} C = {result:.2f} F")

        flag = input("You Want To Continue y Or n  ")
        if flag == "n": 
            flag = False
            print("GoodBye ..")

# Call Function 
#temp_converter()



# Methode 2:


class TempConverter():
    def __init__ (self):
        print("\n" +"*********** Temprature Converter From Fahrenheit  To Celcius And Back *************" + "\n")
        flag = True
        while flag:
            chose_unite = input("Enter 1 Or 2 : \n 1 - Fahrenheit To Celcius \n 2 - Celcius To Fahrenheit \n >> ")
            if chose_unite == "1":
                f = input("Enter The Temprature Value :  ")
                self.fahrTocel(f)
                
            elif chose_unite == "2":
                c = input("Enter The Temprature Value :  ")
                self.celTofahr(c)


            flag = input("You Want To Continue y Or n  ")
            if flag == "n": 
                flag = False
                print("GoodBye ..")
        

    def fahrTocel(self, f):
        result = (float(f) - 32) * 5
        print(f"{f} F = {result:.2f} C")
    
        

    def celTofahr(self , c):
        result = (float(c) * 9/5) + 32
        print(f"{c} C = {result:.2f} F")
        



# Create Instance
instance = TempConverter()





