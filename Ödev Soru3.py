def ilkaltıkar(yG,fG,üRg,çM,kG,dM):
    global hesapa
    hesapa=(yG+fG+üRg)-(çM+kG+dM)
    return hesapa
def sonaltıgiderler(yG,sG,eTg,üSg,çM,kG,bM):
    global hesapb
    hesapb=(yG+sG+eTg+üSg)-(çM+kG+bM)
    return hesapb
def farkhesapla(hesapa,hesapb):
    fark=hesapa-hesapb
    if(fark>5000):
        print("İşletme çok karlı")
    elif(1000<fark<5000):
        print("İşletme karı normal")
    else:
        print("İşletme yeterince karda değil")
yG=int(input("Yazlım Geliri="))
fG=int(input("Finansman Gelrri="))
üRg=int(input("Ürün satış geliri="))
çM=int(input("Çalışan Maaşları="))
kG=int(input("Kira Gideri="))
dM=int(input("Donanım Maliyeti="))
sG=int(input("Sponsorluk Geliri="))
eTg=int(input("E ticaret geliiri="))
üSg=int(input("Ürün satış geliri="))
bM=int(input("Bakım Maliyeti="))
k=ilkaltıkar(yG,fG,üRg,çM,kG,dM)
p=sonaltıgiderler(yG,sG,eTg,üSg,çM,kG,bM)
farkhesapla(k,p)


