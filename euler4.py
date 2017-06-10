'''Largest palindrome product
Problem 4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.'''


def euler4():
    start=999
    final= 100
    max=0
    for j in range (start,final,-1):
        for n in range(j,final,-1):
            product= n * j
            numberWord=str(product)
            end = len(numberWord)-1
            i=0
            while i<=len(numberWord)/2 and (numberWord[i]==numberWord[end]):
                i+=1
                end-=1
                if i-1 == (len(numberWord))/2:
                    max = int(numberWord)
                    return max



print(euler4())

print ("done")
