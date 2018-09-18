
#string concatention

print ("Hello")

first_name = input("Enter first name: ")
last_name = input("Enter Last Name: ")
city = input("Enter city: ")
state = input("Enter state: ")
zip_code = input("Enter zip code: ")


#My name is first_name, last_name and I live in city, state zip_code
#message = "My name is " + first_name + ", " + last_name + " and I live in " + city + ", " + state + " " + zip_code

#string interpolation(best way to concatenate)
message = "My name is {0}, {1} and I live in {2}, {3} {4}".format(first_name, last_name, city, state, zip_code)

print(message)










#name = input("Enter your name: ")


#snake case = first_numnber (underscore)
#camel case = firstNumber

#input function ALWAYS returns string data type
# convert string into interger
#first_number = int(input("Enter first number: "))
#second_number = int(input("Enter second number: "))

#int function converts string to interger
#number = int("45")

#first_number_as_int = int("45")
#second_number_as_int = int("70")


#result = first_number + second_number
#print (result)

#name = "John"
#age = 20
#ersion = 3.45

# print will print the value of the name variable onto the screen
#print(name)

#name = "Mary"

#print (name)
