# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#   print("this is function")
#   print("this is greet function")
#   print("this call from outside")

# greet()

def greet_with(name,location):
  print(f"Hello {name}")
  print(f"what is it like in {location}")

greet_with('yuvraj','mumbai')

greet_with(location='mumbai',name='yuvraj')