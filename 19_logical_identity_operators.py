# Initialize x with the value 5
x = 5 	
y = 5

z = [0, 1, 2, 3, 4, 5]

aString = "jane"
strings = ["jane", "jone"]

print(x < 5 and  x < 10) #and -Returns True if both statements are true 		
print(x < 5 or x < 4) 	 #or 	Returns True if one of the statements is true 	
print(not(x < 5 and x < 10)) #not 	Reverse the result, returns False if the result is true 	

print(x is y) #is  	Returns True if both variables are the same object 	 	
print(x is not y) #is not 	Returns True if both variables are not the same object 

print(x in z)  #in  	Returns True if a sequence with the specified value is present in the object
print(x not in z)  #not in 	Returns True if a sequence with the specified value is not present in the object

print(aString in strings)  #in  	Returns True if a sequence with the specified value is present in the object
print(aString not in strings)  #not in 	Returns True if a sequence with the specified value is not present in the object

# INSTRUCTIONS FOR TESTING
# 1. Launch your terminal and run the code
# 2. Run the code -> python 19_logical_identity_operators.py