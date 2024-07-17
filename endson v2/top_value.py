
from middle_value import LightningRiskCalculator_middle_values
mid = LightningRiskCalculator_middle_values()
class LightningRiskCalculator_top_values:

    def __init__(self):
        self.R_A_1 = None
        self.N_D = mid.n_d_belirle()
        self.P_A = mid.p_a_belirle()
        self.L_A = mid.l_a_belirle()
        self.R_B_1 = None
        self.R_C_1 = None
        self.R_M_1 = None
        self.R_U_1 = None
        self.R_V_1 = None
        self.R_W_1 = None
        self.R_Z_1 = None
    def r_a_1_belirle(self):
        self.R_A_1 =self.N_D*self.P_A*self.L_A
        return self.R_A_1
    
        
x = LightningRiskCalculator_top_values()
print(x.r_a_1_belirle())     