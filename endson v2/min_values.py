import pandas as pd
from output_value import LightningRiskCalculator_output_value
import math
import traceback
import re
from tkinter import messagebox
from Interface_functions import MainWindow

pi =math.pi
output = LightningRiskCalculator_output_value()




class LightningRiskCalculator_min_values:
    def __init__(self):
        self.N_G_C = output.n_g_bul()
        self.A_D_genişlik_C = output.a_d_genişlik_bul()
        self.A_D_uzunluk_C = output.a_d_uzunluk_bul()
        self.A_D_denklem_C = output.a_d_denklem()
        self.A_D_yükseklik_C = output.a_d_yükseklik_bul()
        self.A_D_yükseklik_max_C = output.a_d_yükseklik_max_bul()

        self.A_DJ_genişlik_C = output.a_dj_genişlik_bul()
        self.A_DJ_uzunluk_C = output.a_dj_uzunluk_bul()
        self.A_DJ_yükseklik_C = output.a_dj_yükseklik_bul()
        self.A_DJ_yükseklik_max_C = output.a_dj_yükseklik_max_bul()
        self.C_D_C = output.c_d_bul()

        self.C_DJ_C = output.c_dj_bul()
        self.P_TA_C = output.p_ta_bul()
        self.P_B_C = output.p_b_bul()
        self.r_t_C = output.r_t_bul()
        self.n_z_bölü_n_t_C = output.n_z_bölü_n_t_bul()
        self.t_z_bölü_8760_C = output.tz_8760_bul()
        self.P_SPD_C = output.p_spd_bul()
        self.C_LD_C = output.c_ld_bul()
        self.L_O_C = output.l_o_bul()
        self.P_MS_C = output.p_ms_bul()


        self.r_p_C = output.r_p_bul()
        self.r_f_C = output.r_f_bul() 
        self.H_Z_C = output.h_z_bul()
        self.L_F_C = output.l_f_bul()

        self.L_L_C = output.l_l_bul()
        self.C_I_C = output.c_ı_bul()
        self.C_T_C = output.c_t_bul()
        self.C_E_C = output.c_e_bul()
        self.P_TU_C = output.p_tu_bul()
        self.P_EB_C = output.p_eb_bul()
        self.P_LD_C = output.p_ld_bul()
        self.P_LI_C = output.p_lı_bul()
        self.L_FO_C_2 =output.l_fo_2_bul()
        self.L_FO_4_C = output.l_fo_4_bul()


        self.c_a_bölü_c_t_c = output.c_a_bölü_c_t()

        self.N_G = None
        self.A_D_genişlik = self.A_D_genişlik_C
        self.A_D_uzunluk = self.A_D_uzunluk_C
        self.A_D_denklem = self.A_D_denklem_C
        self.A_D_yükseklik = self.A_D_yükseklik_C
        self.A_D_yükseklik_max  =  self.A_D_yükseklik_max_C 

        self.A_DJ_genişlik = self.A_DJ_genişlik_C
        self.A_DJ_uzunluk = self.A_DJ_uzunluk_C
        self.A_DJ_yükseklik = self.A_DJ_yükseklik_C
        self.A_DJ_yükseklik_max  =  self.A_DJ_yükseklik_max_C 
        self.A_D = None
        self.A_DJ = None
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
        self.P_MS =None
        self.r_p = None
        self.r_f = None
        self.H_Z = None
        self.L_F = None
        self.L_L = None
        self.C_I = None
        self.C_T = None
        self.C_E = None
        self.P_TU = None
        self.P_EB =None
        self.L_L = None
        self.P_LD = None
        self.P_LI = None
        #######################################################################################33
        #######################################################################################33
        self.L_F_2=None
        self.L_O_2=None
        ##########################################################################################
        self.L_F_3=None
        ##########################################################################
        self.L_T_4=None
        self.L_F_4=None
        self.L_O_4=None
        self.c_z_b_c_t = None
        self.c_t=None

    def n_g_belirle(self):
        self.N_G = self.N_G_C
        return self.N_G

    
    
    def a_d_belirle(self):
        
        if self.A_D_denklem == "evet":
            self.HMAX =  self.A_D_yükseklik_max
            self.A_D= pi*(3*self.HMAX)**2

        elif self.A_D_denklem=="hayır":
            self.A_D = (self.A_D_uzunluk * self.A_D_genişlik)+(2*3*self.A_D_yükseklik)*(self.A_D_uzunluk+self.A_D_genişlik)+(pi*(3*self.A_D_yükseklik)**2)
        
        return self.A_D
    def c_dj_belirle(self):
        data = {
            "bağıl konum": [
                "Daha yüksek cisimler ile çevrelenen yapı",
                "Aynı yükseklikte veya daha alçak cisimler ile çevrelenen yapı",
                "Aynı yapı: yakında başka cisimlerin olmaması",
                "Tepe veya tepecik üzerinde ayrık yapı"
            ],
            "C_DJ": [0.25, 0.5, 1, 2]
        }
        C_DJ_DF = pd.DataFrame(data)
        self.C_DJ = C_DJ_DF.loc[C_DJ_DF["bağıl konum"] == self.C_DJ_C, "C_DJ"].values[0]
        return self.C_DJ     
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
        self.C_D = C_D_DF.loc[C_D_DF["bağıl konum"] == self.C_D_C, "C_D"].values[0]
        return self.C_D

    def p_ta_belirle(self):
        data = { 
            "ilave koruma tedbirleri": [
                "Koruma tedbiri yok",
                "Uyarı işaretleri",
                "Açıktaki bölümlerin elektriksel yalıtımları",
                "Etkin zemin eş potansiyel kuşaklanması",
                "Fiziksel kısıtlamalar ve indirme indirme iletkeni olarak kullanılan bina iskeleti"
            ],
            "P_TA": [1, 0.1, 0.01, 0.01, 0]
        }
        P_TA_DF = pd.DataFrame(data)
        self.P_TA = P_TA_DF.loc[P_TA_DF["ilave koruma tedbirleri"] == self.P_TA_C, "P_TA"].values[0]
        return self.P_TA

    def p_b_belirle(self):
        data = { 
            "yapı karakteristikleri": [
                "Yapı LPS ile korunumuyor",
                "Yapı 4. seviye LPS ile korunuyor",
                "Yapı 3. seviye LPS ile korunuyor",
                "Yapı 2. seviye LPS ile korunuyor",
                "Yapı 1. seviye LPS ile korunuyor",
                "LPS 1'e uygun yakalama ucu sistemine ve doğal indirme iletkeni olarak davranan sürekli metal veya takviyeli beton iskelete sahip yapı",
                "Metal çatıya ve çatıdaki bütün tesisatı doğrudan yıldırım düşmesine karşı tamamen koruyan, muhtemelen doğal bileşenler dahil, bir yakalama ucu sistemine ve doğal indirme iletkeni olarak davranan sürekli metal veya takviyeli beton iskelete sahip yapı"
            ],
            "P_B": [1, 0.2, 0.1, 0.05, 0.02, 0.01, 0.001]
        }
        P_B_DF = pd.DataFrame(data)
        self.P_B = P_B_DF.loc[P_B_DF["yapı karakteristikleri"] == self.P_B_C, "P_B"].values[0]
        return self.P_B

    def l_t_belirle(self):
        self.L_T = 10**-2
        return self.L_T

    def n_z_bölü_n_t_belirle(self):
        self.n_z_bölü_n_t = self.n_z_bölü_n_t_C
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
        self.r_t = r_t_DF.loc[r_t_DF["yapı tipi"] == self.r_t_C, "r_t"].values[0]
        return self.r_t
    def a_dj_belirle(self):
        
        if self.A_DJ_yükseklik != self.A_D_yükseklik_max:
            self.HMAXJ =  self.A_DJ_yükseklik_max
            self.A_DJ= pi*(3*self.HMAXJ)**2

        elif self.A_DJ_yükseklik == self.A_D_yükseklik_max:
            self.A_DJ = (self.A_DJ_uzunluk * self.A_DJ_genişlik)+(2*3*self.A_DJ_yükseklik)*(self.A_DJ_uzunluk+self.A_DJ_genişlik)+(pi*(3*self.A_DJ_yükseklik)**2)
        return self.A_DJ
    def t_z_bölü_8760_belirle(self):
        if self.t_z_bölü_8760_C == "bilmiyorum":
            self.t_z_bölü_8760 = 1
        elif isinstance(self.t_z_bölü_8760_C, int) or isinstance(self.t_z_bölü_8760_C, float):
            self.t_z_bölü_8760 = float(self.t_z_bölü_8760_C) / 8760
        
        return self.t_z_bölü_8760

    def p_spd_belirle(self):
        data = {
            "LPL": [
                "Kordineli SPD sistemi yok",
                "3. ve 4. seviye",
                "2. seviye",
                "1.seviye"
            ],
            "P_SPD": [1, 0.05, 0.02, 0.01]
        }
        P_SPD_DF = pd.DataFrame(data)
        self.P_SPD = P_SPD_DF.loc[P_SPD_DF["LPL"] == self.P_SPD_C, "P_SPD"].values[0]
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
        self.C_LD = C_LD_DF.loc[C_LD_DF["Dış hat tipi ve Girişte bağlantı"] == self.C_LD_C, "C_LD"].values[0]
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
        self.L_O = L_O_DF.loc[L_O_DF["Tipik kayıp değeri"] == self.L_O_C, "L_O"].values[0]
        return self.L_O
    def a_m_belirle(self):
        self.A_M = 2*500*(self.A_D_uzunluk+self.A_D_genişlik)+(pi*(500)**2)
        return self.A_M
    def p_ms_belirle(self):
        self.P_MS = self.P_MS_C
        return self.P_MS
    
    def r_p_belirle(self):
        data = {
            "yangın tedbirleri": [
                "Patlama riski var",
                "Tedbir yok",
                "Aşağıdaki tedbirlerden biri: Yangın söndürücüler, elle çalıştırılan sabit yangın söndürme tesisleri, elle çalıştırılan alarm tesisleri, hidrantlar, yangına karşı korunmalı bölmeler, kaçış güzergâhları.",
                "Aşağıdaki tedbirlerden biri:Otomatik sabit yangın söndürme tesisleri, otomatik alarm tesisleri bulunuyorsa (itfayiye 10 dkdan az sürede gelebiliyorsa ve aşırı gerilim gibi hasarlardan korunuyorsa)",
            ],
            "r_p": [1, 1, 0.5, 0.2]
        }

        r_p_DF = pd.DataFrame(data)

        # Check if r_p_C exists in the 'yangın tedbirleri' column
        if self.r_p_C in r_p_DF["yangın tedbirleri"].values:
            self.r_p = r_p_DF.loc[r_p_DF["yangın tedbirleri"] == self.r_p_C, "r_p"].values[0]
            return self.r_p
        else:
            raise ValueError("Provided r_p_C value does not match any entry in the 'yangın tedbirleri' column.")
    
    def r_f_belirle(self):
        data = {
            "risk tutarı" :
            ["Patlama : Bölgeler 0, 20 ve katı patlayıcı",
                "Patlama : Bölgeler 1, 21",
                "Patlama : Bölgeler 2, 22",
                "Yangın : Yüksek",
                "Yangın : Normal",
                "Yangın : Düşük",
                "Patlama ve Yangın : Yok "
                ],
                "r_f" : [1,0.1,0.001,0.1,0.01,0.001,0]
        }
        r_f_DF = pd.DataFrame(data)
       
        self.r_f = r_f_DF.loc[r_f_DF["risk tutarı"]==self.r_f_C,"r_f"].values[0]
        return self.r_f
    
    def h_z_belirle(self):
        data ={
            "özel tehlike cinsi" : 
            ["Özel tehlike yok",
                "Düşük panik seviyesi (örneğin, yapının iki katla sınırlı olması, insan sayısının 100’den fazla olmaması)",
                "Orta panik seviyesi (yapının kültür veya spor faaliyetlerine tahsis edilmesi ve katılan insan sayısının 100 ile 1000 arasında olması gibi)",
                "Tahliye zorluğu (örneğin, hareket edemeyen kişiler, hastaneler)",
                "Yüksek panik seviyesi (örneğin, yapının kültür veya spor faaliyetlerine tahsis edilmesi ve katılan insan sayısının 1000’den fazla olması gibi)"
            ],
            "h_z" : [1,2,5,5,10]
        }
        h_z_DF = pd.DataFrame(data)
        self.H_Z = h_z_DF.loc[h_z_DF["özel tehlike cinsi"]==self.H_Z_C,"h_z"].values[0]
        return self.H_Z
    
    def l_f_belirle(self):
        data = { 
            "yüzde kayıp" : 
            ["Patlama riski",
                "Hastane, otel, okul, kamu binası",
                "Halka açık eğlence yeri, ibadethane, müze",
                "Sanayi, ticari",
                "Diğerleri"
                ],
                "L_f" : [0.1,0.1,0.05,0.02,0.01]
        }
        L_F_DF = pd.DataFrame(data)

        self.L_F = L_F_DF.loc[L_F_DF["yüzde kayıp"]==self.L_F_C,"L_f"].values[0]
        return self.L_F
    def a_l_belirle(self):
        self.L_L = self.L_L_C
        self.A_L = 40* self.L_L
        return self.A_L
    
    def c_ı_belirle(self):
        data = {
            "Güzergah" : ["Havai","Gömülü","Tamamiyle bir kafes biçimindeki toprak sonlandırma uclarına giden gömülü kablolar"
            ],
            "C_ı" : [1,0.5,0.01]
        }
        C_I_DF = pd.DataFrame(data)
        self.C_I = C_I_DF.loc[C_I_DF["Güzergah"]==self.C_I_C,"C_ı"].values[0]
        return self.C_I
    def C_t_belirle(self):
        data = {
            "Tesisat" : [
                "AG güç, telekomünikasyon veya veri hattı",
                "YG güç (YG/AG transformatörü ile)"
            ],
            "C_t" : [1,0.2]
        }
        C_t_DF = pd.DataFrame(data)
        self.C_T = C_t_DF.loc[C_t_DF["Tesisat"]== self.C_T_C,"C_t"].values[0]
        return self.C_T
    def C_e_belirle(self):
        data = {
            "Çevre" : [
                "Kırsal",
                "Banliyo",
                "Şehir",
                "Büyük binaların olduğu şehir(20m'den yüksek.)"
            ],
            "C_e" : [1,0.5,0.1,0.01]
        }
        C_e_DF = pd.DataFrame(data)
        
        self.C_E= C_e_DF.loc[C_e_DF["Çevre"]==self.C_E_C,"C_e"].values[0]
        return self.C_E
    def p_tu_belirle(self):
        data = {
            "Korunma tedbiri": [
                "Korunma tedbirleri yok",
                "Kablaj uyarıları",
                "Elektriksel yalıtım",
                "Fiziksel kısıtlamalar"
            ],
            "P_TU": [1, 10**-1, 10**-2, 0]
        }
        P_TU_DF = pd.DataFrame(data)

        self.P_TU = P_TU_DF.loc[P_TU_DF["Korunma tedbiri"] == self.P_TU_C, "P_TU"].values[0]
        return self.P_TU
    def p_eb_belirle(self,):
        data = {
            "LPL": [
                "SPD yok",
                "III-IV",
                "II",
                "I"
            ],
            "P_EB": [1, 0.05, 0.02, 0.01]
        }
        P_EB__DF = pd.DataFrame(data)

        self.P_EB = P_EB__DF.loc[P_EB__DF["LPL"] == self.P_EB_C, "P_EB"].values[0]
        return self.P_EB

    def a_ı_belirle(self):
        self.A_I = 4000*self.L_L
        return self.A_I
    def p_ld_belirle(self):
        if self.P_LD_C[0] == "Havai veya gömülü hat, zırhlanmamış veya zırhı donanım gibi aynı kuşaklama barasına bağlanan zırhlanmış":
            self.P_LD = 1
        elif self.P_LD_C[0] == "Zırh donanımı gibi aynı kuşaklama barasına bağlanan zırhlanmış havai veya gömülü":
            data = {
                "Direnç Değeri": ["5 Ω /km <RS ≤ 20 Ω /km", "5 Ω /km <RS ≤ 20 Ω /km", "5 Ω /km <RS ≤ 20 Ω /km", "5 Ω /km <RS ≤ 20 Ω /km", "5 Ω /km <RS ≤ 20 Ω /km",
                                    "1 Ω /km <RS ≤ 5 Ω /km", "1 Ω /km <RS ≤ 5 Ω /km", "1 Ω /km <RS ≤ 5 Ω /km", "1 Ω /km <RS ≤ 5 Ω /km", "1 Ω /km <RS ≤ 5 Ω /km",
                                    "RS ≤ 1 Ω /km", "RS ≤ 1 Ω /km", "RS ≤ 1 Ω /km", "RS ≤ 1 Ω /km", "RS ≤ 1 Ω /km"],
                "Dayanım Gerilimi": ["1", "1.5", "2.5", "4", "6",
                                        "1", "1.5", "2.5", "4", "6",
                                        "1", "1.5", "2.5", "4", "6",],
                "Değer": [1, 1, 0.95, 0.9, 0.8,
                            0.9, 0.8, 0.6, 0.3, 0.1,
                            0.6, 0.4, 0.2, 0.04, 0.02]
            }
            df = pd.DataFrame(data)
            self.P_LD = df.loc[(df['Direnç Değeri'] == self.P_LD_C[1]) & (df['Dayanım Gerilimi'] == self.P_LD_C[2]), 'Değer'].values[0]
        return self.P_LD

    def p_lı_belirle(self):
        if self.P_LI_C[1] == "Güç hatları":
            data = {
                "Dayanım Gerilimi": ["1", "1.5", "2.5", "4", "6"],
                "Değer": [1, 0.6, 0.3, 0.16, 0.1]
            }
        elif self.P_LI_C[1] == "Telekomünikasyon hatları":
            data = {
                "Dayanım Gerilimi": ["1", "1.5", "2.5", "4", "6"],
                "Değer": [1, 0.5, 0.2, 0.08, 0.04]
            }
        else:
            raise ValueError("Geçersiz hat türü")

        df = pd.DataFrame(data)
        
        self.P_LI = df.loc[df['Dayanım Gerilimi'] == self.P_LI_C[2], 'Değer'].values[0]
        return self.P_LI
    
    def c_lı_belirle(self):
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
        self.C_LI = C_LI_DF.loc[C_LI_DF["Dış hat tipi ve Girişte bağlantı"] == self.C_LD_C, "C_LI"].values[0] # C_LI_C tanımlanacak 
        return self.C_LI

##############################################################################################################################################################
##############################################################################################################################################################

    def l_f_2_belirle(self):
        data = { 
            "yüzde kayıp" : 
            ["Gaz, su, güç besleme",
                "TV, telekomünikasyon hatları",
                ],
                "L_f_2" : [10**-1,10**-2]
        }
        L_F_2_DF = pd.DataFrame(data)

        self.L_F_2 = L_F_2_DF.loc[L_F_2_DF["yüzde kayıp"]==self.L_FO_C_2,"L_f_2"].values[0]
        return self.L_F_2


    def l_o_2_belirle(self):
        data = { 
            "hizmet tipi" : 
            ["Gaz, su, güç besleme",
                "TV, telekomünikasyon hatları",
                ],
                "L_o_2" : [10**-2,10**-3]
        }
        L_O_2_DF = pd.DataFrame(data)

        self.L_O_2 = L_O_2_DF.loc[L_O_2_DF["hizmet tipi"]==self.L_FO_C_2,"L_o_2"].values[0]
    
        return self.L_O_2
##############################################################################################################################################33
##############################################################################################################################################33
    def l_f_3_belirle(self):
        self.L_F_3 = 10**-1
        return self.L_F_3
    ################################################################################################################################
    ################################################################################################################################
    def l_t_4_belirle(self):
        self.L_T_4 = 10**-2
        return self.L_T_4
    
    def l_f_4_belirle(self):
        data = { 
            "yapının tipi" : 
            ["Patlama riski",
                "Hastahane, sanayi, müze, zirai",
                "Otel, okul, ofis, ibadet yeri, halka açık eğlence yeri, ticari",
                "Diğerleri"
                ],
                "L_f" : [1,0.5,0.2,10**-1]
        }
        L_F_4_DF = pd.DataFrame(data)
        self.L_F_4 = L_F_4_DF.loc[L_F_4_DF["yapının tipi"]==self.L_FO_4_C,"L_f"].values[0]
        return self.L_F_4
    
    def l_o_4_belirle(self):
        data = { 
            "yapının tipi" : 
            ["Patlama riski",
                "Hastahane, sanayi, müze, zirai",
                "Otel, okul, ofis, ibadet yeri, halka açık eğlence yeri, ticari",
                "Diğerleri"
                ],
                "L_o" : [10**-1,10**-2,10**-3,10**-4]
        }
        L_O_4_DF = pd.DataFrame(data)

        self.L_O_4 = L_O_4_DF.loc[L_O_4_DF["yapının tipi"]==self.L_FO_4_C,"L_o"].values[0]
        return self.L_O_4
    
    def c_z_bölü_c_t(self):
        return 1

    def c_a_bölü_c_t(self):
        if self.c_a_bölü_c_t_c == "Var":
            return (1/10)
        elif self.c_a_bölü_c_t_c == "Yok":
            return 0     
        
