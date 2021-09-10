# Função check_palindrome
def check_palindrome(string):
    w = ""
    for i in string:
        w = i + w
    if (string == w):
        print('É palíndrome')
        return True
    else:
        print('Não é palíndrome')
        return False



# Função check_palindrome até metade da string
def check_palindrome2(string):
    for i in range(0, int(len(string)/2)):
        if string[i] != string[len(string)-i-1]:
            print('Não é palíndrome')
            return False
    print('É palíndrome')
    return True

check_palindrome(input('Digite a palavra que você quer testar: '))