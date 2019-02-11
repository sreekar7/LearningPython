# Simple demonstration on while loop

i,j = 1,1

while i < 5:
    print("hello ", end="") # end="" will stays on the same line
    j = 1
    while j < 4:
        print("Srikar ", end="")
        j += 1

    i += 1;
    print() #Simply prints the newline