class LightningRiskCalculator_output_value:
    def __init__(self):
        self.N_G = None
        self.A_D_genişlik = None
        self.A_D_uzunluk = None
        self.A_D_yükseklik = None
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

        self.r_p = None
        """
        self.r_f = None
        self.H_Z = None
        self.L_F = None
"""
        
    def n_g_bul(self):
        N_G = input("Yıldırım yoğunluğunu giriniz (sayı/bilmiyorum): ")
        if N_G.lower() == "bilmiyorum":
            T_D = float(input("Fırtınalı gün sayısını giriniz: "))
            N_G = 0.1 * T_D
        else:
            N_G = float(N_G)
        return N_G
    def a_d_denklem(self):
        A_D_denklem = "hayır"#input("yapı karmaşık yapıda mı: (evet/hayır)")
        return A_D_denklem
    def a_d_genişlik_bul(self):
        A_D_genişlik = "20"#float(input("Yapı genişliğini giriniz: "))
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

    def r_p_bul(self):
        self.r_p ="Patlama riski var"#input("Yangın tedbiri sonucu kayıp azaltma faktörü nedir ?")
        return self.r_p
    """
    def r_f_bul(self):
        self.r_f ="Patlama : Bölgeler 1, 21"#input("Yangın riskine bağlı azalma faktörü nedir")
        return self.r_f
    def h_z_bul(self):
        self.H_Z = "Düşük panik seviyesi (örneğin, yapının iki katla sınırlı olması, insan sayısının 100’den fazla olmaması)"#input("Özel tehlike olması halinde bağıl kayıp miktarını arttıran hz faktörü:")
        return self.H_Z
    def l_f_bul(self):
        self.L_F = "Hastane, otel, okul, kamu binası"#input("Yapıda fiziksel hasarla ilgili tipik yüzde kayıp :")
        return self.L_F
        """