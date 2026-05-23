#Write a program using a for loop to flatten a nested list [[1,2],[3,4],[5]] → [1,2,3,4,5]. Do not use any built-in flatten method.

#flatten a
a = [1,[2],[[3]],[[[4]]],[[[[5]]]],[[[[[6,7]]]]]]

#logic flatten each element list of a and store it in a new list which then gives falttened a 
nl = []

#func to flatten an element disc
def flat(l):
    while type(l[0])==list:
        l = l[0]
    return l

# loop for nested lists
for i in a[:]:
    if type(i)==list:
        nl = nl + flat(i)
        a.remove(i)            # a now is a flattened list but missing elements which are stored in nl

#final  flattened list
a = a + nl

print(a)            # done and dusted
