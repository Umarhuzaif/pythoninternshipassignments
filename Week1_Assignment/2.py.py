#Program To Perform Airthmetic Opertaions(+,-,*,/)
def math_op(Firstnumber,Secondnumber):
    #addition opertaion
    Addition=Firstnumber + Secondnumber
    print(f"{Firstnumber}+{Secondnumber}={Addition} ")
    #substraction operation
    Substraction=Firstnumber - Secondnumber 
    print(f"{Firstnumber}-{Secondnumber}={Substraction} ")
    #multplication operation
    Multiplication=Firstnumber*Secondnumber
    print(f"{Firstnumber}*{Secondnumber}={Multiplication}")
    #Division Operation
    Division=Firstnumber/Secondnumber 
    print(f"{Firstnumber}/{Secondnumber}={Division}")
try:
    Firstnumber=float(input("Enter the First Number:"))
    Secondnumber=float(input("Enter the Second Number:"))
    math_op(Firstnumber,Secondnumber) #function call
except ValueError:
 print("Error:Enter Only Numeric Values!")
except ZeroDivisionError:
 print("Error:Division by Zero")    
 





 