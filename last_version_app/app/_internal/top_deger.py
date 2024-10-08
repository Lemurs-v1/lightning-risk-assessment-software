from middle_value import LightningRiskCalculator_middle_values
mid = LightningRiskCalculator_middle_values()
class LightningRiskCalculator_top_values:

    def __init__(self):
        self.R_A_1 = None
        self.N_D = mid.n_d_belirle()
        self.P_A = mid.p_a_belirle()
        self.L_A = self.L_U = mid.l_au_1_belirle()
        self.R_B_1 = None
        self.P_B = mid.p_b_belirle()
        self.L_B =self.L_V= mid.l_bv_1_belirle()
        self.R_C_1 = None
        self.P_C = mid.p_c_belirle()
        self.L_C = self.L_M = self.L_W = self.L_Z_1 = mid.l_cmwz_1_belirle()
        self.R_M_1 = None
        self.N_M = mid.n_m_belirle()
        self.P_M = mid.p_m_belirle()
        self.R_U_1 = None
        self.N_L = mid.n_l_belirle()
        self.N_DJ = mid.n_dj_belirle()
        self.P_U = mid.p_u_belirle()
        self.R_V_1 = None
        self.P_V = mid.p_v_belirle()
        self.R_W_1 = None
        self.P_W = mid.p_w_belirle()
        self.R_Z_1 = None
        
        self.R_Z_2 = None
        self.R_B_2 = None
        self.L_B_2 = self.L_V_2 = mid.l_bv_2_belirle()
        self.R_C_2 = None
        self.L_C_2 = self.L_M_2 = self.L_W_2 = self.L_Z_2 = mid.l_cmwz_2_belirle()
        self.R_M_2 = None
        self.R_W_2 = None
        self.R_V_2 = None
        self.R_Z_2 = None
        self.N_I = mid.n_ı_belirle()
        self.P_Z = mid.p_z_belrile()

        self.R_B_3 = None
        self.L_B_3 = self.L_V_3 =  mid.l_bv_3_belirle()

        self.R_A_4 = None
        self.L_A_4 = self.L_U_4 = mid.l_au_4_belirle()
        self.R_B_4 = None
        self.L_B_4 = self.L_V_4 = mid.l_bv_4_belirle()
        self.R_C_4 = None
        self.L_C_4 = self.L_M_4 = self.L_W_4 = self.L_Z_4 = mid.l_cmwz_4_belirle()
        self.R_M_4 = None
        self.R_U_4 = None
        self.R_V_4 = None
        self.R_W_4 = None
        self.R_Z_4 = None


    def r_a_1_belirle(self):
        self.R_A_1 = self.N_D*self.P_A*self.L_A
        return self.R_A_1
    def r_b_1_belirle(self):
        self.R_B_1 = self.N_D*self.P_B*self.L_B
        return self.R_B_1
    def r_c_1_belirle(self):
        self.R_C_1 = self.N_D*self.P_C*self.L_C
        return self.R_C_1
    def r_m_1_belirle(self):
        self.R_M_1 = self.N_M*self.P_M*self.L_M
        return self.R_M_1
    def r_u_1_belirle(self):
        self.R_U_1 = (self.N_L + self.N_DJ)*self.P_U*self.L_U
        return self.R_U_1
    def r_v_1_belirle(self):
        self.R_V_1 = (self.N_L + self.N_DJ)*self.P_V*self.L_V
        return self.R_V_1
    def r_w_1_belirle(self):
        self.R_W_1 = (self.N_L + self.N_DJ)*self.P_W*self.L_W
        return self.R_W_1
    def r_z_1_belirle(self):
        self.R_Z_1 = self.N_I*self.P_Z*self.L_Z_1
        return self.R_Z_1
    
    #r2 icin r'ler

    def r_b_2_belirle(self):
        self.R_B_2 = self.N_D*self.P_B*self.L_B_2
        return self.R_B_2
    def r_c_2_belirle(self):
        self.R_C_2 = self.N_D*self.P_C*self.L_C_2
        return self.R_C_2
    def r_m_2_belirle(self):
        self.R_M_2 = self.N_M*self.P_M*self.L_M_2
        return self.R_M_2
    def r_v_2_belirle(self):
        self.R_V_2 = (self.N_L + self.N_DJ)*self.P_V*self.L_V_2
        return self.R_V_2
    def r_w_2_belirle(self):
        self.R_W_2 = (self.N_L + self.N_DJ)*self.P_W*self.L_W_2
        return self.R_W_2
    def r_z_2_belirle(self):
        self.R_Z_2 = self.N_I*self.P_Z*self.L_Z_2
        return self.R_Z_2
    
    #r3 icin r'ler

    def r_b_3_belirle(self):
        self.R_B_3 = self.N_D*self.P_B*self.L_B_2
        return self.R_B_3
    def r_v_3_belirle(self):
        self.R_V_3 = (self.N_L + self.N_DJ)*self.P_V*self.L_V_3
        return self.R_V_3
    
    #r4 icin r'ler

    def r_a_4_belirle(self):
        self.R_A_4 = self.N_D*self.P_A*self.L_A_4
        return self.R_A_4
    def r_b_4_belirle(self):
        self.R_B_4 = self.N_D*self.P_B*self.L_B_4
        return self.R_B_4
    def r_c_4_belirle(self):
        self.R_C_4 = self.N_D*self.P_C*self.L_C_4
        return self.R_C_4
    def r_m_4_belirle(self):
        self.R_M_4 = self.N_M*self.P_M*self.L_M_4
        return self.R_M_4
    def r_u_4_belirle(self):
        self.R_U_4 = (self.N_L + self.N_DJ)*self.P_U*self.L_U_4
        return self.R_U_4
    def r_v_4_belirle(self):
        self.R_V_4 = (self.N_L + self.N_DJ)*self.P_V*self.L_V_4
        return self.R_V_4
    def r_w_4_belirle(self):
        self.R_W_4 = (self.N_L + self.N_DJ)*self.P_W*self.L_W_4
        return self.R_W_4
    def r_z_4_belirle(self):
        self.R_Z_4 = self.N_I*self.P_Z*self.L_Z_4
        return self.R_Z_4
    
    
x = LightningRiskCalculator_top_values()
print("mmmmmmmmmmmmmmmmmmmmmm")
print(x.r_a_1_belirle())
print(x.r_b_1_belirle())
print(x.r_c_1_belirle())
print(x.r_m_1_belirle())
print(x.r_u_1_belirle())
print(x.r_v_1_belirle())
print(x.r_w_1_belirle())
print(x.r_z_1_belirle())
print("mmmmmmmmm")

print(x.r_b_2_belirle())
print(x.r_c_2_belirle())
print(x.r_m_2_belirle())
print(x.r_v_2_belirle())
print(x.r_w_2_belirle())
print(x.r_z_2_belirle())

print(x.r_b_3_belirle())
print(x.r_v_3_belirle())
print("annna")

print(x.r_a_4_belirle())
print(x.r_b_4_belirle())
print(x.r_c_4_belirle())
print(x.r_m_4_belirle())
print(x.r_u_4_belirle())
print(x.r_v_4_belirle())
print(x.r_w_4_belirle())
print(x.r_z_4_belirle())
print("mmmmmmmmmmmmmmmmmmmmmm")
