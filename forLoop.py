# print 4*4 * Matrix

# <editor-fold desc="Commented">
i = 1

while i < 5:
    print ("*", end="")
    j = 1
    while j < 4:
        print(" *", end="")
        j += 1
    i += 1
    print()
print ("Exit !!")
# </editor-fold>


#Other way of doing it.
#range(start, stopping, steps),
# start and steps are optional.it starts with '0'

for i in range(4):
    for j in range(4):
        print("* ", end="")

#for k in range(10,21):
#for a in range(20,11,-1):  to print in reverse order