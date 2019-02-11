#find if a given number is Odd r Even.
x = int(input("Enter a number"))
r = x % 2

if r == 0:
    print("Even")
    if x > 5:
        print(" and Greater than 5")
    else:
        print("and Not greater than 5")
else:
    print("Odd")

print ("Bye !!")