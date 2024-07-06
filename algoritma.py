import pandas as pd

def N_G_BELIRLE():
    N_G = input("topraga yildirim düsme yogunlugunu giriniz: ")
    if not  N_G:
        T_D = float(input("fırtınalı gün sayısını giriniz: "))
        N_G = 0.1*T_D
    return N_G
        
        
def A_D_BELIRLE():
    A_D = float(input("yapı alanını giriniz:")) # genişlik ve uzunluk ayrı ayrı alınabilir 
    return A_D


def C_D_BELIRLE():
    data = {
        "bağıl konum":["Daha yüksek cisimler ile çevrelenen yapı" , 
            "Aynı yükseklikte veya daha alçak cisimler ile çevrelenen yapı" ,
              "Aynı yapı: yakında başka cisimlerin olmaması","Tepe veya tepecik üzerinde ayrık yapı"],
              "C_D":[0.25,0.5,1,2]
              }
    C_D_DF =  pd.DataFrame(data)

    seçim = input("Bağıl konumu nedir: ")
    C_D_sonuç = C_D_DF.loc[C_D_DF["bağıl konum"]== seçim,"C_D"].values[0]
    return C_D_sonuç

N_G=N_G_BELIRLE()
A_D=A_D_BELIRLE()
C_D=C_D_BELIRLE()
print (N_G,A_D,C_D)





