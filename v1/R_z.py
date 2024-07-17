import pandas as pd

# sonunda "#" olan fonksiyonlar halihazırda tanımlanmışlardır.

class N_ı(): 
    def __init__(self) -> None:
        self.onuzeri
        self.A_ı_belirle

    def N_g(self): #
        pass
    def A_ı_belirle(self): # Hattın yakınında toprağa düşen yıldırımların toplama alanı
        pass               # Nasıl belirleneceğini tartış şekil A.5
    def C_ı(self): # R_w içinde yazıldı.
        pass
    def C_e(self): #
        pass
    def C_t(self): #
        pass
    def onuzeri(self):
        on_uzeri = 10**-6
        return on_uzeri

class P_z():
    def __init__(self) -> None:
        self.C_lı_belirle
    
    def P_spd_belirle(self): #
        pass
    
    def P_lı_belirle():
        P_lı_cevap = input("Güç hatları veya telekominikasyon hatlarının güzergah, zırhlama ve kuşaklama şartları hangisidir? ")
        if P_lı_cevap == "evet":
            sonuc = 1
        elif P_lı_cevap == "hayır":
            data = {
                "Hat tipi": ["Güç Hatları", "Güç Hatları", "Güç Hatları", "Güç Hatları", "Güç Hatları",
                                "Telekomünikasyon hatları", "Telekomünikasyon hatları", "Telekomünikasyon hatları", "Telekomünikasyon hatları", "Telekomünikasyon hatları",
                ],
                "Dayanım Gerilimi": ["1", "1.5", "2.5", "4", "6",
                                    "1", "1.5", "2.5", "4", "6",
                                   ],
                "Değer": [1, 0.6, 0.3, 0.16, 0.1,
                        1, 0.5, 0.2, 0.08, 0.04,
                        ]
            }
            df = pd.DataFrame(data)
            print(df)
            secim1 = input("Hat tipini giriniz:")
            secim2 = input("Dayanım gerilimini giriniz (1-1,5-2,5-4-6):")
            
            sonuc = df.loc[(df['Hat tipi'] == secim1) & (df['Dayanım Gerilimi'] == secim2), 'Değer'].values[0]
        return sonuc 
    def C_lı_belirle(self):
        data = {
            "Dış hat tipi ve Girişte bağlantı": [
                "Dış hat tipi: Zırhlanmamış havai hat/ Girişte bağlantı: Tanımlanmamış",
                "Dış hat tipi: Zırhlanmamış gömülü hat / Girişte bağlantı: Tanımlanmamış",
                "Dış hat tipi: Çoklu topraklanmış nötr güç hattı / Girişte bağlantı: Yoktur",
                "Dış hat tipi: Zırhlanmış gömülü hat (güç veya TLC) / Girişte bağlantı: Zırh, donanımda olduğu gibi aynı kuşaklama barasına bağlanmamış",
                "Dış hat tipi: Zırhlanmış havai hat (güç veya TLC) / Girişte bağlantı: Zırh, donanımda olduğu gibi aynı kuşaklama barasına bağlanmamış",
                "Dış hat tipi: Zırhlanmış gömülü hat (güç veya TLC) / Girişte bağlantı: Zırh, donanımda olduğu gibi aynı kuşaklama barasına bağlanmış",
                "Dış hat tipi: Zırhlanmış havai hat (güç veya TLC) / Girişte bağlantı: Zırh, donanımda olduğu gibi aynı kuşaklama barasına bağlanmış",
                "Dış hat tipi: Yıldırıma karşı koruyucu kablo kanalları, metalik kanal veya metalik borular içinde yıldırım koruyucu kablo veya kablaj / Girişte bağlantı: Zırh, donanımda olduğu gibi aynı kuşaklama barasına bağlanmış",
                "Dış hat tipi: Dış hat yok / Girişte bağlantı: Dış hatlara bağlantı yok (yalnız başına bulunan sistemler)",
                "Dış hat tipi: Herhangi bir tip / Girişte bağlantı: EN 62305-4’e göre ayırma ara yüzü"
                ],
                "C_LI": [1, 1, 0.2, 0.3, 0.1, 0, 0, 0, 0, 0]
                }
        C_LI_DF = pd.DataFrame(data)
        self.C_LD = C_LI_DF.loc[C_LI_DF["Dış hat tipi ve Girişte bağlantı"] == C_LI_C, "C_LD"].values[0] # C_LI_C tanımlanacak 
        return self.C_LI



class L_z():
    def __init__(self) -> None:
        pass
    def L_o_belirle(self): #
        pass
    def nz_bolu_nt(self): #
        pass
    def tz_bolua87608(self): #
        pass
