def sum(a,b,c):
    sum=a+b+c
    if a==b==c:
        sum = sum*3
    return sum

x=int(input('Enter No.1'))
y=int(input('Enter No.2'))
z=int(input('Enter No.3'))
print(sum(x,y,z))