import matplotlib.pyplot as plt

class Grafik:
    def grafik(self, categories, values, constant_value=1e-5):
        # Grafiği oluşturma
        fig, ax = plt.subplots()

        # Düz çizgiyi çizme
        ax.plot(categories, [constant_value] * len(categories), color='blue', label='Constant Value')

        # Diğer değerleri çizme
        ax.plot(categories, values, color='red', label='Values')

        # Başlık ve etiketler
        ax.set_title('Total')
        ax.set_xlabel('Categories')
        ax.set_ylabel('Values')
        ax.legend()

        # PNG olarak kaydetme
        plt.savefig('graph.png')

        # Gösterme
        plt.show()

# Kullanım örneği
categories = ['RA', 'RB',"RC"]
values = [1e-5, 8e-6, 6e-2]
grafik_obj = Grafik()
grafik_obj.grafik(categories, values)