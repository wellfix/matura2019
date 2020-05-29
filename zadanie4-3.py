def nwd(a, b):
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a

dzielnik = 1
dlg = 1
maxlen = 0
pierwsza = 0
dzielniczek = 0
plik = open("liczby.txt").read().split()
try:
    for i, x in enumerate(plik):
        x = int(x)
        y = int(plik[i + 1])
        z = int(plik[i-1])
        if nwd(dzielnik, x) > 1:
            dlg = dlg + 1
            dzielnik = nwd(dzielnik, x)
        else:
            if maxlen <= dlg:
                maxlen = dlg
                pierwsza = int(plik[i - dlg])
                dzielniczek = dzielnik
            dlg = 1
            if nwd(nwd(z,x), nwd(x,y)) > 1:
                dlg = 2
                dzielnik = nwd(nwd(z,x), nwd(x,y))
            else:
                dzielnik = nwd(x, y)
except:
    pass

print(str(maxlen)+" "+str(pierwsza)+" "+str(dzielniczek))