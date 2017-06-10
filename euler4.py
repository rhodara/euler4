'''Largest palindrome product
Problem 4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 √ó 99.
Find the largest palindrome made from the product of two 3-digit numbers.'''

def isPalindrome(numberWord):
    end = len(numberWord)-1
    i=0
    isPal=1
    while (i<=len(numberWord)/2) and (isPal==1):
        if (numberWord[i]!=numberWord[end]):
            isPal = 0
        i+=1
        end-=1
    return isPal
	

def euler4():
    start=999
    final= 100
    max=0
    for j in range (start,final,-1):
        for n in range(j,final,-1):
            product= n * j
            numberWord=str(product)
            if (isPalindrome(numberWord)):
                nWord = int(numberWord)
                if nWord >max:
                    max = nWord
    return max
print(euler4())