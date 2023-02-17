#Write A python program to take two numbers from the user and check whether number is divisible by both the numbers or not#
x=int(input("Enter the value whose divisibility is to be checked:"))
d1=int(input("Enter the first divisior:"))
d2=int(input("Enter the second divisior:"))
if (x%d1==0 and x%d2==0):
    print("YES")
else:
    print("NO")


