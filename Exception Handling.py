a = 10

try:
    k = int(input("Please Enter the number"))
    print(a/k)
    print("Resource open")

except ValueError as e:
    print("Invalid input")

except ZeroDivisionError as e:
    print("You can't devide the number with zero")

except Exception as e:  # handles all the other errors
    print("Got an exception")

finally:
    print("Resource Closed")
