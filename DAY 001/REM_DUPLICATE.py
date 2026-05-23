#Write a program using a for loop to remove duplicate elements from a list while preserving order. Do not use set().

#input list
l = list(input())   # input of form 1 2 1 2 3 4 ... # l = list we wanna remove duplicates of

#create new list and store unique elements from l to this list
nl = []

#logic for unique element from list l
for i in range(len(l)):
    count = 0
    for k in range(0,i):
        if l[k]!=l[i]:
            count+=1
    if count==i:
        nl.append(l[i])       #element that never appeared before landed to new list

nl.remove(' ')        #remove space element
print(nl)           # we got a list of elements given in input (separated by a space)

