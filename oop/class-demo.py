# Comment ismined bir sınıf oluşturunuz.
# Comment sınıfı username, test, likes, dislikes isminde özelliklere sahip olsun.
# 5 adet farklı comment oluşturup döngü yardımıyla yorumları ekrana yazdırınız.

class Comment:
    def __init__(self, username, text, likes=0, dislikes=0):
        self.username = username
        self.text = text
        self.likes = likes
        self.dislikes = dislikes

c1 = Comment("musolee1", "Merhaba Dünya!", 15, 3)
c2 = Comment("musolee2", "Merhaba Dünya2!", 16, 2)
c3 = Comment("musolee3", "Merhaba Dünya3!", 12, 6)
c4 = Comment("musolee4", "Merhaba Dünya4!", 11, 3)
c5 = Comment("musolee5", "Merhaba Dünya5!", 13, 8)

comments = [c1.text,c2.text,c3.text,c4.text,c5.text]

for c in comments:
    print(c)