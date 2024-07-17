import pandas as pd

def P_ld_belirle():
    P_ld_cevap = input("Güç hatları veya telekominikasyon hatlarının güzergah, zırhlama ve kuşaklama şartları hangisidir? ")
    if P_ld_cevap == "evet":
        sonuc = 1
    elif P_ld_cevap == "hayır":
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
        print(df)
        secim1 = input("Direnç değerini giriniz: ")
        secim2 = input("Dayanım gerilimini giriniz (1-1,5-2,5-4-6): ")
        
        sonuc = df.loc[(df['Direnç Değeri'] == secim1) & (df['Dayanım Gerilimi'] == secim2), 'Değer'].values[0]
    
    return sonuc  

x = P_ld_belirle()
print(x)
