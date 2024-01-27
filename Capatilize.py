#   `Get a list of name as an input from the user and make the first letters in caps and print each word as a list.


l=[] #here l declare as list.
for a in range (1,4):
 n =input("Enter the value"+str(a)+":-")
 #n.capitalize()
 # n.capitalize() --> This code is  executable with below code of line but  this is not executible separately . why??
 l.append(n.capitalize())

print(l)