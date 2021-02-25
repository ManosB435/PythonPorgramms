import random
x = int(input('ΕΙΣΑΓΕΤΕ ΤΟΝ ΟΡΟ ΑΚΟΛΟΥΘΙΑΣ FIBONACCI ΠΟΥ ΘΕΛΕΤΕ:'))


def Fibo(x):
    if x<0:
        print('incorrect input')
    elif x == 0:
        return 0
    elif x==1 or x==2:
        return 1
    else:
        return Fibo(x-1)+Fibo(x-2)

c=Fibo(x)

print('Η ΤΙΜΗ ΤΟΥ ΟΡΟΥ ΠΟΥ ΕΠΙΛΕΞΑΤΕ ΕΙΝΑΙ:', c)
w = 0
if x == 0 or x == 2 or x == 1 or x == 3:
    print('ΤΟ',c, 'ΔΕΝ ΕΙΝΑΙ ΠΡΩΤΟΣ')
else:
    for i in range(0, 20):

        a = random.randint(1, c-1)

        if (a ** (c-1) - 1) % c == 0:
            w += 1
    if w == 20:
        print(c, 'ΕΙΝΑΙ ΠΡΩΤΟΣ')
    else:
        print(c, 'ΔΕΝ ΕΙΝΑΙ ΠΡΩΤΟΣ')