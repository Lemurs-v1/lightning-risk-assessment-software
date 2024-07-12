import pandas as pd
class LightningRiskCalculator_output_value:
    def __init__(self):
        self.N_G = None
        self.A_D_genişlik = None
        self.A_D_uzunluk = None
        self.A_D_yükseklik = None
        self.A_D_denklem = None
        self.C_D = None
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

       

    def n_g_bul(self):
        self.N_G = 15 #input("Yıldırım yoğunluğunu giriniz (sayı/bilmiyorum): ")
        if self.N_G == "bilmiyorum":
            T_D = float(input("Fırtınalı gün sayısını giriniz: "))
            self.N_G = 0.1 * T_D
        else:
            self.N_G = float(self.N_G)
        return self.N_G
    def a_d_denklem(self):
        self.A_D_denklem = "hayır"#input("yapı karmaşık yapıda mı: (evet/hayır)")
        return self.A_D_denklem
    def a_d_yükseklik_bul(self):
        self.A_D_yükseklik = 150#float(input("yapı yüksekliğini giriniz: "))
        return self.A_D_yükseklik
    def a_d_genişlik_bul(self):
        self.A_D_genişlik = 20#float(input("Yapı genişliğini giriniz: "))
        return self.A_D_genişlik

    def a_d_uzunluk_bul(self):
        self.A_D_uzunluk = 30#float(input("Yapı uzunluğunu giriniz: "))
        return self.A_D_uzunluk
    

    def c_d_bul(self):
        self.C_D = "Daha yüksek cisimler ile çevrelenen yapı"#input("Bağıl konumu nedir: ")
        return self.C_D

    def p_ta_bul(self):
        self.P_TA = "koruma tedbiri yok"#input("İlave koruma tedbiri nedir: ")
        return self.P_TA

    def p_b_bul(self):
        self.P_B = "yapı 4. seviye LPS ile korunuyor"#input("Yapı karakteristiği nedir: ")
        return self.P_B

    def r_t_bul(self):
        self.r_t = "mermer, seramik"#input("Yapı tipi nedir: ")
        return self.r_t

    def n_z_bölü_n_t_bul(self):
        oran = "evet"#input("Yapıdaki ve bölgedeki kişi sayısı eşit mi (evet/hayır): ")
        if oran.lower() == "evet":
            self.n_z_bölü_n_t = 1
        elif oran.lower() == "hayır":
            n_z = float(input("Bölgedeki kişi sayısı nedir: "))
            n_t = float(input("Yapıdaki kişi sayısı nedir: "))
            self.n_z_bölü_n_t = n_z / n_t
        else:
            print("Geçerli bir ifade giriniz.")
            self.n_z_bölü_n_t = None
        return self.n_z_bölü_n_t

    def tz_8760_bul(self):
        tz_8760 = "bilmiyorum"#input("Kişiler bölgede yılda kaç saat bulunmakta (saat/bilmiyorum): ")
        if tz_8760.lower() == "bilmiyorum":
            return 1
        else:
            return float(tz_8760) / 8760

    def p_spd_bul(self):
        self.P_SPD = "3. ve 4. seviye"#input("LPL seviyesini giriniz: ")
        return self.P_SPD

    def c_ld_bul(self):
        self.C_LD = "Dış hat tipi: Zırhlanmamış havai hat/ Girişte bağlantı: Tanımlanmamış"#input("Dış hat tipi ve girişte bağlantı olarak ne kullanılıyor: ")
        return self.C_LD

    def l_o_bul(self):
        self.L_O = "Patlama riski"#input("Yapı tipi nedir (tipik kayıp değeri için): ")
        return self.L_O
    def p_ms_bul (self):
        P_MS_soru = "hayır"#input("Sargılar arasında topraklı ekrana sahip ayırma transformatörleri veya fiber optik kablolar veya optik kuplörden meydana gelen ayırma ara yüzleri ile birlikte sağlanan donanım kullanılıyor mu ? :")
        if P_MS_soru == "evet":
            KS1 = 0 
            KS2 = 0
        elif P_MS_soru == "hayır":
            P_MS_soru2 = "hayır"#input("Kalınlıkları 0,1 mm’den fazla sürekli metal zırhlar mevcut mu ")
            if P_MS_soru2 =="hayır":
                KS1 = 10**-4
                KS2 = 10**-4
            elif P_MS_soru2 == "evet":
                WM1 = float(input(" ızgara benzeri uzaysal zırhlar veya ekran tipi LPS indirme iletkenlerinin ızgara gözenek genişliklerini giriniz(W_M_1)"))
                WM2 = float(input(" ızgara benzeri uzaysal zırhlar veya ekran tipi LPS indirme iletkenlerinin ızgara gözenek genişliklerini giriniz(W_M_2)"))
                KS1 = WM1*0.12
                KS2 = WM2*0.12
        P_MS_soru3 = "Zırhlanmamış kablo – döngüleri önlemek için güzergâh tedbiri yok a"#input("İç kablaj tipi nedir")
        data = {
            "iç kablaj tipi": [
                "Zırhlanmamış kablo – döngüleri önlemek için güzergâh tedbiri yok a",
                "Zırhlanmamış kablo – döngüleri önlemek için güzergâh tedbiri var b ",
                "Zırhlanmamış kablo – döngüleri önlemek için güzergâh tedbiri var c",
                "Zırhlanmış kablolar e metal kanal içinde serili kablolar  d",
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
        self.r_p ="Patlama riski var"#input("Yangın tedbiri sonucu kayıp azaltma faktörü nedir ?")
        return self.r_p
    
    
    def r_f_bul(self):
        self.r_f ="Yangın : Yüksek"#input("Yangın riskine bağlı azalma faktörü nedir")
        return self.r_f
    
    def h_z_bul(self):
        self.H_Z = "Tahliye zorluğu (örneğin, hareket edemeyen kişiler, hastaneler)"#input("Özel tehlike olması halinde bağıl kayıp miktarını arttıran hz faktörü:")
        return self.H_Z
    
    
    def l_f_bul(self):
        self.L_F = "Halka açık eğlence yeri, ibadethane, müze"#input("Yapıda fiziksel hasarla ilgili tipik yüzde kayıp :")
        return self.L_F


