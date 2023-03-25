#program to find Largest of 5 numbers 
try:
      while True:
        numbers=(input("Enter the number:"))
        numbers.append(numbers)
        print(f"Maximum number among given input is :{max(numbers)}")
except ValueError:
    print("Give the Input in Numeric form!")        