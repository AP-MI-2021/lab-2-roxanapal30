# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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

def test_get_largest_prime_below():
    assert get_largest_prime_below(9) == 7

def main():
    test_get_largest_prime_below()
    n=int(input("Dati nr.:"))
    get_largest_prime_below(n)
    print(get_largest_prime_below(n))

main()