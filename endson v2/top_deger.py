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
        self.L_C = self.L_M = self.L_W = mid.l_cmwz_1_belirle()
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
    def r_a_1_belirle(self):
        self.R_A_1 =self.N_D*self.P_A*self.L_A
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
    
        
x = LightningRiskCalculator_top_values()
print(x.r_a_1_belirle())
print(x.r_b_1_belirle())
print(x.r_c_1_belirle())
print(x.r_m_1_belirle())
print(x.r_u_1_belirle())
print(x.r_v_1_belirle())
print(x.r_w_1_belirle())

