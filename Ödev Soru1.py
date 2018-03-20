#tSm=toplam satış miktarı
#hM=hammadde maliyeti
#bOg=bakım onarım giderleri
#sG=sevkiyat giderleri
#sAhg=satın alınan hizmet giderleri


def katmadegerciro(tSm,hM,bOg,sG,sAhg):
    #Global yapmamın nedeni başka fonksiyona girdi olacak
    global katmadegerciro
    katmadegerciro=(tSm-(hM+bOg+sG+sAhg))
    if(katmadegerciro>1000):
        print("İşletme karda katma değer cirosu yüksek")
    elif(500<katmadegerciro<999):
        print("İşletme karda katma değer cirosu normal")
    else:
        print("İşletme katma değer cirosu düşük")
tSm=int(input("Toplam Satış miktarı="))
hM=int(input("Hammadde Maliyeti="))
bOg=int(input("Bakım onarım Gidereri="))
sG=int(input("Sevkiyat Giderleri="))
sAhg=int(input("Satın Alınan Hizmet Giderleri="))

k=katmadegerciro(tSm,hM,bOg,sG,sAhg)


