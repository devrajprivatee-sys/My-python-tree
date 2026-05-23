#Write a program to count the frequency of each character in a string using a for loop and a dictionary.

s = input()    #string input
d = {}
l = list(s)    #storing each char as list item

for i in range(len(l)):       #loop to get each char in string
    count =0
    for k in range(0,i):        #loop to make sure characters are uniquely used not repeated
        if l[i]!=l[k]:
            count+=1

    if count==i:
        d[l[i]]=1
        for j in range(i+1,len(l)):        #gets the char count and stores it in dictionary key value
            if l[j]==l[i]:
                d[l[i]]+=1

# d is dictionary containing counts but it is random 
# we got the dictionary containing count of each char but we want to show it in ascending order instead of random




b =[]
for i in d:
    b.append(i)             # keys of answer dictionary stored in list

b.sort()        #sorted keys (ASCII order)
for i in b:
    print( f'count of {i} is {d[i]}')  #print character and its count in input string usinf f-string
