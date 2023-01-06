with open("strawbery.txt","r") as file:
    my_list=[[],[],[]]
    sen=[]
    for line in file:
        replaced=line.replace(",","")
        replaced=replaced.replace('"','')
        replaced=replaced.replace("...","")
        replaced=replaced.replace('',"")
        stripped=replaced.strip()
        splitted=stripped.split(" ")
        splitted.append(" ")
        sen.append(splitted)
    result=[]
    for deger in range(len(sen)):
        for sayi in range(len(sen[deger])):
            if sen[deger][sayi]!=' ' and sen[deger][sayi]!='':
                result.append(sen[deger][sayi])
    sonuclar=[[],[],[]]

    for kelime in range(len(result)):
        if len(result[kelime])==2:
            if len(result[kelime-1])==2:
                if len(result[kelime+1])==2:
                    sonuclar[0].append(f"{result[kelime-1].upper()}, {result[kelime].upper()}, {result[kelime+1].upper()}")
        elif len(result[kelime])==3:
            if len(result[kelime-1])==3:
                if len(result[kelime+1])==3:
                    sonuclar[1].append(f"{result[kelime-1].upper()}, {result[kelime].upper()}, {result[kelime+1].upper()}")
        elif len(result[kelime])==4:
                if len(result[kelime-1])==4:
                    if len(result[kelime+1])==4:
                        sonuclar[2].append(f"{result[kelime-1].upper()}, {result[kelime].upper()}, {result[kelime+1].upper()}")

    for eleman in range(len(sonuclar)):
        for char in range(len(sonuclar[eleman])):
            print(sonuclar[eleman][char])
