#Write a program to reverse a number using a while loop (e.g., 1234 → 4321). Do not convert to string.

#take input
n = int(input())

# append individual digit into a list
l = []

#digits logic
d=10
while n//(d//10) !=0:
    l.append( (n%d)//(d//10) )  #digits stored into list , order is reverse
    d*=10

#print reversed number using membership operator
for i in l:
    print(i,end='')

# Now using strings
# a = str(n)
# b = a[::-1]
# for i in b:
#    print(i, end='')
