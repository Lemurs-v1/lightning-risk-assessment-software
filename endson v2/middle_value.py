from min_values import LightningRiskCalculator_min_values
import traceback
import re

min = LightningRiskCalculator_min_values()


class LightningRiskCalculator_middle_values:
    def __init__(self):
        #######################RA
        #######################

        self.N_D = None
        self.N_G = min.n_g_belirle()
        self.A_D = min.a_d_belirle()
        self.C_D = min.c_d_belirle()
        self.C_DJ = min.c_dj_belirle()
        self.N_DJ = None
        self.A_Dj = min.a_dj_belirle()
        ############################
        self.P_A=None
        self.P_TA = min.p_ta_belirle()
        self.P_B = min.p_b_belirle()
        ###########################
        self.L_AU_1 =None
        self.r_t = min.r_t_belirle() 
        self.L_t_1= min.l_t_belirle()
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
        self.L_CMWZ_1 = None
        self.L_O_1 = min.l_o_belirle()
        ##############################
        #############################
        self.P_C = None
        self.C_LD = min.c_ld_belirle()
        ##################################
        #################################
        self.L_BV_1 = None
        self.r_p = min.r_p_belirle()
        self.r_f = min.r_f_belirle()
        self.h_z = min.h_z_belirle()
        self.L_F_1 = min.l_f_belirle()
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
        ###################
        self.L_BV_2 = None
        self.L_F_2 = min.l_f_2_belirle()
        self.L_CMWZ_2 = None
        self.L_O_2 = min.l_o_2_belirle()
        ###############################
        self.L_BV_3 = None
        self.L_F_3 = min.l_f_3_belirle()
        self.c_z_bölü_c_t = min.c_z_bölü_c_t()

        self.L_AU_4 = None
        self.L_T_4 = min.l_t_4_belirle()
        self.c_a_bölü_ct = min.c_a_bölü_c_t()
        self.L_F_4= min.l_f_4_belirle()
        self.L_O_4 = min.l_o_4_belirle()
        self.L_BV_4 =None
        self.L_CMWZ = None




    def n_d_belirle(self):
        self.N_D = self.N_G*self.A_D*self.C_D*10**-6
        return self.N_D
    def p_a_belirle(self):
        self.P_A = self.P_TA*self.P_B
        return self.P_A
    def l_au_1_belirle(self):
        self.L_AU_1 = self.r_t*self.L_t_1*self.nz_bölü_nt*self.tz_bölü_8760
        return self.L_AU_1
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
    def l_cmwz_1_belirle(self):#LC=LM=LZ=LW(L1 İÇİN)
        self.L_MCZW_1 = self.L_O_1*self.nz_bölü_nt*self.tz_bölü_8760
        return self.L_MCZW_1
    #######################################################################################
    #######################################################################################
    
    def l_bv_1_belirle(self):#LB=LV
        self.L_BV_1=self.L_F_1*self.h_z*self.nz_bölü_nt*self.tz_bölü_8760*self.r_p*self.r_f
        return self.L_BV_1
        
    ###################################################################################333
    ###################################################################################333
    
    def n_l_belirle(self):
        self.N_L = self.N_G*self.A_L*self.C_I*self.C_T*self.C_E*10**-6
        return self.N_L
    def n_dj_belirle(self):#İhmal ADJ ANLAMIA BAKILDIGINDA EKLENEBİLİR
        self.N_DJ = self.N_G*self.A_Dj*self.C_DJ*self.C_T*(10**-6)
        return self.N_DJ
    def p_w_belirle(self):#GİRİLMEMİŞ girelecek 
        self.P_W = self.P_LD*self.P_SPD*self.C_LD
        return self.P_W
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
#bu işlemler yapılırken c_abcd ve c_t yaklasık 1 alındı
    def p_b_belirle(self):
        return self.P_B
    def l_bv_2_belirle(self):
        self.L_BV_2=  self.r_p*self.r_f*self.L_F_2*self.nz_bölü_nt
        return self.L_BV_2
    def l_cmwz_2_belirle(self):
        self.L_CMWZ_2 = self.L_O_2*self.nz_bölü_nt
        return self.L_CMWZ_2
    
    def l_bv_3_belirle(self):
        self.L_BV_3 = self.r_p*self.r_f*self.L_F_3*self.c_z_bölü_c_t
        return self.L_BV_3
    
    def l_au_4_belirle(self):
        self.L_AU_4 =self.r_t*self.L_T_4*self.c_a_bölü_ct
        return self.L_AU_4
    def l_bv_4_belirle(self):
        self.L_BV_4 =self.r_p*self.r_f*self.L_F_4*1
        return self.L_BV_4
    def l_cmwz_4_belirle(self):
        self.L_CMWZ_4 = self.L_O_4*self.c_a_bölü_ct
        return self.L_CMWZ_4
"""    
x = LightningRiskCalculator_middle_values()
print("4444asdasad444")
print(x.l_au_4_belirle())
print(x.l_bv_4_belirle())
print(x.l_cmwz_4_belirle())


print(x.p_m_belirle())
print(x.n_m_belirle())
print(x.p_c_belirle())

print(x.p_a_belirle())
print(x.n_d_belirle())

print(x.n_l_belirle())
print(x.p_u_belirle())
print(x.p_v_belirle())
print(x.n_ı_belirle())
print(x.p_z_belrile())
"""