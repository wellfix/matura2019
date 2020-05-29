plik = open("liczby.txt").read().split()
counter = 0
for x in plik:
    x = int(x)
    if x == 1:
        counter=counter+1
        continue
    elif x%3 != 0:
        continue
    else:
        while True:
            if x == 3:
                counter= counter+1
                break
            elif x%3 == 0:
                x=x/3
            else:
                break
print(counter)




