from top_deger import LightningRiskCalculator_top_values

top = LightningRiskCalculator_top_values()

class LightningRiskCalculator_result():
    def __init__(self):
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
        soru = "evet"#input("Yapıda patlama riski veya elektriksel sistemlerin arızalanması durumunda insan hayatını direkt tehlike altına alacak bir durum mevcut mu ? (evet/hayır)")
        if (soru == "evet"):
            self.R_1 = self.R_A_1+self.R_B_1+self.R_U_1+self.R_V_1+(self.R_C_1+self.R_M_1+self.R_W_1+self.R_Z_1)
        elif(soru == "hayır"):
            self.R_1 = self.R_A_1+self.R_B_1+self.R_U_1+self.R_V_1
        return self.R_1
    def R_2_belirle(self):
        self.R_2 = self.R_B_2+self.R_C_2+self.R_M_2+self.R_V_2+self.R_W_2+self.R_Z_2
        return self.R_2
    def R_3_belirle(self):
        self.R_3 = self.R_B_3+self.R_V_3
        return self.R_3
    def R_4_belirle(self):
        soru = "evet"#input("Sadece hayvan kaybı riski mi mevcut ? (evet/hayır)")
        if (soru=="evet"):
            self.R_4 = self.R_B_4+self.R_C_4+self.R_M_4+self.R_V_4+self.R_W_4+self.R_Z_4+(self.R_A_4+self.R_U_4)
        elif(soru=="hayır"):
            self.R_4 = self.R_B_4+self.R_C_4+self.R_M_4+self.R_V_4+self.R_W_4+self.R_Z_4
        return self.R_4
    
start = LightningRiskCalculator_result()

print(start.R_1_belirle())
print(start.R_2_belirle())
print(start.R_3_belirle())
print(start.R_4_belirle())

değerler = f"{start.R_1_belirle()}#{start.R_2_belirle()}#{start.R_3_belirle()}#{start.R_4_belirle()}"
with open("sonuc.txt", "w") as dosya:
    dosya.write(değerler)