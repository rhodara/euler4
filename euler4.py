'''Largest palindrome product
Problem 4 
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.'''


def euler4():
    num1=999
    num2=999
    final= int(num1/2)
    max=0
    nWord=0
    for j in range (num2,final,-1):
        for n in range(j,final,-1):
            product= n * j
            #print(product)
            numberWord=str(product)
            end = len(numberWord)-1
            palindrome=True
            i=0
            while i<=len(numberWord)/2 and (numberWord[i]==numberWord[end]):
                #print (numberWord[i],numberWord[end])
                i+=1
                end-=1
            if i-1 == (len(numberWord))/2:
                print (numberWord)
                palindrome=True
                nWord = int(numberWord)
                if nWord >max:
                    max = nWord
    return max

       
    
print(euler4())

print ("done")