# -*- coding:utf-8 -*-
Main_Loop = 1

def sesliHarfKontrol(harf):
    if harf == "a" or harf == "e" or harf == "ı" or harf == "i" or harf == "o" or harf == "ö" or harf == "u" or harf == "ü":
        return True
    else:
        return False

while Main_Loop == 1:
    kelime_listesi = []
    kelime_listesi_2 = []
    harf_listesi = []
    hece_listesi = []
    cumle = input("Hecelere ayırmak istediğini cümleyi giriniz:")
    if cumle == "çıkış":
        break
    cumle = cumle.lower()
    print(cumle)
    kelime_listesi = cumle.split()
    kelime_listesi_2 = cumle.split()
    for x in kelime_listesi_2:
        kelime_listesi.append(x)
        kelime_listesi.append(" ")
    kelime_listesi.pop()
    for x in kelime_listesi:
        for a in range(len(x)):
            t = a + 1
            if t > len(x):
                harf_listesi.append(x[a:])
            else:
                harf_listesi.append(x[a:t])
    for x in range(len(harf_listesi)):
        if harf_listesi[x] == " ":
            hece_listesi.append(" ")
        elif x == 0 or harf_listesi[x-1] == " ":
            if sesliHarfKontrol(harf_listesi[x]) == True:
                try:
                    if sesliHarfKontrol(harf_listesi[x+2]) == True:
                        hece_listesi.append(harf_listesi[x])
                    elif sesliHarfKontrol(harf_listesi[x+1]) == True:
                        hece_listesi.append(harf_listesi[x])
                    else:
                        try:
                            if sesliHarfKontrol(harf_listesi[x + 3]) == True:
                                hece_listesi.append(harf_listesi[x] + harf_listesi[x + 1])
                            else:
                                hece_listesi.append(harf_listesi[x] + harf_listesi[x + 1] + harf_listesi[x + 2])
                        except:
                            hece_listesi.append(harf_listesi[x]+harf_listesi[x+1]+harf_listesi[x+2])
                except:
                    try:
                        if sesliHarfKontrol(harf_listesi[x+1]) == True:
                            hece_listesi.append(harf_listesi[x])
                        else:
                            hece_listesi.append(harf_listesi[x]+harf_listesi[x+1])
                    except:
                        hece_listesi.append(harf_listesi[x])
            else:
                try:
                    if sesliHarfKontrol(harf_listesi[x+1]) == True:
                        try:
                            if sesliHarfKontrol(harf_listesi[x+2]) == True:
                                try:
                                    if sesliHarfKontrol(harf_listesi[x+3]) == True:
                                        hece_listesi.append(harf_listesi[x]+harf_listesi[x+1])
                                    else:
                                        try:
                                            if sesliHarfKontrol(harf_listesi[x+4]) == True:
                                                hece_listesi.append(harf_listesi[x]+harf_listesi[x+1]+harf_listesi[x+2])
                                            else:
                                                hece_listesi.append(harf_listesi[x]+harf_listesi[x+1]+harf_listesi[x+2]+harf_listesi[x+3])
                                        except:
                                            hece_listesi.append(harf_listesi[x]+harf_listesi[x+1])
                                            hece_listesi.append(harf_listesi[x+2]+harf_listesi[x+3])
                                except:
                                    random_variable_for_else_func = 1
                            else:
                                try:
                                    if sesliHarfKontrol(harf_listesi[x + 3]) == True:
                                        hece_listesi.append(harf_listesi[x] + harf_listesi[x + 1])
                                    else:
                                        try:
                                            if sesliHarfKontrol(harf_listesi[x + 4]) == True:
                                                hece_listesi.append(harf_listesi[x] + harf_listesi[x + 1] + harf_listesi[x + 2])
                                            else:
                                                hece_listesi.append(harf_listesi[x] + harf_listesi[x + 1] + harf_listesi[x + 2] + harf_listesi[x + 3])
                                        except:
                                            hece_listesi.append(harf_listesi[x] + harf_listesi[x + 1] + harf_listesi[x + 2] + harf_listesi[x + 3])
                                except:
                                    hece_listesi.append(harf_listesi[x] + harf_listesi[x + 1] + harf_listesi[x + 2])
                        except:
                            hece_listesi.append(harf_listesi[x] + harf_listesi[x + 1])
                    else:
                        hece_listesi.append(harf_listesi[x])
                except:
                    hece_listesi.append(harf_listesi[x])
        else:
            if sesliHarfKontrol(harf_listesi[x]) == False:
                try:
                    if sesliHarfKontrol(harf_listesi[x+1]) == True:
                        try:
                            if sesliHarfKontrol(harf_listesi[x+2]) == True:
                                hece_listesi.append(harf_listesi[x]+harf_listesi[x+1])
                            else:
                                try:
                                    if sesliHarfKontrol(harf_listesi[x+3]) == True:
                                        hece_listesi.append(harf_listesi[x] + harf_listesi[x + 1])
                                    else:
                                        hece_listesi.append(harf_listesi[x] + harf_listesi[x + 1] + harf_listesi[x + 2])
                                except:
                                    hece_listesi.append(harf_listesi[x] + harf_listesi[x + 1]+harf_listesi[x+2])
                        except:
                            hece_listesi.append(harf_listesi[x] + harf_listesi[x + 1])
                    else:
                        random_variable_for_else_func = 1
                except:
                    random_variable_for_else_func = 1

    print(hece_listesi)

