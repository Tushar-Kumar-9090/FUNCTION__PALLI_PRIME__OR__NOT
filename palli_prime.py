
# ## Pally Prime or not

def isPallindrom(n):
    num=n
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if num==rev:
        return True
    else:
        return False


def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False

def isPallyprime(n):
    if isPallindrom(n):
        if isPrime(n):
            return True
        else:
            return False
    else:
        return False

def PallyprimeNumber(ll,ul):
    for i in range(ll,ul+1):
        if isPallyprime(i):
            print(i)
PallyprimeNumber(10,500)