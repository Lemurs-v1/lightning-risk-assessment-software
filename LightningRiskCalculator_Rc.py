from LightningRiskCalculator_Ra import LightningRiskCalculator_N_D
from LightningRiskCalculator_Ra import LightningRiskCalculator_L_A
import pandas as pd
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

class LightningRiskCalculator_L_C:

    def __init__ (self):
        self.L_O = None
    def l_c_belirle(self):

        def l_o_belirle():
            data ={ "Tipik kayıp değeri": [
                    "Patlama riski","Hastahanenin yoğun bakım ünitesi ve ameliyathane","Hastahanenin diğer bölümleri"
                    ],
                    "L_O": [10**-1,10**-2,10**-3]
                    }
            L_O_DF = pd.DataFrame(data)
            seçim = input("Yapı tipi nedir: (tipik kayıp değeri için) ")
            L_O = L_O_DF.loc[L_O_DF["Tipik kayıp değeri"] == seçim, "L_O"].values[0]
            return L_O
        L_O = l_o_belirle()
        n_z_bölü_n_t = LightningRiskCalculator_L_A().n_z_bölü_n_t_belirle()
        t_z_bölü_8760 = LightningRiskCalculator_L_A().t_z_bölü_8760_belirle()
        L_C = n_z_bölü_n_t*t_z_bölü_8760*L_O
        return L_C

class LightningRiskCalculator_R_C:
    def __int__(self):
        self.L_C =None
        self.P_C = None
        self.N_D = None
    def r_c_belirle(self):
        L_C = LightningRiskCalculator_L_C().l_c_belirle()
        P_C = LightningRiskCalculator_P_C().p_c_belirle()
        N_D = LightningRiskCalculator_N_D().n_d_belirle()
        R_C = L_C*P_C*N_D
        return R_C