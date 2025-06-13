#xml ile json birlikte kullanımı
# ülke paraları ve cripto paraları birleştirme uygulaması

import requests as rq
import xml.etree.ElementTree as et

from xml_kur import fiyat

coinUrl="https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"
dovizUrl="https://www.tcmb.gov.tr/kurlar/today.xml"

kurlar={}

r1=rq.get(coinUrl)
veri=r1.json()

r2=rq.get(dovizUrl)
xmlveri=r2.content
veri2=et.fromstring(xmlveri)


for coin in veri:
    kurlar.update({coin.get("name").upper():float(coin.get("current_price"))})

    for kur in veri2:
        isim=kur[2].text
        fiyat=kur[3].text
        fiyat=float(fiyat)
        kurlar.update({isim.upper():fiyat})




for k in kurlar:
    print(f"{k}: {kurlar.get(k)}")
