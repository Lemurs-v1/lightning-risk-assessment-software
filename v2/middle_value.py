from min_values import LightningRiskCalculator_min_values
min = LightningRiskCalculator_min_values()
class LightningRiskCalculator_middle_values:
    def __init__(self):
        self.N_D = None
        self.L_A = None
        self.P_A = None
        self.N_G = None
        self.A_M = None
    def n_d_belirle(self):
        self.N_G = min.n_g_belirle()
        self.A_D = min.a_d_belirle()
        self.C_D = min.c_d_belirle()
        self.N_D = self.N_G*self.A_D[0]*self.C_D
        return self.N_D
    def p_a_belirleme(self):
        self.P_A = min.p_ta_belirle()*min.p_b_belirle()
        return self.P_A
    def l_a_belirle(self):
        self.L_A = min.r_t_belirle()*min.l_t_belirle()*min.n_z_bölü_n_t_belirle()*min.t_z_bölü_8760_belirle()
    #####################################################################################3
    def n_m_belirle(self):
        self.A_M = min.a_m_belirle()
        self.N_M = self.N_G* self.A_M
        return self.N_M    
x = LightningRiskCalculator_middle_values()
print(x.n_d_belirle())
print(x.n_m_belirle())

