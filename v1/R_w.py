import pandas as pd

class N_l():
    def __init__(self) -> None:
        pass
    
    def N_g_belirle(self):
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
    


class N_dj():
    def __init__(self) -> None:
        pass
    def N_g_belirlee(self):# 2tane e ile bitiyor çünkü yukarda tanımlı bir daha tanımlamak istemedim.
        pass
    def A_dj_belirle(self): #A_d bitişik yapının toplama alanı. anlayan, anlamayana anlatsın amk.
        pass
    def C_dj_belirlee(self): #C_dj aslında C_T ile aynı tabloyu kullanıyor incelenebilir.
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
    
    def P_ld_belirle(self):
        
        self.P_ld_cevap = input("Güç hatları veya telekominikasyon hatlarının güzergah, zırhlama ve kuşaklama şartları hangisidir ?")
        if self.P_ld_cevap == "evet": #Havai veya gömülü hat, zırhlanmamış veya zırhı donanım gibi aynı kuşaklama barasına bağlanan zırhlanmış ise =>> "evet"
            sonuc = int(1)
        elif self.P_ld_cevap == "hayır": #Zırhı donanım gibi aynı kuşaklama barasına bağlanan zırhlanmış havai veya gömülü ise =>> "hayır"
            data = {
                "5 Ω /km <RS ≤ 20 Ω /km" :[
                    "1",
                    "1",
                    "0.95",
                    "0.9",
                    "0.8"
                ],
                "1 Ω /km <RS ≤ 5 Ω /km" :[
                    "0.9",
                    "0.8",
                    "0.6",
                    "0.3",
                    "0.1"
                ],
                "RS ≤ 1 Ω /km" :[
                    "0.6",
                    "0.4",
                    "0.2",
                    "0.04",
                    "0.02"

                ]
                
            }
            secim1 = input("Direnç değerini giriniz :")
            secim2 = input("Dayanım gerilimini giriniz :") 
            sonuc = data[secim1][secim2]
        return sonuc       
    
    def C_ld_belirle(self):
        pass

class L_w():
    def __init__(self) -> None:
        pass
    def L_o_belirle(self):
        pass #output da belirlenmiş

        
