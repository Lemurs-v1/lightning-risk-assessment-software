import tkinter as tk
import os
import sys
import time
import subprocess

def restart_program():
    # Text box içeriğini geçici bir dosyaya kaydet
    with open("temp.txt", "w") as f:
        f.write(text_box.get("1.0", tk.END))
    
    # Programı kapatmadan önce bir süre gecikme ekleyin
    root.destroy()
    time.sleep(1)

    # Programı yeniden başlatın
    subprocess.Popen([sys.executable] + sys.argv)
    sys.exit()

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Yeniden Başlatma Örneği")

# Text box oluştur
text_box = tk.Text(root, height=10, width=40)
text_box.pack()

# Yeniden başlatma tuşu
restart_button = tk.Button(root, text="Yeniden Başlat", command=restart_program)
restart_button.pack()

# Uygulama yeniden başlatıldığında text box içeriğini geri yükle
try:
    with open("temp.txt", "r") as f:
        content = f.read()
        text_box.insert(tk.END, content)
except FileNotFoundError:
    pass  # Eğer temp.txt dosyası yoksa bir şey yapma

root.mainloop()
