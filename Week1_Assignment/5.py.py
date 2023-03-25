#program to find that Input number is divisible by 5 and 25 but not 50
def input_num(number):
    if number % 5==0 and number %25 ==0 and number % 50 !=0:
        print(f"Given {number} is Divisile by 5 and 25 but not by 50")
    else:
        print(f"Given {number} is not Divisible by 5 and 25 or is divisible by 50")    
try:
    number=int(input("Enter the number:"))
    input_num(number)
except ValueError:
    print("Error:Only Enter the Numeric Values")
