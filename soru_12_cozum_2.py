for t in range(1900,2100):

    toplam=0

    for rakam in str(t):

        toplam+=int(rakam) 

    if toplam==(2005-t):

        print(f"{t} yılında doğmuştur")