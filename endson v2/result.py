from top_deger import LightningRiskCalculator_top_values
import pandas as pd

top = LightningRiskCalculator_top_values()


class LightningRiskCalculator_result():
    def __init__(self):
        with open("kullanıcı_değer.txt", "r",encoding="utf-8") as dosya:
            self.veriler_file = dosya.read()

        self.veriler = self.veriler_file.split("\n")
        self.R1_value=str(self.veriler[55])
        self.R4_value=str(self.veriler[56])
        self.R_1 =None
        self.R_2 = None
        self.R_3 = None
        self.R_4 = None
        self.R_A_1 = top.r_a_1_belirle()
        self.R_B_1 = top.r_b_1_belirle()
        self.R_C_1 = top.r_c_1_belirle()
        self.R_M_1 = top.r_m_1_belirle()
        self.R_U_1 = top.r_u_1_belirle()
        self.R_V_1 = top.r_v_1_belirle()
        self.R_W_1 = top.r_w_1_belirle()
        self.R_Z_1 = top.r_z_1_belirle()

        self.R_B_2 = top.r_b_2_belirle()
        self.R_C_2 = top.r_c_2_belirle()
        self.R_M_2 = top.r_m_2_belirle()
        self.R_V_2 = top.r_v_2_belirle()
        self.R_W_2 = top.r_w_2_belirle()
        self.R_Z_2 = top.r_z_2_belirle()

        self.R_B_3 = top.r_b_3_belirle()
        self.R_V_3 = top.r_b_4_belirle()


        self.R_A_4 = top.r_a_4_belirle()
        self.R_B_4 = top.r_b_4_belirle()
        self.R_C_4 = top.r_c_4_belirle()
        self.R_M_4 = top.r_m_4_belirle()
        self.R_U_4 = top.r_u_4_belirle()
        self.R_V_4 = top.r_v_4_belirle()
        self.R_W_4 = top.r_w_4_belirle()
        self.R_Z_4 = top.r_z_4_belirle()




    def R_1_belirle(self):
        soru_1 = self.R1_value#input("Yapıda patlama riski veya elektriksel sistemlerin arızalanması durumunda insan hayatını direkt tehlike altına alacak bir durum mevcut mu ? (evet/hayır)")
        if (soru_1 == "Evet"):
            self.R_1 = self.R_A_1+self.R_B_1+self.R_U_1+self.R_V_1+(self.R_C_1+self.R_M_1+self.R_W_1+self.R_Z_1)
        elif(soru_1 == "Hayır"):
            self.R_1 = self.R_A_1+self.R_B_1+self.R_U_1+self.R_V_1
        return self.R_1
    def R_2_belirle(self):
        self.R_2 = self.R_B_2+self.R_C_2+self.R_M_2+self.R_V_2+self.R_W_2+self.R_Z_2
        return self.R_2
    def R_3_belirle(self):
        self.R_3 = self.R_B_3+self.R_V_3
        return self.R_3
    def R_4_belirle(self):
        soru = self.R4_value#input("Sadece hayvan kaybı riski mi mevcut ? (evet/hayır)")
        if (soru=="Evet"):
            self.R_4 = self.R_B_4+self.R_C_4+self.R_M_4+self.R_V_4+self.R_W_4+self.R_Z_4+(self.R_A_4+self.R_U_4)
        elif(soru=="Hayır"):
            self.R_4 = self.R_B_4+self.R_C_4+self.R_M_4+self.R_V_4+self.R_W_4+self.R_Z_4
        return self.R_4
    def R_tespit(self):
<<<<<<< Updated upstream
        değerler = [self.R_1_belirle(), self.R_2_belirle(), self.R_3_belirle(), self.R_4_belirle()]
        with open("sonuc.txt", "w", encoding="utf-8") as dosya:
            for değer in değerler:
                dosya.write(f"{değer}#")
x = LightningRiskCalculator_result()
x.R_tespit()
=======
        # self burada bir sınıf içinde olmalı, self'den önce bir sınıf tanımlı olduğunu varsayıyorum
        degerler = [self.R_1_belirle(), self.R_2_belirle(), self.R_3_belirle(), self.R_4_belirle()]

        # v listesinin uzunluğunu kontrol etme
        if len(degerler) >= 4:
            v_a = ['R_1', 'R_2', 'R_3', 'R_4']
            degerler = [[degerler[0], degerler[1], degerler[2], degerler[3]]]  # İndeksler 0'dan 3'e kadar olmalı
        else:
            raise IndexError(f"v listesi beklenen uzunlukta değil: {len(degerler)}")

        # DataFrame oluşturma
        f = pd.DataFrame(degerler, columns=v_a)

        # DataFrame'i CSV dosyasına kaydetme
        f.to_csv('veriler.csv', index=False)

 
 
>>>>>>> Stashed changes


x = LightningRiskCalculator_result()
x.R_tespit()