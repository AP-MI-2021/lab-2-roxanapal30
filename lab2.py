'''
fucntia get_largest_prime_below returneaza cel mai mare nr prim mai mic decat cel dat
'''
def get_largest_prime_below(n):
    shouldRun=True
    cmmnr=n-1
    while shouldRun:
        if cmmnr<2:
            shouldRun = False
            return 0
        if cmmnr==2:
            shouldRun = False
            return 2
        if cmmnr==3:
            shouldRun = False
            return 3
        nrdiv=0
        for d in range (2,cmmnr//2+1):
            if cmmnr%d==0:
               nrdiv=nrdiv+1
        if nrdiv==0:
           shouldRun=False
        else:
            cmmnr=cmmnr-1
    return cmmnr
'''
fucntia is_antipalindrome verifica daca numarul dat este palindrom
'''
def is_antipalindrome(n):
    shouldRun=True
    d=0
    oknrpalindrom=0
    while shouldRun:
       d=d*10+n%10
       n=n//10
       if d == n :
           shouldRun=False
           oknrpalindrom=1
       elif d*10+n%10==n:
           shouldRun=False
           oknrpalindrom=1
       if d>n:
           shouldRun=False
    if oknrpalindrom==1:
        return True
    else:
        return False

def test_get_largest_prime_below():
    assert get_largest_prime_below(9) == 7
    assert get_largest_prime_below(1) == 0

def test_is_antipalindrome():
    assert is_antipalindrome(121) is True
    assert is_antipalindrome(123) is False

def main():
    test_get_largest_prime_below()
    test_is_antipalindrome()
    n=int(input("Dati nr.:"))
    get_largest_prime_below(n)
    print(get_largest_prime_below(n))
    if is_antipalindrome(n) ==True:
        print("este palindrom")
    else:
        print("nu este palindrom")

main()