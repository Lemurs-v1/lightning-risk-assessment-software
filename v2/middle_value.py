from min_values import LightningRiskCalculator_min_values
min = LightningRiskCalculator_min_values()
class LightningRiskCalculator_middle_values:
    def __init__(self):
        #######################RA
        #######################
        self.N_D = None
        self.N_G = min.n_g_belirle()
        self.A_D = min.a_d_belirle()
        self.C_D = min.c_d_belirle()
        ############################
        self.P_A=None
        self.P_TA = min.p_ta_belirle()
        self.P_B = min.p_b_belirle()
        ###########################
        self.L_A =None
        self.r_t = min.r_t_belirle() 
        self.L_t= min.l_t_belirle()
        self.nz_bölü_nt = min.n_z_bölü_n_t_belirle()
        self.tz_bölü_8760 = min.t_z_bölü_8760_belirle()
        #############################RM
        #############################
        self.N_M = None
        self.A_M = min.a_m_belirle()
        ##############################
        self.P_M = None
        self.P_SPD = min.p_spd_belirle()
        self.P_MS = min.p_ms_belirle()
        #############################
        self.L_M = None
        self.L_O = min.l_o_belirle()
        ##############################
        #############################
        self.P_C = None
        self.C_LD = min.c_ld_belirle()
        ##################################
        #################################

    def n_d_belirle(self):
        self.N_D = self.N_G*self.A_D[0]*self.C_D
        return self.N_D
    def p_a_belirleme(self):
        self.P_A = self.P_TA*self.P_B
        return self.P_A
    def l_a_belirle(self):
        self.L_A = self.r_t*self.L_t*self.nz_bölü_nt*self.tz_bölü_8760
        return self.L_A
    ##############################
    ###########################
    def p_c_belirle(self):
        self.P_C = self.P_SPD*self.C_LD
        return self.P_C
    #####################################################################################
    #####################################################################################3
    def n_m_belirle(self):
        self.N_M = self.N_G* self.A_M*(10**-6)
        return self.N_M 
    def p_m_belirle(self):
        self.P_M = self.P_SPD*self.P_MS 
        return self.P_M
    def l_m_belirle(self):#LC=LM=LZ=LW(L1 İÇİN)
        self.L_M = self.L_O*self.nz_bölü_nt*self.tz_bölü_8760
        return self.L_M
    #######################################################################################
        
        
x = LightningRiskCalculator_middle_values()
print(x.p_m_belirle())


