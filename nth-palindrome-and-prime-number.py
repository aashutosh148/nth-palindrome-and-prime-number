def ispalindrome(num):
    x=num
    reverse=0
    while(x!=0):
        digit=x%10
        reverse=reverse*10+digit
        x=x//10
    if num==reverse:
        return True
    else:
        return False
def isprime(n):
    x=True
    for i in range(2,n):
        if(n%i==0):
            x= False
            break
    return x
n=int(input("Give Nth value:"))
primeAndPalindrome=[]
for i in range (2,100000):
    if ispalindrome(i) and isprime(i):
        primeAndPalindrome.append(i)
    if len(primeAndPalindrome)==n+10:
        break
print(primeAndPalindrome[n-1])
        
    
