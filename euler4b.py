
def ispalindrome(string):
	decide=1
	i=0
	while i<=int(len(string)/2) and isPal==1:
		if string[i]!=string[-(i+1)]:
			isPal=0
		i+=1
	return isPal

if __name__=='__main__':
    aux=0
    for k in range(101,1000):
	    for j in range(101,1000):
		    if ispalindrome(str(j*k)) and j*k>aux:
			    aux=j*k
    print (aux)
