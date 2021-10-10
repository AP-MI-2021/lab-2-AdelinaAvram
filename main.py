def isPrime (n):
    '''
    determina daca x este numar prim
    :param x: nr. intreg
    :return: True daca x e prim si False daca nu este
    '''
    if n<2:
        return False
    if n==2:
        return True
    div = 2
    while div*div<=n:
        if n%div==0:
            return False
        div=div+1
    return True

def testisPrime():
    assert isPrime(-1) is False
    assert isPrime(0) is False
    assert isPrime(1) is False
    assert isPrime(2) is True
    assert isPrime(3) is True
    assert isPrime(4) is False
    assert isPrime(5) is True

def get_largest_prime_below(n):
    '''
    determina ultimul nr prim mai mic decat x
    :param x: nr intreg
    :return: ultimul nr prim mai mic decat x
    '''
    if isPrime(n)==True:
        n=n-1
        while isPrime(n)==False:
            n=n-1
        return n
    else:
        while isPrime(n)==False:
            n=n-1
        return n

def test_get_largest_prime_below():
    assert get_largest_prime_below(10) == 7
    assert get_largest_prime_below(33) == 31
    assert get_largest_prime_below(3) == 2
    assert get_largest_prime_below(13) == 11
    assert get_largest_prime_below(54) == 47


def is_palindrome(n):
    '''
    verifica daca un numar este palindrom
    :param n: nr intreg
    :return: True, daca n e palindrom si False, in caz contrar
    '''
    ogl = 0
    copie = n
    while n!=0:
        ogl = ogl*10 + n%10
        n = n//10
    if copie==ogl:
        return True
    return False

def test_is_palindrome():
    assert is_palindrome(27) is False
    assert is_palindrome(1551) is True
    assert is_palindrome(12321) is True
    assert is_palindrome(235555) is False
    assert is_palindrome (0) is True

while True:
    print("1. Determinati cel mai mare numar prim mai mic decat un numar dat.")
    print ("2. Verificati daca un numar este palindrom")
    print ("x. Iesire")

    optiune = input ("Dati optiunea: ")

    if optiune == "1":
        n = int(input ("Dati nr.: "))

        print (get_largest_prime_below(n))

    elif optiune == "2":
        n = int(input ("Dati nr.: "))

        print (is_palindrome(n))

    elif optiune == "x":
        break

    else:
        print("Optiune gresita. Reincercati!")
