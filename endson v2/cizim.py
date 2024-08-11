import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from top_deger import LightningRiskCalculator_top_values
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator, MaxNLocator


top = LightningRiskCalculator_top_values()





class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super(MplCanvas, self).__init__(self.fig)
        
        with open("kullanıcı_değer.txt", "r",encoding="utf-8") as dosya:
            veriler_file = dosya.read()

        veriler = veriler_file.split("\n")

        self.Ad_y_double_C = float(veriler[33]) 
        self.Ad_g_double_C = float(veriler[34])  
        self.Ad_u_double_C = float(veriler[35])  
        self.Ad_ymax_double_C = float(veriler[48])


        self.Adj_g_double_C = float(veriler[36])  
        self.Adj_u_double_C = float(veriler[37])  
        self.Adj_y_double_C = float(veriler[49])
        self.Adj_ymax_double_C = float(veriler[50])


        self.Ad_durum = str(veriler[0])

        self.Adj_kontrol = str(veriler[4])
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
        self.R_V_3 = top.r_v_3_belirle()


        self.R_A_4 = top.r_a_4_belirle()
        self.R_B_4 = top.r_b_4_belirle()
        self.R_C_4 = top.r_c_4_belirle()
        self.R_M_4 = top.r_m_4_belirle()
        self.R_U_4 = top.r_u_4_belirle()
        self.R_V_4 = top.r_v_4_belirle()
        self.R_W_4 = top.r_w_4_belirle()
        self.R_Z_4 = top.r_z_4_belirle()
        self.categories_1 = ['RA', 'RB', 'RC', 'RM', 'RU', 'RV', 'RW', 'RZ']
        self.values_1 = [self.R_A_1, self.R_B_1, self.R_C_1,self.R_M_1,self.R_U_1,self.R_V_1,self.R_W_1,self.R_Z_1]

        self.categories_2 = ['RB', 'RC', 'RM', 'RV', 'RW', 'RZ']
        self.values_2 = [self.R_B_2, self.R_C_2,self.R_M_2,self.R_V_2,self.R_W_2,self.R_Z_2]

        self.categories_3 = ['RB', 'RV']
        self.values_3 = [self.R_B_3, self.R_V_3]

        self.categories_4 = ["RA",'RB', 'RC', 'RM', "RU",'RV', 'RW', 'RZ']
        self.values_4 = [self.R_A_4,self.R_B_4, self.R_C_4,self.R_M_4,self.R_U_4,self.R_V_4,self.R_W_4,self.R_Z_4]


    def grafik_1(self, constant_value_1=1e-5):
        # Grafiği oluşturma
        fig, ax = plt.subplots(figsize=(10, 6))

        # Değerlerin minimum ve maksimumlarını hesapla
        min_value = min(min(self.values_1), constant_value_1)
        max_value = max(max(self.values_1), constant_value_1)

        # Mavi çizginin görünmesini sağlamak için margin ekle
        margin = (max_value - min_value) * 0.1  # %10 margin

        # Y eksenini min ve max değerlere göre margin ile ayarlama
        ax.set_ylim(bottom=min_value - margin, top=max_value + margin)

        # Diğer değerleri çizme
        ax.plot(self.categories_1, self.values_1, color='red', marker="o", label='Values')

        # Düz çizgiyi çizme
        ax.plot(self.categories_1, [constant_value_1] * len(self.categories_1), color='blue', label='1e-5')

        # Başlık ve etiketler
        ax.set_title('Total')
        ax.grid(True)
        ax.set_xlabel('Categories')
        ax.set_ylabel('Values')
        ax.legend()
        plt.savefig('output_pdf_1/images/graph_1.png')


    def grafik_2(self, constant_value_2=1e-5):
        # Grafiği oluşturma
        fig, ax = plt.subplots(figsize=(10, 6))

        # Değerlerin minimum ve maksimumlarını hesapla
        min_value = min(min(self.values_2), constant_value_2)
        max_value = max(max(self.values_2), constant_value_2)

        # Mavi çizginin görünmesini sağlamak için margin ekle
        margin = (max_value - min_value) * 0.1  # %10 margin

        # Y eksenini min ve max değerlere göre margin ile ayarlama
        ax.set_ylim(bottom=min_value - margin, top=max_value + margin)

        # Diğer değerleri çizme
        ax.plot(self.categories_2, self.values_2, color='red', marker="o", label='Values')

        # Düz çizgiyi çizme
        ax.plot(self.categories_2, [constant_value_2] * len(self.categories_2), color='blue', label='1e-3')

        # Başlık ve etiketler
        ax.set_title('Total')
        ax.grid(True)
        ax.set_xlabel('Categories')
        ax.set_ylabel('Values')
        ax.legend()

        # PNG olarak kaydetme
        plt.savefig('output_pdf_1/images/graph_2.png')

    def grafik_3(self,constant_value_3=1e-4):
        # Grafiği oluşturma
        fig, ax = plt.subplots(figsize=(10, 6))

        # Değerlerin minimum ve maksimumlarını hesapla
        min_value = min(min(self.values_3), constant_value_3)
        max_value = max(max(self.values_3), constant_value_3)

        # Mavi çizginin görünmesini sağlamak için margin ekle
        margin = (max_value - min_value) * 0.1  # %10 margin

        # Y eksenini min ve max değerlere göre margin ile ayarlama
        ax.set_ylim(bottom=min_value - margin, top=max_value + margin)

        # Diğer değerleri çizme
        ax.plot(self.categories_3, self.values_3, color='red', marker="o", label='Values')

        # Düz çizgiyi çizme
        ax.plot(self.categories_3, [constant_value_3] * len(self.categories_3), color='blue', label='1e-4')

        # Başlık ve etiketler
        ax.set_title('Total')
        ax.grid(True)
        ax.set_xlabel('Categories')
        ax.set_ylabel('Values')
        ax.legend()

        # PNG olarak kaydetme
        plt.savefig('output_pdf_1/images/graph_3.png')

    def grafik_4(self,constant_value_4=1e-3):
        # Grafiği oluşturma
        fig, ax = plt.subplots(figsize=(10, 6))

        # Değerlerin minimum ve maksimumlarını hesapla
        min_value = min(min(self.values_4), constant_value_4)
        max_value = max(max(self.values_4), constant_value_4)

        # Mavi çizginin görünmesini sağlamak için margin ekle
        margin = (max_value - min_value) * 0.1  # %10 margin

        # Y eksenini min ve max değerlere göre margin ile ayarlama
        ax.set_ylim(bottom=min_value - margin, top=max_value + margin)

        # Diğer değerleri çizme
        ax.plot(self.categories_4, self.values_4, color='red', marker="o", label='Values')

        # Düz çizgiyi çizme
        ax.plot(self.categories_4, [constant_value_4] * len(self.categories_4), color='blue', label='1e-3')

        # Başlık ve etiketler
        ax.set_title('Total')
        ax.grid(True)
        ax.set_xlabel('Categories')
        ax.set_ylabel('Values')
        ax.legend()
        plt.savefig('output_pdf_1/images/graph_4.png')


    def plot_area_ad(self, l, w, h, hp):
        self.ax.clear()
        if True:
            # Dikdörtgenin köşe koordinatları
            x = [-l/2, l/2, l/2, -l/2, -l/2]
            y = [-w/2, -w/2, w/2, w/2, -w/2]
            
            
            self.ax.plot(x, y,)
            # Dikdörtgenin alanını doldur
            self.ax.fill(x, y, 'b', alpha=0.3, label="Yapı")

            # Genişletilmiş dikdörtgenin kenarlarını çiz
            self.ax.plot([x[0], x[1]], [y[0] - 3*h, y[1] - 3*h], 'r--')
            self.ax.plot([x[1] + 3*h, x[2] + 3*h], [y[1], y[2]], 'r--')
            self.ax.plot([x[2], x[3]], [y[2] + 3*h, y[3] + 3*h], 'r--')
            self.ax.plot([x[3] - 3*h, x[4] - 3*h], [y[3], y[4]], 'r--')

            # Köşelerde çeyrek çemberler çiz
            corners = [(-l/2, -w/2), (l/2, -w/2), (l/2, w/2), (-l/2, w/2)]
            for (cx, cy) in corners:
                if cx < 0 and cy < 0:
                    theta = np.linspace(np.pi, 3*np.pi/2, 100)
                elif cx > 0 and cy < 0:
                    theta = np.linspace(3*np.pi/2, 2*np.pi, 100)
                elif cx > 0 and cy > 0:
                    theta = np.linspace(0, np.pi/2, 100)
                elif cx < 0 and cy > 0:
                    theta = np.linspace(np.pi/2, np.pi, 100)
                
                x_arc = cx + 3 * h * np.cos(theta)
                y_arc = cy + 3 * h * np.sin(theta)
                self.ax.plot(x_arc, y_arc, 'r--')
            self.ax.plot(0,0,"r--",label = "Düz Yapı Alanı")

        if self.Ad_durum == "evet": # Karmaşık grafik çizimi (karmasik_grafik)
            circle_radius = 3 * hp
            circle = plt.Circle((0, 0), circle_radius, color='g', fill=False, linestyle='--', label="Karmaşık Yapı Alanı")
            self.ax.add_patch(circle)

        self.ax.xaxis.set_major_locator(MaxNLocator(nbins=6, prune='both'))  # X ekseninde en fazla 10 bölüm
        self.ax.yaxis.set_major_locator(MaxNLocator(nbins=6, prune='both')) 
        self.ax.xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))  # X eksenindeki etiket formatı
        self.ax.yaxis.set_major_formatter(FormatStrFormatter('%0.1f'))  # Y eksenindeki etiket formatı

        self.ax.legend(loc='upper right')
        self.ax.set_aspect('equal')
        self.draw()
        
        # Save the plot as a PNG file
        self.fig.savefig("output_pdf_1/images/complex_structure_ad.png")

    def plot_area_adj(self, l_a, w_a, h_a, hp_a):
        self.ax.clear()
        if True:
        # Dikdörtgenin köşe koordinatları
            x = [-l_a/2, l_a/2, l_a/2, -l_a/2, -l_a/2]
            y = [-w_a/2, -w_a/2, w_a/2, w_a/2, -w_a/2]
            
            
            self.ax.plot(x, y,)
            # Dikdörtgenin alanını doldur
            self.ax.fill(x, y, 'b', alpha=0.3, label="Ayrık Yapı")

            # Genişletilmiş dikdörtgenin kenarlarını çiz
            self.ax.plot([x[0], x[1]], [y[0] - 3*h_a, y[1] - 3*h_a], 'r--')
            self.ax.plot([x[1] + 3*h_a, x[2] + 3*h_a], [y[1], y[2]], 'r--')
            self.ax.plot([x[2], x[3]], [y[2] + 3*h_a, y[3] + 3*h_a], 'r--')
            self.ax.plot([x[3] - 3*h_a, x[4] - 3*h_a], [y[3], y[4]], 'r--')

            # Köşelerde çeyrek çemberler çiz
            corners = [(-l_a/2, -w_a/2), (l_a/2, -w_a/2), (l_a/2, w_a/2), (-l_a/2, w_a/2)]
            for (cx, cy) in corners:
                if cx < 0 and cy < 0:
                    theta = np.linspace(np.pi, 3*np.pi/2, 100)
                elif cx > 0 and cy < 0:
                    theta = np.linspace(3*np.pi/2, 2*np.pi, 100)
                elif cx > 0 and cy > 0:
                    theta = np.linspace(0, np.pi/2, 100)
                elif cx < 0 and cy > 0:
                    theta = np.linspace(np.pi/2, np.pi, 100)
                
                x_arc = cx + 3 * h_a * np.cos(theta)
                y_arc = cy + 3 * h_a * np.sin(theta)
                self.ax.plot(x_arc, y_arc, 'r--')
            self.ax.plot(0,0,"r--",label = "Düz Yapı Alanı")
        if self.Adj_y_double_C!=self.Adj_ymax_double_C:
            # Karmaşık grafik çizimi (karmasik_grafik)
            circle_radius = 3 * hp_a
            circle = plt.Circle((0, 0), circle_radius, color='g', fill=False, linestyle='--', label="Karmaşık Yapı Alanı")
            self.ax.add_patch(circle)

        self.ax.xaxis.set_major_locator(MaxNLocator(nbins=8, prune='both'))  # X ekseninde en fazla 10 bölüm
        self.ax.yaxis.set_major_locator(MaxNLocator(nbins=8, prune='both'))  # Y ekseninde her 1 birim için etiket
        self.ax.xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))  # X eksenindeki etiket formatı
        self.ax.yaxis.set_major_formatter(FormatStrFormatter('%0.1f'))  # Y eksenindeki etiket formatı

        self.ax.legend(loc='upper right')
        self.ax.set_aspect('equal')
        self.draw()
        
        # Save the plot as a PNG file
        self.fig.savefig("output_pdf_1/images/complex_structure_adj.png")
    
    def plot_area_adj_yok(self):
        self.ax.clear()
        self.fig.savefig("output_pdf_1/images/complex_structure_adj.png")
    def çizdir(self):
        l = self.Ad_u_double_C # Length
        w =  self.Ad_g_double_C  # Width
        h = self.Ad_y_double_C  # Height (min value)
        hp = self.Ad_ymax_double_C # Karmaşık yapı çıkıntı yüksekliği eklenecek
        self.plot_area_ad(l, w, h, hp)
        l_a = self.Adj_u_double_C # Length ayrık  
        w_a = self.Adj_g_double_C  # Width ayrık  
        h_a = self.Adj_y_double_C  # Height (min value) ayrık
        hp_a = self.Adj_ymax_double_C # Karmaşık yapı çıkıntı yüksekliği ayrık
        self.plot_area_adj(l_a, w_a, h_a, hp_a)
        if self.Adj_kontrol == "True" :
            self.plot_area_adj_yok()
        elif self.Adj_kontrol == "False":
            self.plot_area_adj(l_a, w_a, h_a, hp_a)
        self.grafik_1()
        self.grafik_2()
        self.grafik_3()
        self.grafik_4()

x = MplCanvas()
x.çizdir()





