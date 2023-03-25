#Program To Take Details Of The Person(Name,Company name,Designation)
try:
    name=str(input("Enter your Name:"))
    company_name=str(input("Enter your Company Name:"))
    designation=str(input("Enter your Designation:"))
    #output statement 
    message=f"Hey There ! My name is {name} . I work for {company_name} and I am a {designation}."
    print(message)
except Exception as e:
        print("An Error occured",e)
    