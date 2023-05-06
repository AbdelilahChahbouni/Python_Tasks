# Countdown Calculator

# Function Convert Date Input From String To List Of Integer "10/12/2023" ==> [10 , 12 , 2023]
def convert_form_date(string):
    date = [int(dt) for dt in string.split("/")]
    return date

# TO Get Diffrence Between Days
def get_days(days1 , days2):
    if days1[0] > days2[0]:
        diff_days = days1[0] - days2[0]
    else:
        diff_days = days2[0] - days1[0]
    return diff_days

# To Get Diffrence Between Months 
def get_months(mon1 , mon2):
    if mon1[1] > mon2[1]:
        diff_mont = mon1[1] - mon2[1]
    else:
        diff_mont = mon2[1] - mon1[1]
    return diff_mont

# To Get Diffrence Between Years
def get_years(year1 , year2):
    if year1[2] > year2[2]:
        diff_years = year1[2] - year2[2]
    else:
        diff_years = year2[2] - year1[2]

    return diff_years

# The Main Function

def main():
    state = True
    while state:
        date1 = convert_form_date(input("Enter PLease Date 1 : (years/months/days) >> "))
        date2 = convert_form_date(input("enter Please Date 2 : (years/months/days) >> "))
        print(f"The Amount Between Dates Is {get_years(date1 , date2)} Years , {get_months(date1 , date2)} Months , {get_days(date1 , date2)} Days")

        state = input("You Want To Continue Enter yes or no To Quit : ")
        if state != "yes":
            state= False
            print("GoodBye ...")


main()




















