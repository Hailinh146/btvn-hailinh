
##outcome: Hello, my name is B-max
print("Hello", end="") 
print(", my name ", end="")
print("is B-max", end="")

print()
##outcome: ****************************************

for i in range(40):
    print('*', end="") 

print()

##outcome: x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*
for i in range(20):
    print("x*", end="")
    
print()

##outcome: x*x*x*x*x*
##outcome: *x*x*x*x*x
##outcome: x*x*x*x*x*

##outcome: *x*x*x*x*x
##outcome: x*x*x*x*x*
##outcome: *x*x*x*x*x
##outcome: x*x*x*x*x*
##outcome: *x*x*x*x*x
##outcome: x*x*x*x*x*
##outcome: *x*x*x*x*x

for i in range(5):
    for i in range(5):
        print("x*", end="")
    print()
    for i in range(5):
        print("*x", end="")
    print()
