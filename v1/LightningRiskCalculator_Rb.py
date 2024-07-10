import pandas as pd
from LightningRiskCalculator_Ra import LightningRiskCalculator_N_D


class LightningRiskCalculator_P_B:
    def __init__(self):
        self.P_B=None
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
        P_B = p_b_belirle()
        return P_B
    
class LihtningRiskCalculator_L_B:
    def __init__(self):
        self.r_p = None
        self.r_f = None
        self.h_z = None
        self.L_f = None
        self.n_z_bolu_n_t = None
        self.t_z_bolu_8760 = None
    def L_B_belirle(self):
        def r_p_belirle(self):
            data = {"tedbirler":
                ["tedbir yok",
                "Aşağıdaki tedbirlerden biri: Yangın söndürücüler, elle çalıştırılan sabit yangın söndürme tesisleri, elle çalıştırılan alarm tesisleri, hidrantlar, yangına karşı korunmalı bölmeler, kaçış güzergâhları.",
                "Aşağıdaki tedbirlerden biri: Otomatik sabit yangın söndürme tesisleri, otomatik alarm tesisleri",
                "Patlama riski var"
                ],
                "r_p" : [1,0.5,0.2,1] 
            }
            r_p_DF = pd.DataFrame(data)
            secim = input("Yangın tedbiri sonucu kayıp azaltma faktörü nedir ?")
            r_p = r_p_DF.loc[r_p_DF["tedbirler"]==secim,"r_p"].values[0]
            return r_p
       
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
            secim = input("Yangın riskine bağlı azalma faktörü nedir")
            r_f = r_f_DF.loc[r_f_DF["risk tutarı"]==secim,"r_f"].values(0)
            return r_f
       
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
            secim = input("Özel tehlike olması halinde bağıl kayıp miktarını arttıran hz faktörü:")
            h_z = h_z_DF.loc[h_z_DF["özel tehlike cinsi"]==secim,"h_z"].values(0)
            return h_z
        
        def L_f_belirle(self):
            data = { "yüzde kayıp" : 
                    [
                        "Patlama riski",
                        "Hastane, otel, okul, kamu binası"
                        "Halka açık eğlence yeri, ibadethane, müze"
                        "Sanayi, ticari"
                        "Diğerleri"
                    ],
                    "L_z" : [0.1,0.1,0.05,0.02,0.01]
            }
            L_f_DF = pd.DataFrame(data)
            secim = input("Yapıda fiziksel hasarla ilgili tipik yüzde kayıp :")
            L_f = L_f_DF.loc[L_f_DF["yüzde kayıp"]==secim,"L_f"].value(0)
            return L_f
