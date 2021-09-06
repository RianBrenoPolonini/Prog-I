ordem = list(map(int, input().split()))

if ordem == sorted(ordem):
    print('C')
elif ordem == sorted(ordem, reverse=True):
    print('D')
else:
    print('N')
