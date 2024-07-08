from LightningRiskCalculator_Ra import LightningRiskCalculator_N_D
import pandas as pd
def n_d_belirle(self):
    x = LightningRiskCalculator_N_D()
    N_D = x.n_d_belirle()
    return N_D
class LightningRiskCalculator_P_C:
    def __init__(self):
        self.P_SPD=None
        self.C_LD=None
    def p_c_belirle(self):
        def p_spd_belirle():
            data ={ "LPL": [
                "kordineli spd sistemi yok  ",
                "3. ve 4. seviye",
                "2. seviye",
                "1.seviye",#burda not 2 muhabeti var ama detay bir olay onu en son bakılmalı
                ],
                "P_SPD": [1,0.05,0.02,0.01]
                }
            P_SPD_DF = pd.DataFrame(data)
            seçim = input("LPL seviyesini giriniz: ")
            P_SPD = P_SPD_DF.loc[P_SPD_DF["LPL"] == seçim, "P_SPD"].values[0]
            return P_SPD
        def c_ld_belirle():
            
            data ={ "Dış hat tipi ve Girişte bağlantı": [
                "Dış hat tipi: Zırhlanmamış havai hat/ Girişte bağlantı: Tanımlanmamış",
                "Dış hat tipi: Zırhlanmamış gömülü hat / Girişte bağlantı: Tanımlanmamış",
                "Dış hat tipi: Çoklu topraklanmış nötr güç hattı  / Girişte bağlantı: Yoktur",
                "Dış hat tipi: Zırhlanmış gömülü hat (güç veya TLC) / Girişte bağlantı: Zırh, donanımda olduğu gibi aynı kuşaklama barasına bağlanmamış",
                "Dış hat tipi: Zırhlanmış havai hat (güç veya TLC) / Girişte bağlantı: Zırh, donanımda olduğu gibi aynı kuşaklama barasına bağlanmamış",
                "Dış hat tipi: Zırhlanmış gömülü hat (güç veya TLC) / Girişte bağlantı: Zırh, donanımda olduğu gibi aynı kuşaklama barasına bağlanmış",
                "Dış hat tipi: Zırhlanmış havai hat (güç veya TLC) / Girişte bağlantı: Zırh, donanımda olduğu gibi aynı kuşaklama barasına bağlanmış",
                "Dış hat tipi: Yıldırıma karşı koruyucu kablo kanalları, metalik kanal veya metalik borular içinde yıldırım koruyucu kablo veya kablaj / Girişte bağlantı: Zırh, donanımda olduğu gibi aynı kuşaklama barasına bağlanmış ",
                "Dış hat tipi: Dış hat yok / Girişte bağlantı: Dış hatlara bağlantı yok (yalnız başına bulunan sistemler)",
                "Dış hat tipi: Herhangi bir tip / Girişte bağlantı: EN 62305-4’e göre ayırma ara yüzü",
                ],
                "C_LD": [1,1,1,1,1,1,1,0,0,0]
                }
            C_LD_DF = pd.DataFrame(data)
            seçim = input("Dış hat tipi ve Girişte bağlantı olarak ne kullanılıyor:  ")
            C_LD = C_LD_DF.loc[C_LD_DF["Dış hat tipi ve Girişte bağlantı"] == seçim, "C_LD"].values[0]
            return C_LD
        P_SPD = p_spd_belirle()
        C_LD = c_ld_belirle()
        P_C = P_SPD*C_LD
        return P_C
x = LightningRiskCalculator_P_C()
PC = x.p_c_belirle()
print (PC)
