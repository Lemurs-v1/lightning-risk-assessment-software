import os
class veri_cek:
        def veri_yukle(self):

            
            with open('kullanıcı_değer.txt', 'r',encoding = "utf-8") as dosya:
                veriler = dosya.readlines()
            return veriler


