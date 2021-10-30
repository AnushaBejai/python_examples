num=int(input('enter the number:'))
n=num
sum=0
while (n>0):
    rem=int(n%10)
    n=int(n/10)
    sum=int(sum+(rem*rem*rem))
if (num==sum):
    print('the number %d is an armstrong number' %num)
else:
    print('the number %d is not armstrong number' %num)
