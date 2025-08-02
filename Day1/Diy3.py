'''
Ather = input("What is your name? ")
print(Ather)
print("Hello " + Ather + " Your Name Lenghth is: " + str(len(Ather)))
#Another way to do this
print(f"Hello {Ather} Your Name Lenghth is: {len(Ather)}")
#Another way to do this
print("Hello {} Your Name Lenghth is: {}".format(Ather, len(Ather)))
#Another way to do this
print("Hello {0} Your Name Lenghth is: {1}".format(Ather, len(Ather)))
#Another way to do this
print("Hello {name} Your Name Lenghth is: {length}".format(name=Ather, length=len(Ather)))
'''
anyString=input("Enter a string \n")
Length=len(anyString)
print(type(Length))