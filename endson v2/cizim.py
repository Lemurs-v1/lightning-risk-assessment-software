import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
with open("kullanıcı_değer.txt", "r",encoding="utf-8") as dosya:
    veriler_file = dosya.read()

veriler = veriler_file.split("\n")
Adj_C = str(veriler[4])
Ad_y_double_C = float(veriler[33])  # 2.0
Ad_g_double_C = float(veriler[34])  # 3.0
Ad_u_double_C = float(veriler[35])  # 4.0

Adj_g_double_C = float(veriler[36])  # 10.0
Adj_u_double_C = float(veriler[37])  # 11.0


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super(MplCanvas, self).__init__(self.fig)
        

    def plot_area_ad(self, l, w, h, hp):
        self.ax.clear()
        
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

        # Karmaşık grafik çizimi (karmasik_grafik)
        circle_radius = 3 * hp
        circle = plt.Circle((0, 0), circle_radius, color='g', fill=False, linestyle='--', label="Karmaşık Yapı Alanı")
        self.ax.add_patch(circle)

        self.ax.xaxis.set_major_locator(MultipleLocator(5))  # X ekseninde her 1 birim için etiket
        self.ax.yaxis.set_major_locator(MultipleLocator(5))  # Y ekseninde her 1 birim için etiket
        self.ax.xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))  # X eksenindeki etiket formatı
        self.ax.yaxis.set_major_formatter(FormatStrFormatter('%0.1f'))  # Y eksenindeki etiket formatı

        self.ax.legend(loc='upper right')
        self.ax.set_aspect('equal')
        self.draw()
        
        # Save the plot as a PNG file
        self.fig.savefig("complex_structure_ad.png")

    def plot_area_adj(self, l, w, h, hp):
        self.ax.clear()
        
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

        # Karmaşık grafik çizimi (karmasik_grafik)
        circle_radius = 3 * hp
        circle = plt.Circle((0, 0), circle_radius, color='g', fill=False, linestyle='--', label="Karmaşık Yapı Alanı")
        self.ax.add_patch(circle)

        self.ax.xaxis.set_major_locator(MultipleLocator(5))  # X ekseninde her 1 birim için etiket
        self.ax.yaxis.set_major_locator(MultipleLocator(5))  # Y ekseninde her 1 birim için etiket
        self.ax.xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))  # X eksenindeki etiket formatı
        self.ax.yaxis.set_major_formatter(FormatStrFormatter('%0.1f'))  # Y eksenindeki etiket formatı

        self.ax.legend(loc='upper right')
        self.ax.set_aspect('equal')
        self.draw()
        
        # Save the plot as a PNG file
        self.fig.savefig("complex_structure_ad.png")
    def plot_area_adj_yok(self):
        self.ax.clear()
        self.fig.savefig("complex_structure_adj.png")

x = MplCanvas()
l = Ad_u_double_C # Length
w = Ad_g_double_C  # Width
h = Ad_y_double_C  # Height (min value)
hp = 3 # Karmaşık yapı çıkıntı yüksekliği################ eklenecek
x.plot_area_ad(l, w, h, hp)
l_a = Adj_u_double_C # Length ayrık  
w_a = Adj_g_double_C  # Width ayrık  
h_a = 5  # Height (min value) ayrık########################
hp_a = 3 # Karmaşık yapı çıkıntı yüksekliği ayrık######################

if Adj_C == "True" :
    x.plot_area_adj_yok()
elif Adj_C == "False":
    x.plot_area_adj(l_a, w_a, h_a, hp_a)







