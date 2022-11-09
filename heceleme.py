# -*- coding:utf-8 -*-
kelime = input("Hecelerine ayırmak istediğiniz kelimeyi giriniz:")    
kelime = kelime.lower()
kelime = kelime.splitlines()
def hecelere_ayir(kelime):
    i = 0
    sesli_harf = "aeıioöuü"
    sessiz_harf = "bcçdfgğhjklmnprsştvyz"
    while i < len(kelime):
        if kelime[i] in sesli_harf:
            if i + 1 < len(kelime) and kelime[i+1] in sesli_harf:
                return kelime[0:i+1] + "-" + hecelere_ayir(kelime[i+1:len(kelime)])
            elif i + 2 < len(kelime) and kelime[i+2] in sesli_harf:
                return kelime[0:i+1] + "-" + hecelere_ayir(kelime[i+1:len(kelime)])
            elif i + 3 == len(kelime) and kelime[i+1] in sessiz_harf and kelime[i+2] in sessiz_harf:
                return kelime[0:i+3] + "-" + hecelere_ayir(kelime[i+3:len(kelime)])
            elif i + 3 < len(kelime) and kelime[i+3] in sesli_harf:
                return kelime[0:i+2] + "-" + hecelere_ayir(kelime[i+2:len(kelime)])
            elif i + 3 < len(kelime) and kelime[i+1] in sessiz_harf and kelime[i+2] in sessiz_harf and kelime[i+3] in sessiz_harf:
                return kelime[0:i+3] + "-" + hecelere_ayir(kelime[i+3:len(kelime)])
            else:
                return kelime[0:i+3] + "-" + hecelere_ayir(kelime[i+3:len(kelime)])
        else:
            i += 1
    return kelime

for i in kelime:
    print(hecelere_ayir(i))
    