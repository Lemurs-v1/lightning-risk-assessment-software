import pandas as pd

class LightningRiskCalculator_N_D:
    def __init__(self):
        self.N_G = None
        self.A_D = None
        self.C_D = None

    def n_d_belirle(self):
        def n_g_belirle():
            N_G = input("Toprağa yıldırım düşme yoğunluğunu giriniz: ")  # TÜRKİYE HARİTASINDAN ÇEKİLECEK
            if not N_G:
                T_D = float(input("Fırtınalı gün sayısını giriniz: "))
                N_G = 0.1 * T_D
            return float(N_G)

        def a_d_belirle():
            A_D = float(input("Yapı alanını giriniz: "))  # Genişlik ve uzunluk ayrı ayrı alınabilir
            return A_D

        def c_d_belirle():
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
            seçim = input("Bağıl konumu nedir: ")
            C_D = C_D_DF.loc[C_D_DF["bağıl konum"] == seçim, "C_D"].values[0]
            return C_D

        N_G = n_g_belirle()
        A_D = a_d_belirle()
        C_D = c_d_belirle()
        N_D = N_G * A_D * C_D
        return N_D
    



class LightningRiskCalculator_P_A:
    def __init__(self):
        self.P_TA=None
        self.P_B=None
    def p_a_belirle(self):
        def p_ta_belirle():
            data ={ "ilave koruma tedbirleri": [
                "koruma tedbiri yok",
                "uyarı işaretleri",
                "açıktaki bölümlerin elektriksel yalıtımları",
                "etkin zemin eş potansiyel kuşaklanması",
                "fiziksel kısıtlamalar ve indirme indirme iletkeni olarak kullanılan bina iskeleti"
                ],
                "P_TA": [1,0.1,0.01,0.01,0]
                }
            P_TA_DF = pd.DataFrame(data)
            seçim = input("ilave koruma tedbiri nedir: ")
            P_TA = P_TA_DF.loc[P_TA_DF["ilave koruma tedbirleri"]==seçim,"P_TA"].values[0]
            return P_TA
        def p_b_belirle():
            data ={ "yapı karakteristikleri": [
                "yapı LPS ile korunumuyor",
                "yapı  4. seviye lps ile korunuyor",
                "yapı  3. seviye lps ile korunuyor",
                "yapı  2. seviye lps ile korunuyor",
                "yapı  1. seviye lps ile korunuyor",
                "LPS 1'e uygun yakalama ucu sistemine ve doğal indirme iletkeni olarak davranan sürekli metal veya takviyeli beton iskelete sahip yapı",
                "Metal çatiya ve çatidaki bütün tesisati dogrudan yildirim düsmesine karsi tamamen koruyan, muntemelen dogal bilesenler dahil, bir yakalama ucu sistemine ve dogal indirme iletkeni olarak davranan surekli metal veya takviyeli beton iskelete sahip yapi",
                ],
                "P_B": [1,0.2,0.1,0.05,0.02,0.01,0.001]
                }
            P_B_DF = pd.DataFrame(data)
            seçim = input("Yapı karakteristikliği nedir: ")
            P_B = P_B_DF.loc[P_B_DF["yapı karakteristikleri"]==seçim,"P_B"].values[0]
            return P_B
        P_TA = p_ta_belirle()
        P_B = p_b_belirle()
        P_A = P_B * P_TA
        return P_A
class LightningRiskCalculator_L_A:#test edilmeli pro bir şekilde
    def __init__(self):
        self.r_t = None
        self.L_T = None
        self.n_z_bölü_n_t = None
        self.n_t_bölü_8760 = None
    def l_a_belirle(self):
        def r_t_belirle():
            data ={ "yapı tipi": [
                "tarımsal, beton",
                "mermer, seramik",
                "çakıl, moket, halı",
                "asfalt, muşamba, ahşap",
                ],
                "r_t": [10**-2,10**-3,10**-4,10**-5]
                }
            r_t_DF = pd.DataFrame(data)
            seçim = input("yapı tipi nedir: ")
            r_t = r_t_DF.loc[r_t_DF["yapı tipi"]==seçim,"r_t"].values[0]
            return r_t
        def l_t_belirle():
            L_T= 10**-2
            return L_T
        def n_z_bölü_n_t_belirle():
            oran = input("yapıdaki ve bölgedeki kişi sayısı eşit mi: ")
            if oran == "evet":
                n_z_bölü_n_t = 1
            elif oran == "hayır":
                n_z = float(input("bölgedeki kişi sayısı nedir: "))
                n_t = float(input("yapıdaki kişi sayısı nedir: "))
                n_z_bölü_n_t = n_z/n_t
            else:
                print("geçerli ifade gir")
            return n_z_bölü_n_t
        def n_t_bölü_8760_belirle():#eror function yazılabilir bilmiyorum dışı bir sey girilmesi adına fakat seçimli yapacagımız için pek bir onemi yok
            cevap = input("kişiler bölgede yılda kaç saat bulunmakta (saat/bilmiyorum) ")
            if cevap == "bilmiyorum":
                cevap_son = 1
            else:
                cevap_son = float(cevap)/8760
            n_t_bölü_8760 = cevap_son

            return n_t_bölü_8760
        r_t = r_t_belirle()
        L_T = l_t_belirle()
        n_z_bölü_n_t = n_z_bölü_n_t_belirle()
        n_t_bölü_8760= n_t_bölü_8760_belirle()
        
        L_A = r_t*L_T*n_z_bölü_n_t*n_t_bölü_8760
        return L_A
class LightningRiskCalculator_R_A:
    def __init__(self):
        self.P_A = None
        self.L_A= None
        self.N_D = None
    def r_a_belirler(self):
        P_A = LightningRiskCalculator_P_A().p_a_belirle()
        N_D = LightningRiskCalculator_N_D().n_d_belirle()
        L_A = LightningRiskCalculator_L_A().l_a_belirle()
        R_A = P_A*L_A*N_D
        return R_A
