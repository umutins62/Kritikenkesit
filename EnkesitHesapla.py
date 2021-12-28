# -*- coding: utf-8 -*-
while True:
    from math import sqrt
    from dxfwrite import DXFEngine as dxf
    from dxfwrite.dimlines import dimstyles, LinearDimension
    print("")
    print("*********** DERE KESİT HESABI ***********\n")
    print("Dere kesit hesap programına hoşgeldiniz.\n\nn=Pürüzlülük Katsayısı\nQ100=100 Yıl İçinde geçebilecek maksimum debi\nQ500=500 Yıl İçinde geçebilecek maksimum debi\nÇ=Islak çevre\nR=Hidrolik yarıçap\nJ=Eğim\nA=Alan\nQ=Dereden geçen maksimum debi\n\nLütfen aşağıda istenen bilgileri doğru giriniz.\n")
    print("Programdan çıkmak isterseniz 'q' tuşuna basınız.\n")
    niste = input("n Pürüzlülük katsayısını biliyormusunuz? E,H :\n")

    if (niste == 'E' or niste == 'e'):
        n = float(input("n Pürüzlülük Değeri :"))
        Q500 = float(input("Q500 Değeri :"))
        Q1000 = float(input("Q1000 Değeri :"))
        j = float(input("j Değeri :"))
        h = float(input("Dere yüksekliği :"))
        b = float(input("Dere  genişliği :"))
        byan = sqrt(h * h + h * h)
        büst = 2 * h + b
        A = round(((büst + b) / 2 * h), 4)
        Ç = round((b + 2 * byan), 4)
        R = round((A / Ç), 4)
        V = round((1 / n * pow(R, (2 / 3)) * pow(j, (1 / 2))), 4)
        Q = round((A * V), 2)
        print("")
        print("Q500 : " + str(Q500))
        print("Q1000 : " + str(Q1000))
        print("n : " + str(n))
        print("j : " + str(j))
        print("Islak ALan : " + str(A))
        print("Islak Çevre : " + str(Ç))
        print("Hidrolik Yarıçap : " + str(R))
        print("V : " + str(V) + "\n")
        print("Dereden geçen Q debisi : " + str(Q))
        h500=Q500*h/Q
        h1000=Q1000*h/Q


        if (Q500 <= Q):
            print("Kesit gelen Q500 debisi için  yeterli!")
        else:
            print("Kesit gelen Q500 debisi için  yetersiz!")

        if (Q1000 <= Q):
            print("Kesit gelen Q1000 debisi için  yeterli!")
        else:
            print("Kesit gelen Q1000 debisi için  yetersiz!")
    elif (niste == 'H' or niste == 'h'):
        print("n=(n0+n1+n2+n3+n4)*m\n")
        print("no=Kanalın içerdiği malzeme")
        print("- Toprak=0.020")
        print("- Kaya=0.025")
        print("- Kum=0.024")
        print("- Çakıl=0.028\n")

        print("n1=Düzensizlik derecesi")
        print("- Pürüzsüz=0.000")
        print("- Önemsiz=0.005")
        print("- Orta=0.010")
        print("- Şiddetli=0.020\n")

        print("n2=Kanal yarıçapındaki değişimler")
        print("- Aşamalı=0.000")
        print("- Ara sıra değişen=0.005")
        print("- sık değişen=0.010 - 0.015\n")

        print("n3=Engellerin benzer entkileri")
        print("- İhmal edilebilir=0.000")
        print("- Önemsiz=0.005")
        print("- Kayda değer=0.010")
        print("- Şiddetli=0.020\n")

        print("n4=Bitki örtüsü")
        print("- Düşük=0.005 - 0.010")
        print("- Orta=0.010 - 0.025")
        print("- Yüksek=0.025 - 0.050")
        print("- Çok yüksek=0.050 - 0.100\n")

        print("m=Kıvrım derecesi")
        print("- Öenemsiz=1")
        print("- Kayda değer=1.15")
        print("- Şiddetli=1.3\n")
        print("n=(n0+n1+n2+n3+n4)*m\n")
        n0 = float(input("n0=Kanalın içerdiği Kaya :"))
        n1 = float(input("n1=Düzensizlik derecesi :"))
        n2 = float(input("n2=Kanal yarıçapındaki değişimler :"))
        n3 = float(input("n3=Engellerin benzer entkileri :"))
        n4 = float(input("n4=Bitki örtüsü :"))
        m = float(input("m=Kıvrım derecesi :"))
        n = round(((n0 + n1 + n2 + n3 + n4) * m), 4)
        print("Derenin pürüzlülük katsayısı (n) :" + str(n) + " 'dır.\n")
        Q500 = float(input("Q500 Değeri :"))
        Q1000 = float(input("Q1000 Değeri :"))
        j = float(input("j Değeri :"))
        h = float(input("Dere yüksekliği :"))
        b = float(input("Dere  genişliği :"))
        byan = sqrt(h * h + h * h)
        büst = 2 * h + b
        A = round(((büst + b) / 2 * h), 4)
        Ç = round((b + 2 * byan), 4)
        R = round((A / Ç), 4)
        V = round((1 / n * pow(R, (2 / 3)) * pow(j, (1 / 2))), 4)
        Q = round((A * V), 2)
        print("")
        print("Q500 : " + str(Q500))
        print("Q1000 : " + str(Q1000))
        print("n : " + str(n))
        print("j : " + str(j))
        print("Islak ALan : " + str(A))
        print("Islak Çevre : " + str(Ç))
        print("Hidrolik Yarıçap : " + str(R))
        print("V : " + str(V) + "\n")
        print("Dereden geçen Q debisi : " + str(Q))
        if (Q500 <= Q):
            print("Kesit gelen Q500 debisi için  yetersiz!")

        else:
            print("Kesit gelen Q500 debisi için  yeterli!")

        if (Q1000 <= Q):
            print("Kesit gelen Q1000 debisi için  yetersiz!")
        else:
            print("Kesit gelen Q1000 debisi için  yeterli!")
    elif (niste == 'Q' or niste == 'q'):
        exit()
    else:
        print("Lütfen değerleri doğru giriniz!")
        continue

    cevap = input("Verileri Autocad'a aktarmak istermisiniz E,H :\n")
    if(cevap == 'E' or cevap == 'e'):

        dwg = dxf.drawing('DEREKESİTHESABI.dxf')
        dimstyles.setup(dwg)
        dimstyles.new("dots", tick="DIMTICK_DOT", scale=1, roundval=2, textabove=-.6,height=0.35)
        dimstyles.new("dots1", tick="DIMTICK_DOT", scale=1, roundval=2, textabove=.3,height=0.35)
        x=100
        y=100

        dereadi=input("Lütfen dere adinı giriniz :")
        tarih = input("Lütfen etüd tarihini giriniz :")
        etudyapan = input("Raporu hazırlayan :")

# Dere hatları--------------------------------------------------
        dwg.add(dxf.line((x, y), (x+h, y-h), color=2))
        dwg.add(dxf.line((x+h, y-h), (x+b+h,y-h), color=2))
        dwg.add(dxf.line((x+b+h,y-h), (x+b+2*h,y), color=2))
# Dere üst çizgi-----------------------------------------------------
        dwg.add(dxf.line((x , y ), (x + b + 2 * h, y ), color=140,linetype='DASHDOT'))
        dwg.add(dxf.line((x+h-h500 , y-h+h500 ), (x + b + h+h500, y-h+h500 ), color=140,linetype='DASHDOT'))
        dwg.add(dxf.line((x+h-h1000 , y-h+h1000 ), (x + b + h+h1000, y-h+h1000 ), color=140,linetype='DASHDOT'))

# dere ölçüleri-------------------------------------------------------

        dwg.add(LinearDimension((x+.5, y+.5), ((x , y ), (x + b + 2* h, y )), dimstyle='dots1', angle=0.))
        dwg.add(LinearDimension((x-h-.5, y-h-.5), ((x+h, y-h), (x+b+h,y-h)), dimstyle='dots', angle=0.))
        dwg.add(LinearDimension((x + b + 2 * h + .5, y - h - .5), ((x + b + 2 * h, y-h ), (x + b + 2* h, y )), dimstyle='dots1',angle=90.))


# yazılar------------------------------------------------------------

        dwg.add(dxf.text("Etud Yeri         : " + str(dereadi) , (x , y+3), height=0.25, rotation=0., color=7))
        dwg.add(dxf.text("Etud Tarihi      : " + str(tarih) , (x , y +2.5), height=0.25, rotation=0., color=7))
        dwg.add(dxf.text("Etud Yapan     : " + str(etudyapan) , (x , y +2), height=0.25, rotation=0., color=7))


        dwg.add(dxf.text("Q500: "+str(Q500)+" m3/sn dir.", (x+h, y-h-1.5),height=0.25, rotation=0., color=7))
        dwg.add(dxf.text("Q1000: "+str(Q1000) + " m3/sn dir.", (x + h, y - h - 2), height=0.25, rotation=0., color=7))
        dwg.add(dxf.text("Dere taban genişliği(b): "+str(b) + " m dir.", (x + h, y - h - 2.5), height=0.25, rotation=0., color=7))

        dwg.add(dxf.text("Dere Yüksekligi(h): "+str(h)+" m dir", (x + h, y - h - 3), height=0.25, rotation=0.,color=7))

        dwg.add(dxf.text("Dere taban egimi(j): "+str(j) + "  dir.", (x + h, y - h - 3.5), height=0.25, rotation=0.,color=7))


        dwg.add(dxf.text("Puruzluluk Katsayisi(n): "+str(n)+"  dir.", (x + h, y - h - 4), height=0.25, rotation=0., color=7))
        dwg.add(dxf.text("Islak Alan(A): "+str(A)+" m2.", (x + h, y - h - 4.5), height=0.25, rotation=0., color=7))
        dwg.add(dxf.text("Islak Çevre: "+str(Ç)+" m dir.", (x + h, y - h - 5), height=0.25, rotation=0., color=7))
        dwg.add(dxf.text("Hidrolik Yarıcap: "+str(R)+"  dir.", (x + h, y - h - 5.5), height=0.25, rotation=0., color=7))
        dwg.add(dxf.text("Derenin gecirebildigi maksimum Q debisi: "+str(Q)+" m3/sn dir.", (x + h, y - h - 6), height=0.25, rotation=0., color=7))

        dwg.add(dxf.text("Q500 =" + str(Q500) , (x+h-h500-1 , y-h+h500-0.07 ), height=0.1, rotation=0., color=2))
        dwg.add(dxf.text("Q1000 =" + str(Q1000), (x+h-h1000-1 , y-h+h1000-0.07 ), height=0.1, rotation=0., color=2))
        dwg.add(dxf.text("QDere =" + str(Q), (x-1 , y-0.07 ), height=0.1, rotation=0., color=3))
# solid ile nesne içlerini tarama
        # solidQ = dxf.solid(
        #     [(x + h, y - h), (x + h + b, y - h), (x + b + 2 * h, y ), (x , y )],
        #     color=1)
        # solidQ['layer'] = 'solids'
        # solidQ['color'] = 150
        # dwg.add(solidQ)
        #
        # solid1000 = dxf.solid(
        #     [(x + h, y - h), (x + h + b, y - h), (x + b + h + h1000, y - h + h1000), (x + h - h1000, y - h + h1000)],
        #     color=1)
        # solid1000['layer'] = 'solids'
        # solid1000['color'] = 151
        # dwg.add(solid1000)
        #
        # solid500 = dxf.solid(
        #     [(x + h, y - h), (x + h + b, y - h), (x + b + h + h500, y - h + h500), (x + h - h500, y - h + h500)],
        #     color=1)
        # solid500['layer'] = 'solids'
        # solid500['color'] =152
        # dwg.add(solid500)

        if (Q500 <= Q):
            dwg.add(dxf.text("Derenin gecirebildigi maksimum Q debisi: "+str(Q)+" > Q500 : "+str(Q500)+" olduğundan kesit yerterlidir.", (x + h, y - h - 7.5), height=0.25, rotation=0., color=3))
        else:
            dwg.add(dxf.text("Derenin gecirebildigi maksimum Q debisi: " + str(Q) + " <  Q500  :" + str(
                Q500) + " olduğundan kesit yertersizdir.", (x + h, y - h - 7.5), height=0.25, rotation=0., color=1))

        if (Q1000 <= Q):
            dwg.add(dxf.text("Derenin gecirebildigi maksimum Q debisi: " + str(Q) + " >  Q1000  :" + str(
                Q1000) + " olduğundan kesit yerterlidir.", (x + h, y - h - 8), height=0.25, rotation=0., color=3))
        else:
            dwg.add(dxf.text("Derenin gecirebildigi maksimum Q debisi: " + str(Q) + " <  Q1000  :" + str(
                Q1000) + " olduğundan kesit yertersizdir.", (x + h, y - h - 8), height=0.25, rotation=0., color=1))


# Çizim Şaablonunu oluşturmak------------------------------------------------------

        dwg.add(dxf.line((x-1.5,  y - h - 9), (x +2* h+b+5, y - h-9), color=7))#1.çizgi
        dwg.add(dxf.line((x +2* h+b+5, y - h-9), (x +2* h+b+5, y +4), color=7))#2.çizgi
        dwg.add(dxf.line((x +2* h+b+5, y +4), (x -1.5, y+4), color=7))#3.çizgi
        dwg.add(dxf.line((x -1.5, y +4), (x-1.5,  y - h - 9), color=7))#4.çizgi

        dwg.save()

        print("Autocad dosyası oluşturuldu.")


        cevap1 = input("Program kapatısın mı? E,H :\n")
        if (cevap1 == 'E' or cevap1 == 'e'):
            print("Bye Bye :)!")
        else:
            continue
        break











