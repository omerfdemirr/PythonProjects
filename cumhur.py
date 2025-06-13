import requests as rq
import xml.etree.ElementTree as et

# ✅ XML verisini çek
r = rq.get("https://www.cumhuriyet.com.tr/sitemaps/news.xml")
veri = r.content
root = et.fromstring(veri)

# ✅ XML içeriğini yazdır (Kontrol amaçlı)
print("XML İçeriği:")
print(veri.decode("utf-8"))
print("\n" + "-" * 40 + "\n")

# ✅ Title içeren etiketleri bul ve ekrana yazdır
titles = []
for item in root.iter():
    if "title" in item.tag.lower():  # Eğer etiket adı 'title' içeriyorsa al
        titles.append(item.text)

# ✅ Başlıkları ekrana yazdır
if titles:
    print("Haber Başlıkları:")
    for title in titles:
        print(title)
else:
    print("Title bilgisi bulunamadı! XML içeriğini kontrol edin.")

