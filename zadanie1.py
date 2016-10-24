# coding: utf-8

print u'Podaj liczbę naturalną większą od 1: '

def spr():
    tmp = raw_input()
    if tmp == '1':
        print u'Podałeś liczbę 1! Podaj liczbę naturalną większą od 1: '
        return spr()
    try:
        return int(tmp)
    except:
        print u'Niepoprawny typ danych! Podaj liczbę naturalną większą od 1: '
        return spr()

n = spr()
tab = []
for i in range(2, n+1):
    tab.append(i)

for i in tab:
    x = i + i
    while x <= n:
        if x in tab:
            tab.remove(x)
            x = x + i
        else:
            x = x + i

if n in tab:
    tab.remove(n)

print tab
