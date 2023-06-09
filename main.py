size = 7

#Top row
for i in range(size):
    print("*" , end=" ")
print()

#Middle row
for i in range(size - 2):
    print("*" , end=" ")
    for j in range(size - 2):
        print(" " , end="")
    print("     *")

#Bottom row
for i in range(size):
     print("*" , end=" ")

