import db

urunler = db.urunler

def urunEkle(urunAdi, fiyat):

    db.urunler.append({
        "id": len(db.urunler) + 1,
        "urunAdi": urunAdi,
        "fiyat": fiyat
    })


def urunGuncelle(id, urunAdi, fiyat):
    for urun in db.urunler:
        if(int(urun['id']) == id):
            urun['urunAdi'] = urunAdi
            urun['fiyat'] = fiyat
            break


def urunleriGetir():
    for urun in db.urunler:
        print(f"id: {urun['id']}, Ürün Adı: {urun['urunAdi']} Fiyat: {urun['fiyat']}")