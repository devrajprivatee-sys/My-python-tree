#Write a program using a while loop to check whether a number is a palindrome without using string conversion.

# capture digits > store in a list in order > check if order remains same even when list is reversed

n = int(input())
l = [] 
d = 10 #divisor
while n//(d//10) != 0:
    l.append( (n%d)//(d//10) )   #each digit stored in list but reversed order i.e. ones place then tenth then hundreth ( R TO L )
    d*=10

if l==l[::-1]:
    print('PALINDROME')
else:
    print("NOT A PALINDROMIC NUMBER")
