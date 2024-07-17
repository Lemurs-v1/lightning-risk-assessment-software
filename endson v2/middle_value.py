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
        ##########################s###RM
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
        self.L_B = None
        self.r_p = min.r_p_belirle()
        self.r_f = min.r_f_belirle()
        self.h_z = min.h_z_belirle()
        self.L_F = min.l_f_belirle()
        #################################3
        ##################################
        self.N_L = None
        self.A_L = min.a_l_belirle()
        self.C_I = min.c_ı_belirle()
        self.C_T = min.C_t_belirle()
        self.C_E = min.C_e_belirle()

        self.P_W = None

        self.P_TU = min.p_tu_belirle()
        self.P_EB = min.p_eb_belirle()
        self.P_LD = min.p_ld_belirle()

        self.P_V = None
        self.N_I =None

        self.A_I = min.a_ı_belirle()
        self.P_LI = min.p_lı_belirle()
        self.P_Z = None
        
        self.C_LI = min.c_lı_belirle()


    def n_d_belirle(self):
        self.N_D = self.N_G*self.A_D*self.C_D*10**-6
        return self.N_D
    def p_a_belirle(self):
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
        self.N_M = self.N_G* self.A_M*10**-6
        return self.N_M 
    def p_m_belirle(self):
        self.P_M = self.P_SPD*self.P_MS 
        return self.P_M
    def l_m_belirle(self):#LC=LM=LZ=LW(L1 İÇİN)
        self.L_M = self.L_O*self.nz_bölü_nt*self.tz_bölü_8760
        return self.L_M
    #######################################################################################
    #######################################################################################
    
    def l_b_belirle(self):#LB=LV
        self.L_B=self.L_F*self.h_z*self.nz_bölü_nt*self.tz_bölü_8760*self.r_p*self.r_f
        return self.L_B
        
    ###################################################################################333
    ###################################################################################333
    
    def n_l_belirle(self):
        self.N_L = self.N_G*self.A_L*self.C_I*self.C_T*self.C_E*10**-6
        return self.N_L
    def n_dj_belirle(self):#İhmal ADJ ANLAMIA BAKILDIGINDA EKLENEBİLİR
        return 0
    def p_w_belirle(self):#GİRİLMEMİŞ girelecek 
        self.P_W = self.P_LD*self.P_SPD*self.C_LD
    def p_u_belirle(self):
        self.P_U=self.P_LD*self.P_TU*self.P_EB*self.C_LD
        return self.P_U
    def p_v_belirle(self):
        self.P_V = self.P_EB*self.P_LD*self.C_LD
        return self.P_V
    
    def n_ı_belirle(self):
        self.N_I = self.N_G*self.A_I*self.C_I*self.C_E*self.C_T*((10)**-6)
        return self.N_I
    def  p_z_belrile(self):
        self.P_Z = self.C_LI*self.P_SPD*self.C_LI
        return self.P_Z

        

    
    
       
        
x = LightningRiskCalculator_middle_values()
print(x.l_m_belirle())
print(x.p_m_belirle())
print(x.n_m_belirle())
print(x.p_c_belirle())
print(x.l_a_belirle())
print(x.p_a_belirle())
print(x.n_d_belirle())
print(x.l_b_belirle())
print(x.n_l_belirle())
print(x.p_u_belirle())
print(x.p_v_belirle())
print(x.n_ı_belirle())
print(x.p_z_belrile())

