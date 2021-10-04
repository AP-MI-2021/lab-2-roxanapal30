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
'''
functia get_perfect_squares(n, m) cauta si afiseaza toate patratele perfecte din intervalul [n,m]
'''

def get_perfect_squares(n, m):
    patrateperf=[]
    shouldRun=True
    i=1
    while shouldRun:
       i=i+1
       if i*i>m:
            shouldRun=False
       if i*i>=n:
           if i*i<=m:
            patrateperf.append(i*i)

    return patrateperf

def test_get_largest_prime_below():
    assert get_largest_prime_below(9) == 7
    assert get_largest_prime_below(1) == 0
    assert get_largest_prime_below(15) == 13

def test_is_antipalindrome():
    assert is_antipalindrome(121) is True
    assert is_antipalindrome(123) is False
    assert is_antipalindrome(1245) is False

def test_get_perfect_squares():
    assert get_perfect_squares(2, 9) == [4,9]
    assert get_perfect_squares(1, 5) == [4]
    assert get_perfect_squares(13, 40) == [16,25,36]

def main():
    test_get_largest_prime_below()
    test_is_antipalindrome()
    test_get_perfect_squares()
    shouldRun=True
    while shouldRun:
        print("1.Determinare cel mai mare nr. prim mai mic decat cel dat")
        print("2.Verificare nr. palindrom")
        print("3.Cautare si afisare patrate perfecte din intervalul inchis dat")
        print("4.Iesire")
        optiune=int(input("Dati optiunea:(1, 2, 3 sau 4)"))
        if optiune==1:
            n = int(input("Dati nr.:"))
            print(get_largest_prime_below(n))
        if optiune==2:
            n=int(input("Dati nr:"))
            if is_antipalindrome(n) == True:
                print("este palindrom")
            else:
                print("nu este palindrom")
        if optiune==3:
            n = int(input("Dati nr1.:"))
            m = int(input("Dati nr2.:"))
            print(get_perfect_squares(n, m))
        if optiune==4:
            shouldRun=False

main()