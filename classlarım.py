gündüz_gece= True

class Tekerlek:
    def __init__(self):
        self.basınc = 10
        self.kutle = 3000

    def lastikAsındır(self,km):
        asinma_miktari = km / 100
        self.kutle -= asinma_miktari
    
    def printPSI(self):
        print("Tekerin Basıncı şu anda 10")

    def tekeriPatlat(self):
        self.basınc=0

    def havaEkle(self,miktar=10):
        self.basınc += miktar

    def havaEksilt(self,miktar=3):
        self.basınc -= miktar
        return self.basınc

    def gündüzMü(self):
        global gündüz_gece
        if gündüz_gece == True:
            print("Şu anda Gündüz")
            gündüz_gece = False
        else:
            print("Şu anda Gece")
            gündüz_gece = True

class kışLastigi(Tekerlek):
    def __init__(self):
        super().__init__()
        self.kutle = 3500
    
    
    def printPSI(self,x):
        """
        Bu yorum satırı bu fonksiyonu anlatır..
        """
        print("Tekerin Basıncı şu anda 50")
        super().printPSI()

    def gündüzMü(self):
        pass
        
if __name__ == "__main__":
    kışLastigim = kışLastigi()
    yazLastigim = yazLastigi()
    kışLastigim.printPSI()
    yazLastigim.printPSI()
    print(kışLastigim.basınc)
    kışLastigim.gündüzMü()
    kışLastigim.havaEksilt()


    

    