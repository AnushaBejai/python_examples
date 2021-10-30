n=int(input('Enter the number:'))
rev=0
while (n!=0):
    rem=int(n % 10)
    n=int(n / 10)
    rev=int(rev * 10 + rem)
print(rev)
