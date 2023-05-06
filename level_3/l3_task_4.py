# Currency Converter 




class CurrencyConverter():
    signs = {"usd-euro" : 0.89
            ,"usd-egp" : 30.27
            ,"euro-usd" : 1.12
            , "euro-egp" : 3.94
            ,"egp-usd": 0.033
            ,"egp-euro": 0.029
            ,"dirham-euro" : 0.089
            ,"dirham-usd" : 0.10
            ,"dirham-egp" : 3.03
            ,"usd-dirham" : 9.99
            ,"euro-dirham" : 11.2
            ,"egp-dirham" : 0.33  }

    def __init__(self):
        print("Availlable Currency Sign To Convert : \n * USD\n * EURO\n * EGP\n * DIRHAM")
        flag = True
        while flag:
            try:
                self.converter()
            except:
                print("Please Enter Sign Name Correct ..")
                self.converter()
            state = input("Press Enter To Continue Or quit To Leave :  ")
            if state == "quit":
                flag = False
                print("GoodBye ..")






    def converter(self):
        fr = input("From : ")
        fr_value = input("How Match : ")
        to = input("To : ")
        multi = fr.lower()+"-"+to.lower()
        print(f"*******************\n{fr_value} {fr} = {int(fr_value) * self.signs[fr.lower()+'-'+to.lower()]} {to}\n*******************")


#Create Instance

test = CurrencyConverter()





