import pandas as pd
from output_value import LightningRiskCalculator_output_value
import math
pi =math.pi
output = LightningRiskCalculator_output_value()
N_G_C = output.n_g_bul()
A_D_genişlik_C = output.a_d_genişlik_bul()
A_D_uzunluk_C = output.a_d_uzunluk_bul()
C_D_C = output.c_d_bul()
P_TA_C = output.p_ta_bul()
P_B_C = output.p_b_bul()
r_t_C = output.r_t_bul()
n_z_bölü_n_t_C = output.n_z_bölü_n_t_bul()
t_z_bölü_8760_C = output.tz_8760_bul()
P_SPD_C = output.p_spd_bul()
C_LD_C = output.c_ld_bul()
L_O_C = output.l_o_bul()

class LightningRiskCalculator_min_values:
    def __init__(self):
        self.N_G = None
        self.A_D_AUY = None
        self.C_D = None
        self.P_TA = None
        self.P_B = None
        self.r_t = None
        self.L_T = None
        self.n_z_bölü_n_t = None
        self.t_z_bölü_8760 = None
        self.P_SPD = None
        self.C_LD = None
        self.L_O = None
        self.A_M =None

    def n_g_belirle(self):
        self.N_G = N_G_C
        return self.N_G
    
    def a_d_belirle(self):
        A_D = A_D_uzunluk_C * A_D_genişlik_C
        self.A_D_AUY = [A_D, A_D_uzunluk_C, A_D_genişlik_C]
        return self.A_D_AUY
        
    def c_d_belirle(self):
        data = {
            "bağıl konum": [
                "Daha yüksek cisimler ile çevrelenen yapı",
                "Aynı yükseklikte veya daha alçak cisimler ile çevrelenen yapı",
                "Aynı yapı: yakında başka cisimlerin olmaması",
                "Tepe veya tepecik üzerinde ayrık yapı"
            ],
            "C_D": [0.25, 0.5, 1, 2]
        }
        C_D_DF = pd.DataFrame(data)
        self.C_D = C_D_DF.loc[C_D_DF["bağıl konum"] == C_D_C, "C_D"].values[0]
        return self.C_D

    def p_ta_belirle(self):
        data = { 
            "ilave koruma tedbirleri": [
                "koruma tedbiri yok",
                "uyarı işaretleri",
                "açıktaki bölümlerin elektriksel yalıtımları",
                "etkin zemin eş potansiyel kuşaklanması",
                "fiziksel kısıtlamalar ve indirme indirme iletkeni olarak kullanılan bina iskeleti"
            ],
            "P_TA": [1, 0.1, 0.01, 0.01, 0]
        }
        P_TA_DF = pd.DataFrame(data)
        self.P_TA = P_TA_DF.loc[P_TA_DF["ilave koruma tedbirleri"] == P_TA_C, "P_TA"].values[0]
        return self.P_TA

    def p_b_belirle(self):
        data = { 
            "yapı karakteristikleri": [
                "yapı LPS ile korunumuyor",
                "yapı 4. seviye LPS ile korunuyor",
                "yapı 3. seviye LPS ile korunuyor",
                "yapı 2. seviye LPS ile korunuyor",
                "yapı 1. seviye LPS ile korunuyor",
                "LPS 1'e uygun yakalama ucu sistemine ve doğal indirme iletkeni olarak davranan sürekli metal veya takviyeli beton iskelete sahip yapı",
                "Metal çatıya ve çatıdaki bütün tesisatı doğrudan yıldırım düşmesine karşı tamamen koruyan, muhtemelen doğal bileşenler dahil, bir yakalama ucu sistemine ve doğal indirme iletkeni olarak davranan sürekli metal veya takviyeli beton iskelete sahip yapı"
            ],
            "P_B": [1, 0.2, 0.1, 0.05, 0.02, 0.01, 0.001]
        }
        P_B_DF = pd.DataFrame(data)
        self.P_B = P_B_DF.loc[P_B_DF["yapı karakteristikleri"] == P_B_C, "P_B"].values[0]
        return self.P_B

    def l_t_belirle(self):
        self.L_T = 10**-2
        return self.L_T

    def n_z_bölü_n_t_belirle(self):
        self.n_z_bölü_n_t = n_z_bölü_n_t_C
        return self.n_z_bölü_n_t

    def r_t_belirle(self):
        data = {
            "yapı tipi": [
                "tarımsal, beton",
                "mermer, seramik",
                "çakıl, moket, halı",
                "asfalt, muşamba, ahşap"
            ],
            "r_t": [10**-2, 10**-3, 10**-4, 10**-5]
        }
        r_t_DF = pd.DataFrame(data)
        self.r_t = r_t_DF.loc[r_t_DF["yapı tipi"] == r_t_C, "r_t"].values[0]
        return self.r_t

    def t_z_bölü_8760_belirle(self):
        if t_z_bölü_8760_C == "bilmiyorum":
            cevap_son = 1
        elif isinstance(t_z_bölü_8760_C, int) or isinstance(t_z_bölü_8760_C, float):
            cevap_son = float(t_z_bölü_8760_C) / 8760
        self.t_z_bölü_8760 = cevap_son
        return self.t_z_bölü_8760

    def p_spd_belirle(self):
        data = {
            "LPL": [
                "kordineli SPD sistemi yok",
                "3. ve 4. seviye",
                "2. seviye",
                "1.seviye"
            ],
            "P_SPD": [1, 0.05, 0.02, 0.01]
        }
        P_SPD_DF = pd.DataFrame(data)
        self.P_SPD = P_SPD_DF.loc[P_SPD_DF["LPL"] == P_SPD_C, "P_SPD"].values[0]
        return self.P_SPD

    def c_ld_belirle(self):
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
                "C_LD": [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
                }
        C_LD_DF = pd.DataFrame(data)
        self.C_LD = C_LD_DF.loc[C_LD_DF["Dış hat tipi ve Girişte bağlantı"] == C_LD_C, "C_LD"].values[0]
        return self.C_LD
    def l_o_belirle(self):
        data = {
            "Tipik kayıp değeri": [
                "Patlama riski",
                "Hastahanenin yoğun bakım ünitesi ve ameliyathane",
                "Hastahanenin diğer bölümleri"
            ],
            "L_O": [10**-1, 10**-2, 10**-3]
        }
        L_O_DF = pd.DataFrame(data)
        self.L_O = L_O_DF.loc[L_O_DF["Tipik kayıp değeri"] == L_O_C, "L_O"].values[0]
        return self.L_O
    def a_m_belirle(self):
        self.A_M = 2*500*(self.A_D_AUY[1]+self.A_D_AUY[2])*pi*500**2
        return self.A_M
