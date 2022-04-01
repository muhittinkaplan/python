import Canlilar

class MemelilerClass(Canlilar.CanlilarClass):
    def __init__(self):
        print("Memeliler Class Çalıştı")
    def vucut(self):
        print("memeliler sicak kanlıdır")

    def amfibiIcinYazilmis(self):
        print("Amfibi için yazılmış bir fonksiyon Memeliler içinde")

class SurungenlerClass(Canlilar.CanlilarClass):
    def __init__(self):
        print("Surungenler Class Çalıştı")


    def vucut(self):
        print("Surungenler soguk kanlıdır")
        print(super().superIleGeldim())  # bir üst sınıf olan surungenlerclass ına ulaşıyor

class KuslarClass(Canlilar.CanlilarClass):
    def __init__(self):
        print("Kuslar Class Calisti")
    def vucut(self):
        print("Kuslar Sıcak Kanlıdır")

    def solunum(self):
        print("Kuslar İçindeki Solunum Çalişti, Canlılar içindeki solunum override edildi")

class KopekClass(MemelilerClass):
    def __init__(self):
        print("KopekClass Calisti")
    def ses(self):
        print("Kopekler Havlar")

class KediClass(MemelilerClass):
    def __init__(self):
        print("KediClass Calisti")
    def ses(self):
        print("Kediler Miyavlar")


class YilanClass(SurungenlerClass):
    def __init__(self):
        print("YilanClass Calisti")


    def ses(self):
        print("Yılanlar Tıslar")

class KartalClass(KuslarClass):
    def __init__(self):
        print("Kartal Class Çalıştı")
    def ses(self):
        print("Kuslar Öter")

class AmfibiClass(SurungenlerClass,MemelilerClass):
    def __init__(self):
        print("Amfibi Class Çalıştı, Örnek Hatalı olabilir")
    def ses(self):
        print("Amfibiler genelde ses çıkartmaz")

if __name__ == '__main__':
    kopek=KopekClass()
    kopek.ses()#Kopek Sınıfında Ses
    kopek.vucut()#memeliler sınıfndan kalıtım
    kopek.solunum()#canlılar sınıfından memeliler sınıfına oradan kopek sınıfına
    print("-"*50)
    yılan=YilanClass()
    yılan.ses()#yılan Sınıfında Ses
    yılan.vucut()#yılan sınıfndan kalıtım
    yılan.solunum()#canlılar sınıfından surungenler sınıfına oradan yılan sınıfına
    print("-" * 50)
    kartal=KartalClass()
    kartal.ses()
    kartal.vucut()
    kartal.solunum()
    print("-" * 50)
    kedi=KediClass()
    kedi.ses()
    kedi.solunum()
    print("-"*50)

    bilmedigimHayvan=AmfibiClass()
    bilmedigimHayvan.ses()
    bilmedigimHayvan.vucut()
    bilmedigimHayvan.amfibiIcinYazilmis()#memeliler sınıfında