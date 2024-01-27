# Take the integer as an input and reverse the integer.

#Two cases arises:
#(1) take integer as string and reverse it .
#(2) take integer as list and reverse it.

# 1.

'''str=" "
str=input("Enter the value")
new_string=str[::-1]#
print(new_string) '''

#2.

lis=[]
for a in range (5):
  n =input("enter integer value")
new=lis.append(n)
# revers=new[::-1]
newlis=[]
for i in range (len(new)):
    newlis.append(new[-i])
print(newlis)


# or

#3.

num=int(input("Enter the number:   "))
sum=0
while num>0:
  rem=num%10
  sum=(sum*10)+rem
  num=num//10

print(sum)