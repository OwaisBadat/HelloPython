
#conditions
# == is used to compare lhs with rhs - equality operator
if(1 == 2):
    print("Equal")
    a = 10
    b = 10
    c = a + b
else:
    print ("Not Equal")




#functions or methods
#age variable defined outside the function
age = 20

def validate_age(age):

    age = 10 #this is a brand new variable called age defined insie the validate_age function
    secret = "SOME SECRET"
    if(age >= 18):
        print("age is greater than 18")
    elif(age < 13):
        print("age is less than 13")
    else:
        print("age is not greater than and not less than 13")


validate_age(age)
print("The value of age is {0}".format(age))

#4
def even_or_odd(number):

    if(number % 2 == 0):
        print("EVEN")
    else:
        print("ODD")

even_or_odd(7)


#make = "Honda" is the default for make( DEFAULT MUST BE LAST parameter)
def display_car_info(model, make = "Honda"):
    print("----------")
    print("Make {0} - Model {1}".format(make,model))



def add(first_number, second_number):
    return first_number + second_number
    print("Hey what about me! ")


def greet(name,age):
    print ("Hello, " + name)


#display_car_info("Honda","Accord")

#explicityly specify the name of the parameter(ODER DOESNT MATTER HERE)
#display_car_info(model = "Accord", make = "Honda")

display_car_info(model = "Accord")



#greet("John",32)

#result = add(2,3)
#print(add(2,3))
#print (result)

#this is not th correct order to pass the arguement
#greet(32,"John")



#python
#indention is KEY
#def greet():
    #inside the function

#outside the function
