__author__ = 'garywhite'

n = input('Enter a number: ')
n = float(n)
for i in range(1, 11):
    print('{0} x {1} = {2:.2f}'.format(n, i, n * i))
