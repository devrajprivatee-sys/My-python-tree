# Write a program to print all prime numbers between 1 and 100 using while loop (no for loop allowed).


#function to check if a number is prime or not
def prime(n):
    i = 2
    while i<n:
        
        if n%i!=0:
            pass
        else:
            return False
        i+=1
        
    return True

# input range (count from 1 to ?)
n = int(input())

#loop to print primes <=n
j = 2
while j<=n:
    if prime(j):
        print(j , end=' ')
    j+=1


    
