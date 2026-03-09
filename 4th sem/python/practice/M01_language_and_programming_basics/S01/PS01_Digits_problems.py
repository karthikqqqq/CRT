''''
n = int(input())
count = 0
while n>0:
    count += 1
    n= n//10
print(count)

sample input : 1234
sample output: 10

n = int(input())
s = 0
while n>0:
    s += (n%10)
    n = n//10
print(s)

n = int(input())
while n>0:
    digit =n % 10
    if digit % 2 == 0:
        print(digit,end=" ")
    n = n // 10

n = reverse(int(input()))
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        print(digit,end= " ")
    n = n // 10
'''
n = int(input())
temp = reverse(n)

print(temp == n)

if temp == n:
    print(true)
else:
    print(False)

print(true) if temp == n else print 