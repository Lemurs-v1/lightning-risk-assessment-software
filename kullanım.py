from LightningRiskCalculator import LightningRiskCalculator_N_D
from LightningRiskCalculator import LightningRiskCalculator_P_A
from LightningRiskCalculator import LightningRiskCalculator_L_A

N_D = LightningRiskCalculator_N_D()
P_A = LightningRiskCalculator_P_A()
L_A = LightningRiskCalculator_L_A()
P_A_SON = P_A.p_a_belirle()
N_D_SON = N_D.n_d_belirle()
L_A_SON = L_A.l_a_belirle()
R_A = P_A_SON*L_A_SON*N_D_SON

print(R_A)