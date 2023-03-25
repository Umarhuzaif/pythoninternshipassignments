#program to check call by value and call by referenece
def take_info(name,age):
    try:
        print("Name:",name)
        print("Age:",age)
        return name,age
    except Exception as e:
        print("Error Occured",e)
try:
    name ,age=take_info("Umar",20)
    print("Name and Age are:",name,age)
except Exception as e:
    print("Error Occured",e)
        