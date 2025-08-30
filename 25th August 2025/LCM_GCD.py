a=int(input("Enter your Number"))
b=int(input("Enter next number"))
x,y=a,b
while y!=0:
    x,y= y, x%y
gcd=x
lcm=abs(a*b)//gcd
print([lcm,gcd])
