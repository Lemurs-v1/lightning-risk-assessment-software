import pandas as pd
class LightningRiskCalculator_output_value:
    def __init__(self):
        self.N_G = None
        self.A_D_genişlik = None
        self.A_D_uzunluk = None
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
        self.A_D_yükseklik = None

    def n_g_bul(self):
        N_G = input("Yıldırım yoğunluğunu giriniz (sayı/bilmiyorum): ")
        if N_G.lower() == "bilmiyorum":
            T_D = float(input("Fırtınalı gün sayısını giriniz: "))
            N_G = 0.1 * T_D
        else:
            N_G = float(N_G)
        return N_G
    def a_d_denklem(self):
        A_D_denklem = input("yapı karmaşık yapıda mı: (evet/hayır)")
        return A_D_denklem
    def a_d_yükseklik_bul(self):
        A_D_yükseklik = float (input("yapı yüksekliğini giriniz: "))
        return A_D_yükseklik
    def a_d_genişlik_bul(self):
        A_D_genişlik = float(input("Yapı genişliğini giriniz: "))
        return A_D_genişlik

    def a_d_uzunluk_bul(self):
        A_D_uzunluk = float(input("Yapı uzunluğunu giriniz: "))
        return A_D_uzunluk
    

    def c_d_bul(self):
        C_D = input("Bağıl konumu nedir: ")
        return C_D

    def p_ta_bul(self):
        P_TA = input("İlave koruma tedbiri nedir: ")
        return P_TA

    def p_b_bul(self):
        P_B = input("Yapı karakteristiği nedir: ")
        return P_B

    def r_t_bul(self):
        r_t = input("Yapı tipi nedir: ")
        return r_t

    def n_z_bölü_n_t_bul(self):
        oran = input("Yapıdaki ve bölgedeki kişi sayısı eşit mi (evet/hayır): ")
        if oran.lower() == "evet":
            n_z_bölü_n_t = 1
        elif oran.lower() == "hayır":
            n_z = float(input("Bölgedeki kişi sayısı nedir: "))
            n_t = float(input("Yapıdaki kişi sayısı nedir: "))
            n_z_bölü_n_t = n_z / n_t
        else:
            print("Geçerli bir ifade giriniz.")
            n_z_bölü_n_t = None
        return n_z_bölü_n_t

    def tz_8760_bul(self):
        tz_8760 = input("Kişiler bölgede yılda kaç saat bulunmakta (saat/bilmiyorum): ")
        if tz_8760.lower() == "bilmiyorum":
            return 1
        else:
            return float(tz_8760) / 8760

    def p_spd_bul(self):
        P_SPD = input("LPL seviyesini giriniz: ")
        return P_SPD

    def c_ld_bul(self):
        C_LD = input("Dış hat tipi ve girişte bağlantı olarak ne kullanılıyor: ")
        return C_LD

    def l_o_bul(self):
        L_O = input("Yapı tipi nedir (tipik kayıp değeri için): ")
        return L_O
    def p_ms_bul (self):
        P_MS_soru = input("Sargılar arasında topraklı ekrana sahip ayırma transformatörleri veya fiber optik kablolar veya optik kuplörden meydana gelen ayırma ara yüzleri ile birlikte sağlanan donanım kullanılıyor mu ? :")
        if P_MS_soru == "evet":
            KS1 = 0 
            KS2 = 0
        elif P_MS_soru == "hayır":
            P_MS_soru2 = input("Kalınlıkları 0,1 mm’den fazla sürekli metal zırhlar mevcut mu ")
            if P_MS_soru2 =="hayır":
                KS1 = 10**-4
                KS2 = 10**-4
            elif P_MS_soru2 == "evet":
                WM1 = float(input(" ızgara benzeri uzaysal zırhlar veya ekran tipi LPS indirme iletkenlerinin ızgara gözenek genişliklerini giriniz(W_M_1)"))
                WM2 = float(input(" ızgara benzeri uzaysal zırhlar veya ekran tipi LPS indirme iletkenlerinin ızgara gözenek genişliklerini giriniz(W_M_2)"))
                KS1 = WM1*0.12
                KS2 = WM2*0.12
        P_MS_soru3 = input("İç kablaj tipi nedir")
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

        P_MS_soru4 = float(input(" korunan sistemin anma darbe dayanımı gerilimi nedir"))
        KS4 = (1/P_MS_soru4)
        self.P_MS = (KS1*KS2*KS3*KS4)**2
        return self.P_MS
    def r_p_bul(self):
        r_p =input("Yangın tedbiri sonucu kayıp azaltma faktörü nedir ?")
        return r_p
    def r_f_bul():
        r_f =input("Yangın riskine bağlı azalma faktörü nedir")
        return r_f
    def h_z_bul():
        H_Z = input("Özel tehlike olması halinde bağıl kayıp miktarını arttıran hz faktörü:")
        return H_Z
    def l_f_bul():
        L_F = input("Yapıda fiziksel hasarla ilgili tipik yüzde kayıp :")
        return L_F


