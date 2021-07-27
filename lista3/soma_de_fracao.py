n = list(map(int, input().split()))

def mdc(n1,n2):
    for i in range(max(n1,n2),0,-1):
        if n1 % i == 0 and n2 % i == 0:
            return i

mdc = mdc(n[1]*n[3], (n[1]*n[2])+(n[3]*n[0]))
print(f'{int((((n[1]*n[2])+(n[3]*n[0])) / mdc))} {int((n[1]*n[3])/ mdc)}')
