MustafaHesap = {
    'ad': 'Mustafa Bayramoğlu',
    'hesapNo':'1232d5425',
    'bakiye': 3000,
    'ekHesap': 2000
}

AliHesap = {
    'ad': 'Ali Bayramoğlu',
    'hesapNo':'1232d5426',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba, {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] = hesap['bakiye'] - miktar
        print('Paranızı alabilirsiniz.')
    
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('Paranız yetersiz, ek hesap kullanılsın mı (y/n): ')
            if ekHesapKullanimi == 'y':
                ekHesapKullanılacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] = hesap['ekHesap'] - ekHesapKullanılacakMiktar
                print(f'Paranızı alabilirsiniz. Hesabınızda kalan miktar. Ek Hesap: {hesap['ekHesap']} tl Hesap:{hesap['bakiye']} tl ')
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print('Hesabınızda yeterli miktarda para bulunmamaktadır.')

paraCek(MustafaHesap, 2000)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} No.lu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesabınızda ise {hesap['ekHesap']} TL bulunmaktadır.")

def paraYatir(hesap, paraMiktarı):
    hesap['bakiye'] += paraMiktarı
    print(f"Hesabınıza {paraMiktarı} TL eklendi. Yeni bakiyeniz {hesap['bakiye']} TL oldu. İyi günlerde harcamanızı dileriz.")

bakiyeSorgula(MustafaHesap)

print('***************************')

paraCek(MustafaHesap, 3000)

bakiyeSorgula(MustafaHesap)

print('***************************')

paraYatir(MustafaHesap, 10000)

bakiyeSorgula(MustafaHesap)