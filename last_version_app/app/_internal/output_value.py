import pandas as pd

"""
if Cd_C == "Daha yüksek cisimler ile çevrelenen yapı":
    #print("okey")
else:
    #print("olmadı")

#print("Ad_C:", Ad_C)
#print("Cd_C:", Cd_C)
#print("rt_C:", rt_C)
#print("Ce_C:", Ce_C)
#print("Adj_C:", Adj_C)
#print("Cdj_C:", Cdj_C)
#print("Pb_C:", Pb_C)
#print("Pta_C:", Pta_C)
#print("Cld_C:", Cld_C)
#print("Pli_C:", Pli_C)
#print("Pld_C:", Pld_C)
#print("Pspd_C:", Pspd_C)
#print("Cl_C:", Cl_C)
#print("Peb_C:", Peb_C)
#print("CT_C:", CT_C)
#print("ca_bolu_ct_C:", ca_bolu_ct_C)
#print("rf_C:", rf_C)
#print("rp_C:", rp_C)
#print("Lf_C:", Lf_C)
#print("Lo_C:", Lo_C)
#print("Lfo2_C:", Lfo2_C)
#print("Lfo4_C:", Lfo4_C)
#print("KS3_C:", KS3_C)
#print("Pld2_C:", Pld2_C)
#print("Pld3_C:", Pld3_C)
#print("Pli2_C:", Pli2_C)
#print("Ng_C:", Ng_C)
#print("wm1_C:", wm1_C)
#print("wm2_C:", wm2_C)
#print("Uw_C:", Uw_C)
#print("ekranlama_C:", ekranlama_C)
#print("metal_C:", metal_C)
#print("Ng_double_C:", Ng_double_C)
#print("Ad_y_double_C:", Ad_y_double_C)
#print("Ad_g_double_C:", Ad_g_double_C)
#print("Ad_u_double_C:", Ad_u_double_C)
#print("Adj_g_double_C:", Adj_g_double_C)
#print("Adj_u_double_C:", Adj_u_double_C)
#print("nt_C:", nt_C)
#print("nz_C:", nz_C)
#print("nz_double_C:", nz_double_C)
#print("tz_C:", tz_C)
#print("Ll_C:", Ll_C)
#print("Hz_C", Hz_C)
#print("Ptu_C" ,Ptu_C)
"""

class LightningRiskCalculator_output_value:



    def __init__(self):
        with open("kullanıcı_değer.txt", "r",encoding="utf-8") as dosya:
            veriler_file = dosya.read()
        veriler_file

        veriler = veriler_file.split("\n")

        self.Ad_C = str(veriler[0])  # Karmaşık biçimli
        self.Cd_C = str(veriler[1])  # Daha yüksek cisimler ile çevrelenen yapı
        self.rt_C = str(veriler[2])  # asfalt, muşamba, ahşap
        self.Ce_C = str(veriler[3])  # Şehir
        self.Adj_C = str(veriler[4])  # False
        self.Cdj_C = str(veriler[5])  # Daha yüksek cisimler ile çevrelenen yapı  
        self. Pb_C = str(veriler[6])  # Yapı 1. seviye LPS ile korunuyor
        self.Pta_C = str(veriler[7])  # Etkin zemin eş potansiyel kuşaklanması
        self.Cld_C = str(veriler[8])  # Dış hat tipi: Zırhlanmış havai hat (güç veya TLC) / Girişte bağlantı: Zırh, donanımda olduğu gibi aynı kuşaklama barasına bağlanmış
        self.Pli_C = str(veriler[9])  # 5 Ω /km <RS ≤ 20 Ω /km
        self.Pld_C = str(veriler[10])  # Havai veya gömülü hat, zırhlanmamış veya zırhı donanım gibi aynı kuşaklama barasına bağlanan zırhlanmış
        self.Pspd_C = str(veriler[11])  # 2. seviye
        self.Cl_C = str(veriler[12])  # Gömülü
        self.Peb_C = str(veriler[13])  # I
        self.CT_C = str(veriler[14])  # AG güç, telekomünikasyon veya veri hattı
        self.ca_bolu_ct_C = str(veriler[15])  # Var
        self.rf_C = str(veriler[16])  # Patlama : Bölgeler 2, 22
        self.rp_C = str(veriler[17])  # Patlama riski var
        self.Lf_C = str(veriler[18])  # Sanayi, ticari
        self.Lo_C = str(veriler[19])  # Hastahanenin diğer bölümleri
        self.Lfo2_C = str(veriler[20])  # TV, telekomünikasyon hatları
        self.Lfo4_C = str(veriler[21])  # Gaz, su, güç besleme
        self.KS3_C = str(veriler[22])  # Zırhlanmamış kablo – döngüleri önlemek için güzergâh tedbiri yok a
        self.Pld_2_C = str(veriler[23])  # 1 Ω /km <RS ≤ 5 Ω /km
        self.Pld_3_C = str(veriler[24])  # 2.5
        self.Pli_2_C = str(veriler[25])  # 1.5
        self.Ng_C =str(veriler[26])  # False
        self.wm1_C = float(veriler[27])  # 2.0
        self.wm2_C = float(veriler[28])  # 10.0
        self.Uw_C = float(veriler[29])  # 90.0
        self.ekranlama_C = str(veriler[30])  # True
        self.metal_C = str(veriler[31])  # False
        self.Ng_double_C = float(veriler[32])  # 1.0
        self.Ad_y_double_C = float(veriler[33])  # 2.0
        self.Ad_g_double_C = float(veriler[34])  # 3.0
        self.Ad_u_double_C = float(veriler[35])  # 4.0
        self.Ad_ymax=float(veriler[48])

        self.Adj_g_double_C = float(veriler[36])  
        self.Adj_u_double_C = float(veriler[37])  
        self.Adj_y=float(veriler[49])
        self.Adj_y_max=float(veriler[50])

        self.nt_C = float(veriler[38])  
        self.nz_C = str(veriler[39])  # False
        self.nz_double_C = float(veriler[40])  # 6.0
        self.tz_C = float(veriler[41])  # 7.0
        self.Ll_C = float(veriler[42])  # 8.0
        self.Hz_C = str(veriler[43])
        self.Ptu_C = str(veriler[44])
        self.tz_value = str(veriler[45])
        self.Ll_value=str(veriler[46])
        self.description=str(veriler[47])

        self.Rapor_yazarı=str(veriler[51])
        self.Müsteri=str(veriler[52])
        self.Obje=str(veriler[53])
        self.Proje_no=str(veriler[54])
        self.R1_value=str(veriler[55])
        self.R4_value=str(veriler[56])
        self.N_G = None
        self.A_D_genişlik = None
        self.A_D_uzunluk = None
        self.A_D_yükseklik = None
        self.A_D_yükseklik_max = None
        self.A_D_denklem = None

        
        self.A_DJ_genişlik = None
        self.A_DJ_uzunluk = None
        self.A_DJ_yükseklik = None
        self.A_DJ_yükseklik_max = None
        self.A_DJ_denklem = None
        
        self.C_D = None
        self.C_DJ = None
        self.P_TA = None
        self.P_B = None
        self.r_t = None
        self.n_z_bölü_n_t = None
        self.t_z_bölü_8760 = None
        self.P_SPD = None
        self.C_LD = None
        self.L_O = None
        self.P_MS = None
        self.r_f = None
        self.r_p = None
        self.H_Z = None
        self.L_F = None

        self.L_L = None
        self.C_I = None
        self.C_T = None
        self.C_E = None
        self.A_DJ = None

        self.P_TU =None
        self.P_EB = None
        self.P_LI = None
        self.L_FO_2 = None
        self.L_F_4 = None
        self.c_z = None
        self.c_a_b_c_t = None
        self.P_MS_soru2 = None


    def n_g_bul(self):
        self.N_G = self.Ng_double_C 
 
        if self.Ng_C == 'True':
            self.N_G = 0.1 * self.Ng_double_C
            ##print(self.N_G)
        elif self.Ng_C == "False":
            pass
            ##print(self.N_G)
        return self.N_G

    def a_d_denklem(self):
        self.A_D_denklem = self.Ad_C
        ##print(self.A_D_denklem)#input("yapı karmaşık yapıda mı: Karmaşık biçimli
        return self.A_D_denklem
    def a_d_yükseklik_bul(self):
        self.A_D_yükseklik = self.Ad_y_double_C#float(input("yapı yüksekliğini giriniz: "))
        #print(self.A_D_yükseklik)
        return self.A_D_yükseklik
    def a_d_genişlik_bul(self):
        self.A_D_genişlik = self.Ad_g_double_C
        #print(self.A_D_genişlik)#float(input("Yapı genişliğini giriniz: "))
        return self.A_D_genişlik

    def a_d_uzunluk_bul(self):
        self.A_D_uzunluk =self.Ad_u_double_C
        #print(self.A_D_uzunluk) #float(input("Yapı uzunluğunu giriniz: "))
        return self.A_D_uzunluk
    def a_d_yükseklik_max_bul(self):
        self.A_D_yükseklik_max =self.Ad_ymax
        return self.A_D_yükseklik_max

    def a_dj_yükseklik_bul(self):
        self.A_DJ_yükseklik = self.Adj_y#float(input("yapı yüksekliğini giriniz: "))
        #print(self.A_D_yükseklik)
        return self.A_DJ_yükseklik
    def a_dj_genişlik_bul(self):
        self.A_DJ_genişlik = self.Adj_g_double_C
        #print(self.A_D_genişlik)#float(input("Yapı genişliğini giriniz: "))
        return self.A_DJ_genişlik

    def a_dj_uzunluk_bul(self):
        self.A_DJ_uzunluk =self.Adj_u_double_C
        #print(self.A_D_uzunluk) #float(input("Yapı uzunluğunu giriniz: "))
        return self.A_DJ_uzunluk
    def a_dj_yükseklik_max_bul(self):
        self.A_DJ_yükseklik_max =self.Adj_y_max
        return self.A_DJ_yükseklik_max

    
    



    
        
    def c_d_bul(self):
        self.C_D = self.Cd_C
        #print(self.C_D)#input("Bağıl konumu nedir: ")
        return self.C_D
    def c_dj_bul(self):
        self.C_DJ = self.Cdj_C
        #print(self.C_DJ)#input("ayrık yapının Bağıl konumu nedir: ")
        return self.C_DJ

    def p_ta_bul(self):
        self.P_TA = self.Pta_C
        #print(self.P_TA)#input("İlave koruma tedbiri nedir: ")
        return self.P_TA

    def p_b_bul(self):
        self.P_B = self.Pb_C
        #print(self.P_B)#input("Yapı karakteristiği nedir: ")
        return self.P_B
    

    def r_t_bul(self):
        self.r_t = self.rt_C
        #print(self.r_t)#input("Yapı tipi nedir: ")
        return self.r_t

    def n_z_bölü_n_t_bul(self):
        oran = self.nz_C#input("Yapıdaki ve bölgedeki kişi sayısı biliniyor mu (evet/hayır): ")
        if oran == "True":
            self.n_z_bölü_n_t = 1
            #print(self.n_z_bölü_n_t)
        elif oran == "False":
            n_z = self.nz_double_C
            n_t = self.nt_C
            self.n_z_bölü_n_t = n_z / n_t
            #print(self.n_z_bölü_n_t)
        return self.n_z_bölü_n_t

    def tz_8760_bul(self):
        print(self.tz_value)
        print(self.tz_C)
        if self.tz_value == "True":
            self.t_z_bölü_8760 = 1
        if self.tz_value == "False":
            self.t_z_bölü_8760 =self.tz_C
        return self.t_z_bölü_8760 
        

    def p_spd_bul(self):
        self.P_SPD = self.Pspd_C
        #print(self.P_SPD)#input("LPL seviyesini giriniz: ")
        return self.P_SPD

    def c_ld_bul(self):
        self.C_LD = self.Cld_C
        #print(self.C_LD)#input("Dış hat tipi ve girişte bağlantı olarak ne kullanılıyor: ")
        return self.C_LD

    def l_o_bul(self):
        self.L_O = self.Lo_C
        #print(self.L_O)#input("Yapı tipi nedir (tipik kayıp değeri için): ")
        return self.L_O
    def p_ms_bul (self):
        P_MS_soru = self.ekranlama_C#input("Sargılar arasında topraklı ekrana sahip ayırma transformatörleri veya fiber optik kablolar veya optik kuplörden meydana gelen ayırma ara yüzleri ile birlikte sağlanan donanım kullanılıyor mu ? :")
        if P_MS_soru == 'True':
            KS1 = 0 
            KS2 = 0
        elif P_MS_soru == "False":
            self.P_MS_soru2 =self.metal_C#input("Kalınlıkları 0,1 mm’den fazla sürekli metal zırhlar mevcut mu ")
            if self.P_MS_soru2 =="False":
                KS1 = 10**-4
                KS2 = 10**-4
            elif self.P_MS_soru2 == "True":
                WM1 = self.wm1_C
                WM2 =self.wm2_C
                KS1 = WM1*0.12
                KS2 = WM2*0.12
        P_MS_soru3 = self.KS3_C#input("İç kablaj tipi nedir")
        data = {
            "iç kablaj tipi": [
                "Zırhlanmamış kablo – döngüleri önlemek için güzergâh tedbiri yok a",
                "Zırhlanmamış kablo – döngüleri önlemek için güzergâh tedbiri var b",
                "Zırhlanmamış kablo – döngüleri önlemek için güzergâh tedbiri var c",
                "Zırhlanmış kablolar e metal kanal içinde serili kablolar d",
            ],
            "K_S3": [1,0.2,0.01,0.0001]
        }
        K_S3_DF = pd.DataFrame(data)
        KS3 = K_S3_DF.loc[K_S3_DF["iç kablaj tipi"] == P_MS_soru3, "K_S3"].values[0]

        P_MS_soru4 = 100 #float(input(" korunan sistemin anma darbe dayanımı gerilimi nedir"))
        KS4 = (1/P_MS_soru4)
        self.P_MS = (KS1*KS2*KS3*KS4)**2
        return self.P_MS
    
    
    def r_p_bul(self):
        self.r_p =self.rp_C
        #print(self.r_p)#input("Yangın tedbiri sonucu kayıp azaltma faktörü nedir ?")
        return self.r_p
    
    
    def r_f_bul(self):
        self.r_f =self.rf_C
        #print(self.r_f)#input("Yangın riskine bağlı azalma faktörü nedir")
        return self.r_f
    
    def h_z_bul(self):
        self.H_Z = self.Hz_C
        #print(self.H_Z)#input("Özel tehlike olması halinde bağıl kayıp miktarını arttıran hz faktörü:")
        return self.H_Z
    
    
    def l_f_bul(self):
        self.L_F = self.Lf_C
        #print(self.L_F)#input("Yapıda fiziksel hasarla ilgili tipik yüzde kayıp :")
        return self.L_F
    def l_l_bul(self):
        self.L_L_C = self.Ll_C#float(input("Hat kısmının uzunluğu :"))
        #print(self.L_L_C)
        return self.L_L_C

    def c_ı_bul(self):
        self.C_I = self.Cl_C
        #print(self.C_I)#input("Güzergah türü nedir ?")
        return self.C_I
    def c_t_bul(self):
        self.C_T = self.CT_C
        #print(self.C_T)#input("Tesisat türü nedir?")
        return self.C_T
    def c_e_bul(self):
        self.C_E = self.Ce_C
        #print(self.C_E)#input("Çevre türü nedir?")
        return self.C_E
    def p_tu_bul(self):
        self.P_TU =self.Ptu_C#input("korunma tedbiri nedir ?")
        return self.P_TU
    def p_eb_bul(self):
        self.P_EB = self.Peb_C#input("LPL SEVİYESİ NEDİR?")
        return self.P_EB
    def p_ld_bul(self):
        self.P_LD_1 = self.Pld_C#input("Güç hatları veya telekominikasyon hatlarının güzergah, zırhlama ve kuşaklama şartları hangisidir?(evet/hayır)")
        self.P_LD_2 = self.Pld_2_C#input("Direnç değerini giriniz: ")
        self.P_LD_3 = self.Pld_3_C#input("Dayanım gerilimini giriniz (1-1,5-2,5-4-6): ")
        self.P_LD = [self.P_LD_1,self.P_LD_2,self.P_LD_3]
        return self.P_LD
    def p_lı_bul(self):
        self.P_LI_1 = "döndürmüyor"#input("Güç hatları veya telekominikasyon hatlarının güzergah, zırhlama ve kuşaklama şartları hangisidir?(evet/hayır)")
        self.P_LI_2 = self.Pli_C#input("Hat tipini giriniz:")
        self.P_LI_3 = self.Pli_2_C#input("Dayanım gerilimini giriniz (1-1,5-2,5-4-6):")
        self.P_LI = [self.P_LI_1,self.P_LI_2,self.P_LI_3]
        return self.P_LI
    def l_fo_2_bul(self):
        self.L_FO_2 = self.Lfo2_C#input("yapı tipi nedir")
        return self.L_FO_2
    def l_fo_4_bul(self):
        self.L_FO_4 = self.Lfo4_C#input("yapı tipi nedir")
        return self.L_FO_4
    def c_a_bölü_c_t(self):
        self.c_a_b_c_t = self.ca_bolu_ct_C#input("ortam hayvanlı mı ? (evet/hayır):") 
        return self.c_a_b_c_t
x = LightningRiskCalculator_output_value()
x.tz_8760_bul()