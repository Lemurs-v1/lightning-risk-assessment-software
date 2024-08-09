import tkinter as tk
import pandas as pd
from result import LightningRiskCalculator_result

# Tkinter penceresi oluşturma
root = tk.Tk()
root.title("Veri Görüntüleme")

# Global DataFrame tanımlama
df = pd.DataFrame()
x = LightningRiskCalculator_result()

# DataFrame'i güncelleyen fonksiyon
def refresh_data():
    global df
    try:
        x.R_tespit()  # Önce CSV dosyasını güncelleyin
        df = pd.read_csv('veriler.csv')  # Sonra CSV dosyasını okuyun
        update_ui()  # UI'yi güncelle
    except FileNotFoundError:
        label.config(text="Dosya bulunamadı.")
    except Exception as e:
        label.config(text=f"Hata: {str(e)}")

# UI güncelleme fonksiyonu
def update_ui():
    if df.empty:
        label.config(text="Veri yok.")
    else:
        label.config(text=df.to_string())

# Yenileme butonu oluşturma
refresh_button = tk.Button(root, text="Veriyi Yenile", command=refresh_data)
refresh_button.pack()

# Bir Label tanımlama
label = tk.Label(root, text="Veriyi görmek için butona basın.")
label.pack()

# İlk veri yükleme
refresh_data()

# Tkinter döngüsü
root.mainloop()
