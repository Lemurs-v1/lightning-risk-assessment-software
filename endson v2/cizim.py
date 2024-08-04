import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

class Calculation:
    def Ad_grafik(self, l, w, h):  
        alan = l * (w + 2) * 3 * h * (l + w) + np.pi * (3 * h) ** 2
        return alan

class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super(MplCanvas, self).__init__(self.fig)
        

    def plot_area(self, l, w, h, hp):
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
        self.fig.savefig("complex_structure.png")

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Çevreyi Kesik Çizgilerle Göster')

        self.show()

        self.plot()

    def plot(self):
        l = 10  # Length
        w = 5   # Width
        h = 2   # Height (min value)
        hp = 3 # Karmaşık yapı çıkıntı yüksekliği

        calculation = Calculation()
        area = calculation.Ad_grafik(l, w, h)

        self.canvas.plot_area(l, w, h, hp)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

