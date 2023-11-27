## intro examples
# basic printing
print("Whatcha got now?")
# print with concatenate
print("Whatcha got "+"right now"+"!?")
# example with ''
print("The so-called 'currency'.")

# input - make sure running in Terminal 
# with project path % python <filename>
# NOT just running here - will appear in Output pane but no interactivity
# OR...Run dropdown:
#  Run in Dedicated Terminal
#  Run in Interactive Window (requires pkg)
# demo input - nothing happens
input("Hey, what is your name, anyway? ")
# input saved as variable
yname = input("name please: ")
# print results from input
print("hello "+yname+" mucho gusto!")

## BAND NAME GENERATOR
town = input("what town did you grow up? ")
pet = input("what your favorite pet name? ")
print("Here are some band name suggestions:\n")
print(town+" "+pet)
print(town+" "+pet+"s")
print(pet+" "+town)
print(pet+" "+town+"s")

## len, subsets
print("town has this many letters: "+str(len(town)))
print("the second letter is "+town[1])

## types
print("Provide some variables and I will tell you what type they are: \n")
input_var_01 = input("variable integer: ")
input_var_02 = input("variable float: ")
input_var_03 = input("variable string: ")
input_var_04 = input("last one: bool: ")
input_var_01 = int(input_var_01)
input_var_02 = float(input_var_02)
#input_var_03 = str(input_var_03) # not needed - default str
input_var_04 = bool(input_var_04)
print("variable 1: "+str(type(input_var_01)))
print("variable 2: "+str(type(input_var_02)))

print("variable 3: "+str(type(input_var_03)))
print("variable 4: "+str(type(input_var_04)))
# chg variable types is easy:
# - to string
# str(var)
# - to integer
# int(var)
# - to float
# float(var)





