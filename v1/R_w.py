import pandas as pd

class N_l():
    def __init__(self) -> None:
        pass
    def A_l_belirle(self):
        self.A_l = 40* self.L_l
        self.L_l = input("Hat kısmının uzunluğu :")
    
    def C_ı_belirle(self):
        data = {
            "Güzergah" : ["Havai","Gömülü","Tamamiyle bir kafes biçimindeki toprak sonlandırma uclarına giden gömülü kablolar (EN 62305-4:2011, Madde 5.2)"
            ],
            "C_ı" : [1,0.5,0.01]
        }
        C_ı_DF = pd.DataFrame(data)
        seçim = input("Güzergah türü nedir ?")
        C_ı = C_ı_DF.loc[C_ı_DF["Güzergah"]==seçim,"C_ı"].values[0]
        return C_ı
    
    def C_t_belirle(self):
        data = {
            "Tesisat" : [
                "AG güç, telekomünikasyon veya veri hattı",
                "YG güç (YG/AG transformatörü ile)"
            ],
            "C_t" : [1,0.2]
        }
        C_t_DF = pd.DataFrame(data)
        seçim = input("Tesisat türü nedir?")
        C_t = C_t_DF.loc[C_t_DF["Tesisat"]== seçim,"C_t"].values[0]
        return C_t
    
    def C_e_belirle(self):
        data = {
            "Çevre" : [
                "Kırsal",
                "Banliyo",
                "Şehir",
                "Büyük binaların olduğu şehir(20m'den yüksek.)"
            ],
            "C_t" : [1,0.5,0.1,]
        }
        C_e_DF = pd.DataFrame(data)
        seçim = input("Çevre türü nedir?")
        C_e = C_e_DF.loc[C_e_DF["Çevre"]== seçim,"C_e"].values[0]
        return C_e
    


class N_dt():
    def __init__(self) -> None:
        pass
class P_w():
    def __init__(self) -> None:
        pass

    def P_spd_belirle(self):
        data = {
            "Korunma tedbiri" : ["SPD yok","3-4","2","1"],
            "P_spd":[1,0.05,0.02,0.01,]
        }
        P_spd_DF = pd.DataFrame(data)
        seçim = input("SPD’lerin tasarımlandığı LPL’nin fonksiyonu olarak PSPD ihtimali değeri")
        P_SPD = P_spd_DF.loc[P_spd_DF["korunma tedbiri"]== seçim,"P_spd"].values[0]
        return P_SPD
    
    def P_lb_belirle(self):
        
    def C_ld_belirle(self):
        pass

class L_w():
    def __init__(self) -> None:
        pass

        
