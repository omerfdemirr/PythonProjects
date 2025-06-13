import  requests as rq
import xml.etree.ElementTree as et

r = rq.get("https://www.tcmb.gov.tr/kurlar/today.xml")
veri=r.content
root=et.fromstring(veri)

for kur in root:
    isim = kur[1].text
    fiyat=kur[3].text
    print(isim,fiyat)
