from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QListView , QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Interface import Ui_MainWindow  # Arayüz tanımını içeren dosya
from PyQt5.QtGui import QIcon
import codecs
from PyQt5.QtWidgets import QMessageBox
import os
from tkinter import Tk, filedialog
from PIL import Image
import os
import tkinter as tk
import webbrowser
import re
import time
import traceback
from tkinter import messagebox
import subprocess


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.adjust_combobox_popup_width()
        self.delete_html_files_from_folder()

        # QComboBox'lar
        self.Ad_comboBox = self.ui.Ad_comboBox
        self.Ad_comboBox.currentIndexChanged.connect(self.selection_changed_Ad)

        self.Cd_comboBox = self.ui.Cd_comboBox
        self.Cd_comboBox.currentIndexChanged.connect(self.selection_changed_Cd)

        self.rt_comboBox = self.ui.rt_comboBox
        self.rt_comboBox.currentIndexChanged.connect(self.selection_changed_rt)

        self.Ce_comboBox = self.ui.Ce_comboBox
        self.Ce_comboBox.currentIndexChanged.connect(self.selection_changed_Ce)

        self.Adj_checkBox = self.ui.Adj_checkBox
        self.Adj_checkBox.stateChanged.connect(self.selection_changed_Adj)

        self.Cdj_comboBox = self.ui.Cdj_comboBox
        self.Cdj_comboBox.currentIndexChanged.connect(self.selection_changed_Cdj)

        self.Pb_comboBox = self.ui.Pb_comboBox
        self.Pb_comboBox.currentIndexChanged.connect(self.selection_changed_Pb)

        self.Pta_comboBox = self.ui.Pta_comboBox
        self.Pta_comboBox.currentIndexChanged.connect(self.selection_changed_Pta)

        self.Cld_comboBox = self.ui.Cld_comboBox
        self.Cld_comboBox.currentIndexChanged.connect(self.selection_changed_Cld)

        self.Pli_comboBox = self.ui.Pli_comboBox
        self.Pli_comboBox.currentIndexChanged.connect(self.selection_changed_Pli)

        self.Pld_comboBox = self.ui.Pld_comboBox
        self.Pld_comboBox.currentIndexChanged.connect(self.selection_changed_Pld)

        self.Pspd_comboBox = self.ui.Pspd_comboBox
        self.Pspd_comboBox.currentIndexChanged.connect(self.selection_changed_Pspd)

        self.Cl_comboBox = self.ui.Cl_comboBox
        self.Cl_comboBox.currentIndexChanged.connect(self.selection_changed_Cl)

        self.Peb_comboBox = self.ui.Peb_comboBox
        self.Peb_comboBox.currentIndexChanged.connect(self.selection_changed_Peb)

        self.CT_comboBox = self.ui.CT_comboBox
        self.CT_comboBox.currentIndexChanged.connect(self.selection_changed_CT)

        self.ca_bolu_ct_comboBox = self.ui.ca_bolu_ct_comboBox
        self.ca_bolu_ct_comboBox.currentIndexChanged.connect(self.selection_changed_ca_bolu_ct)

        self.rf_comboBox = self.ui.rf_comboBox
        self.rf_comboBox.currentIndexChanged.connect(self.selection_changed_rf)

        self.rp_comboBox = self.ui.rp_comboBox
        self.rp_comboBox.currentIndexChanged.connect(self.selection_changed_rp)

        self.Lf_comboBox = self.ui.Lf_comboBox
        self.Lf_comboBox.currentIndexChanged.connect(self.selection_changed_Lf)

        self.Lo_comboBox = self.ui.Lo_comboBox
        self.Lo_comboBox.currentIndexChanged.connect(self.selection_changed_Lo)

        self.Lfo2_comboBox = self.ui.Lfo2_comboBox
        self.Lfo2_comboBox.currentIndexChanged.connect(self.selection_changed_Lfo2)

        self.Lfo4_comboBox = self.ui.Lfo4_comboBox
        self.Lfo4_comboBox.currentIndexChanged.connect(self.selection_changed_Lfo4)

        self.KS3_comboBox = self.ui.KS3_comboBox
        self.KS3_comboBox.currentIndexChanged.connect(self.selection_changed_KS3)

        self.Pld_2_comboBox = self.ui.Pld_comboBox2
        self.Pld_2_comboBox.currentIndexChanged.connect(self.selection_changed_Pld_2)

        self.Pld_3_comboBox = self.ui.Pld_comboBox3
        self.Pld_3_comboBox.currentIndexChanged.connect(self.selection_changed_Pld_3)

        self.Pli_2_comboBox = self.ui.Pli_comboBox2
        self.Pli_2_comboBox.currentIndexChanged.connect(self.selection_changed_Pli_2)

        self.Hz_comboBox=self.ui.Hz_comboBox
        self.Hz_comboBox.currentIndexChanged.connect(self.selection_changed_Hz)

        self.Ptu_comboBox = self.ui.Ptu_comboBox
        self.Ptu_comboBox.currentIndexChanged.connect(self.selection_changed_Ptu)

        self.R1soru_comboBox=self.ui.R1soru_comboBox
        self.R1soru_comboBox.currentIndexChanged.connect(self.selection_changed_R1soru)

        self.R4soru_comboBox=self.ui.R4soru_comboBox
        self.R4soru_comboBox.currentIndexChanged.connect(self.selection_changed_R4soru)

        # Diğer bileşenler
        # Ekranlama Checkbox

        self.wm1_doubleSpinbox = self.ui.wm1_doubleSpinbox
        self.wm2_doubleSpinbox = self.ui.wm2_doubleSpinbox
        self.Uw_doubleSpinbox = self.ui.Uw_doubleSpinbox
        self.Ng_checkBox = self.ui.Ng_checkBox
        self.ekranlama_checkBox = self.ui.ekranlama_checkBox
        self.ekranlama_checkBox.stateChanged.connect(self.selection_changed_ekranlama)

        self.metal_checkBox = self.ui.metal_checkBox
        self.metal_checkBox.stateChanged.connect(self.selection_changed_metal)

        self.Ng_doubleSpinbox = self.ui.Ng_doubleSpinbox
        self.Ad_y_doubleSpinbox = self.ui.Ad_y_doubleSpinbox
        self.Ad_ymax_doubleSpinbox = self.ui.Ad_ymax_doubleSpinbox
        self.Ad_g_doubleSpinbox = self.ui.Ad_g_doubleSpinbox
        self.Ad_u_doubleSpinbox = self.ui.Ad_u_doubleSpinbox
        self.Adj_y_doubleSpinbox = self.ui.Adj_y_doubleSpinbox
        self.Adj_y_doubleSpinbox_2=self.ui.Adj_y_doubleSpinbox_2
        self.Adj_g_doubleSpinbox = self.ui.Adj_g_doubleSpinbox
        self.Adj_u_doubleSpinbox = self.ui.Adj_u_doubleSpinbox
        self.nt_doubleSpinbox = self.ui.nt_doubleSpinbox
        self.nz_checkBox = self.ui.nz_checkBox
        self.tz_checkBox=self.ui.tz_checkBox
        self.Ll_checkbox=self.ui.Ll_checkBox
        self.nz_doubleSpinbox = self.ui.nz_doubleSpinbox
        self.tz_doubleSpinbox = self.ui.tz_doubleSpinbox
        self.Ll_doubleSpinbox = self.ui.Ll_doubleSpinbox

        # TextEdit bileşeni
        self.textEdit = self.ui.textEdit
        self.lineEdit=self.ui.lineEdit
        self.lineEdit_2=self.ui.lineEdit_2
        self.lineEdit_3=self.ui.lineEdit_3
        self.lineEdit_4=self.ui.lineEdit_4

        # Kaydet ve Temizle butonları
        self.kaydet_pushButton = self.ui.kaydet_pushButton
        self.kaydet_pushButton.clicked.connect(self.save_values)

        self.temizle_pushButton = self.ui.temizle_pushButton
        self.temizle_pushButton.clicked.connect(self.clear_values)

        #html aç

        self.rapor_pushButton= self.ui.rapor_pushButton
        self.rapor_pushButton.clicked.connect(self.open_html_files)

        # Uygulama ikonu ayarla
        icon_path = "icon.png"
        self.setWindowIcon(QtGui.QIcon(icon_path))
        
        # Sistem tepsisi ikonu ayarla
        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(QtGui.QIcon(icon_path))
        self.tray_menu = QtWidgets.QMenu()
        self.quit_action = self.tray_menu.addAction("Çıkış")
        self.quit_action.triggered.connect(QtWidgets.qApp.quit)
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.show()
        #hesapla butonu
        self.hesapla_pushButton = self.ui.hesapla_pushButton
        self.hesapla_pushButton.clicked.connect(self.calculate)
        #logo yükle 
        self.logo_pushButton = self.ui.logo_pushButton
        self.logo_pushButton.clicked.connect(self.logo)
        #ÇİZİM BAS
        self.rapor_pushButton = self.ui.rapor_pushButton
        self.rapor_pushButton.clicked.connect(self.cizim)
        self.load_values()


    def selection_changed_Ad(self):
        selected_item = self.Ad_comboBox.currentText()
    
    def selection_changed_Cd(self):
        selected_item = self.Cd_comboBox.currentText()
    
    def selection_changed_rt(self):
        selected_item = self.rt_comboBox.currentText()
    
    def selection_changed_Ce(self):
        selected_item = self.Ce_comboBox.currentText()
    
    def selection_changed_Adj(self):
        state = self.Adj_checkBox.isChecked()
    
    def selection_changed_Cdj(self):
        selected_item = self.Cdj_comboBox.currentText()
    
    def selection_changed_Pb(self):
        selected_item = self.Pb_comboBox.currentText()
    
    def selection_changed_Pta(self):
        selected_item = self.Pta_comboBox.currentText()
    
    def selection_changed_Cld(self):
        selected_item = self.Cld_comboBox.currentText()
    
    def selection_changed_Pli(self):
        selected_item = self.Pli_comboBox.currentText()
    
    def selection_changed_Pld(self):
        selected_item = self.Pld_comboBox.currentText()
    
    def selection_changed_Pspd(self):
        selected_item = self.Pspd_comboBox.currentText()
    
    def selection_changed_Cl(self):
        selected_item = self.Cl_comboBox.currentText()
    
    def selection_changed_Peb(self):
        selected_item = self.Peb_comboBox.currentText()
    
    def selection_changed_CT(self):
        selected_item = self.CT_comboBox.currentText()
    
    def selection_changed_ca_bolu_ct(self):
        selected_item = self.ca_bolu_ct_comboBox.currentText()
    
    def selection_changed_rf(self):
        selected_item = self.rf_comboBox.currentText()
    
    def selection_changed_rp(self):
        selected_item = self.rp_comboBox.currentText()
    
    def selection_changed_Lf(self):
        selected_item = self.Lf_comboBox.currentText()
    
    def selection_changed_Lo(self):
        selected_item = self.Lo_comboBox.currentText()

    def selection_changed_Hz(self):
        selected_item = self.Hz_comboBox.currentText()
    
    def selection_changed_Lfo2(self):
        selected_item = self.Lfo2_comboBox.currentText()
    
    def selection_changed_Lfo4(self):
        selected_item = self.Lfo4_comboBox.currentText()
    
    def selection_changed_KS3(self):
        selected_item = self.KS3_comboBox.currentText()
    
    def selection_changed_Pld_2(self):
        selected_item = self.Pld_2_comboBox.currentText()
    
    def selection_changed_Pld_3(self):
        selected_item = self.Pld_3_comboBox.currentText()
    
    def selection_changed_Pli_2(self):
        selected_item = self.Pli_2_comboBox.currentText()
    def selection_changed_ekranlama(self):
        state = self.ekranlama_checkBox.isChecked()

    def selection_changed_metal(self):
        state = self.metal_checkBox.isChecked()

    def selection_changed_Ptu(self):
        selected_item = self.Ptu_comboBox.currentText()

    def selection_changed_tz_double_value(self):
        state = self.tz_checkBox.isChecked()

    def selection_changed_Ll_double_value(self):
        state = self.Ll_checkbox.isChecked()

    def selection_changed_R1soru(self):
        selected_item = self.R1soru_comboBox.currentText()

    def selection_changed_R4soru(self):
        selected_item = self.R4soru_comboBox.currentText()






    def open_html_files(self):
        # Çıktı dosyalarının kaydedileceği dizin
        html_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output_pdf_1')
        
        # HTML dosyalarını al
        html_files = [f for f in os.listdir(html_folder_path) if f.endswith('.html')]
        
        # Dosya isimlerindeki numaraları çıkarıp sıralama fonksiyonu
        def extract_number(file_name):
            match = re.search(r'(\d+)\.html$', file_name)
            return int(match.group(1)) if match else float('inf')
        
        # HTML dosyalarını numaralara göre sıralama
        html_files.sort(key=extract_number)
        
        for html_file in html_files:
            file_path = os.path.join(html_folder_path, html_file)
            webbrowser.open(f'file://{os.path.abspath(file_path)}')
            time.sleep(0.5)  # 0.5 saniye bekleme


    def load_values(self):
        try:
            with open("kullanıcı_değer.txt", "r", encoding='utf-8') as dosya_2:
                lines = dosya_2.readlines()
                # Her bileşene sırasıyla değerleri atayın
                if lines[0].strip() == 'evet':
                    self.Ad_comboBox.setCurrentText('Karmaşık biçimli')
                elif lines[0].strip() == 'hayır':
                    self.Ad_comboBox.setCurrentText('Düz biçimli')
                else:
                    self.Ad_comboBox.setCurrentText('Seçiniz')

                self.Cd_comboBox.setCurrentText(lines[1].strip())
                self.rt_comboBox.setCurrentText(lines[2].strip())
                self.Ce_comboBox.setCurrentText(lines[3].strip())
                self.Adj_checkBox.setChecked(lines[4].strip() == 'True')
                self.Cdj_comboBox.setCurrentText(lines[5].strip())
                self.Pb_comboBox.setCurrentText(lines[6].strip())
                self.Pta_comboBox.setCurrentText(lines[7].strip())
                self.Cld_comboBox.setCurrentText(lines[8].strip())
                self.Pli_comboBox.setCurrentText(lines[9].strip())
                self.Pld_comboBox.setCurrentText(lines[10].strip())
                self.Pspd_comboBox.setCurrentText(lines[11].strip())
                self.Cl_comboBox.setCurrentText(lines[12].strip())
                self.Peb_comboBox.setCurrentText(lines[13].strip())
                self.CT_comboBox.setCurrentText(lines[14].strip())
                self.ca_bolu_ct_comboBox.setCurrentText(lines[15].strip())
                self.rf_comboBox.setCurrentText(lines[16].strip())
                self.rp_comboBox.setCurrentText(lines[17].strip())
                self.Lf_comboBox.setCurrentText(lines[18].strip())
                self.Lo_comboBox.setCurrentText(lines[19].strip())
                self.Lfo2_comboBox.setCurrentText(lines[20].strip())
                self.Lfo4_comboBox.setCurrentText(lines[21].strip())
                self.KS3_comboBox.setCurrentText(lines[22].strip())
                self.Pld_2_comboBox.setCurrentText(lines[23].strip())
                self.Pld_3_comboBox.setCurrentText(lines[24].strip())
                self.Pli_2_comboBox.setCurrentText(lines[25].strip())
                self.Ng_checkBox.setChecked(lines[26].strip() == 'True')
                self.wm1_doubleSpinbox.setValue(float(lines[27].strip()))
                self.wm2_doubleSpinbox.setValue(float(lines[28].strip()))
                self.Uw_doubleSpinbox.setValue(float(lines[29].strip()))
                self.ekranlama_checkBox.setChecked(lines[30].strip() == 'True')
                self.metal_checkBox.setChecked(lines[31].strip() == 'True')
                self.Ng_doubleSpinbox.setValue(float(lines[32].strip()))
                self.Ad_y_doubleSpinbox.setValue(float(lines[33].strip()))
                self.Ad_g_doubleSpinbox.setValue(float(lines[34].strip()))
                self.Ad_u_doubleSpinbox.setValue(float(lines[35].strip()))
                self.Adj_g_doubleSpinbox.setValue(float(lines[36].strip()))
                self.Adj_u_doubleSpinbox.setValue(float(lines[37].strip()))
                self.nt_doubleSpinbox.setValue(float(lines[38].strip()))
                self.nz_checkBox.setChecked(lines[39].strip() == 'True')
                self.nz_doubleSpinbox.setValue(float(lines[40].strip()))
                self.tz_doubleSpinbox.setValue(float(lines[41].strip()))
                self.Ll_doubleSpinbox.setValue(float(lines[42].strip()))
                self.Hz_comboBox.setCurrentText(lines[43].strip())
                self.Ptu_comboBox.setCurrentText(lines[44].strip())
                self.tz_checkBox.setChecked(lines[45].strip() == 'True')
                self.Ll_checkbox.setChecked(lines[46].strip() == 'True')
                self.textEdit.setPlainText(lines[47].strip())
                self.Ad_ymax_doubleSpinbox.setValue(float(lines[48].strip()))
                self.Adj_y_doubleSpinbox.setValue(float(lines[49].strip()))
                self.Adj_y_doubleSpinbox_2.setValue(float(lines[50].strip()))
                self.lineEdit.setText(lines[51].strip())
                self.lineEdit_2.setText(lines[52].strip())
                self.lineEdit_4.setText(lines[53].strip())
                self.lineEdit_3.setText(lines[54].strip())
                self.R1soru_comboBox.setCurrentText(lines[55].strip())
                self.R4soru_comboBox.setCurrentText(lines[56].strip())
        except FileNotFoundError:
            # Eğer dosya yoksa (ilk kez açılıyorsa), hiçbir şey yapma
            pass

    def delete_html_files_from_folder(self):
        folder_path = "_internal\\output_pdf_1"
        images_folder_path = os.path.join(folder_path, "images")
        specific_png_files = [
            "graph_1.png", "graph_2.png", "graph_3.png", 
            "graph_4.png", 
            "complex_structure_adj.png", "complex_structure_ad.png"
        ]

        
        # output_pdf_1 klasöründeki .html dosyalarını sil
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".html"):
                file_path = os.path.join(folder_path, file_name)
                os.remove(file_path)
        
        # images klasöründeki belirli .png dosyalarını sil
        for file_name in os.listdir(images_folder_path):
            if file_name in specific_png_files:
                file_path = os.path.join(images_folder_path, file_name)
                os.remove(file_path)
        
        # Kodun bulunduğu dizindeki belirli .txt dosyalarını sil






 
    def save_values(self):


        Ad_value = self.Ad_comboBox.currentText()
        if Ad_value == 'Karmaşık biçimli':
            Ad_value='evet'
        elif Ad_value == 'Düz biçimli':
            Ad_value = 'hayır'
        Cd_value = self.Cd_comboBox.currentText()
        rt_value = self.rt_comboBox.currentText()
        Ce_value = self.Ce_comboBox.currentText()
        Adj_value = self.Adj_checkBox.isChecked()
        Cdj_value = self.Cdj_comboBox.currentText()
        Pb_value = self.Pb_comboBox.currentText()
        Pta_value = self.Pta_comboBox.currentText()
        Cld_value = self.Cld_comboBox.currentText()
        Pli_value = self.Pli_comboBox.currentText()
        Pld_value = self.Pld_comboBox.currentText()
        Pspd_value = self.Pspd_comboBox.currentText()
        Hz_value = self.Hz_comboBox.currentText()
        Ptu_value=self.Ptu_comboBox.currentText()
        Cl_value = self.Cl_comboBox.currentText()
        Peb_value = self.Peb_comboBox.currentText()
        CT_value = self.CT_comboBox.currentText()
        ca_bolu_ct_value = self.ca_bolu_ct_comboBox.currentText()
        rf_value = self.rf_comboBox.currentText()
        rp_value = self.rp_comboBox.currentText()
        Lf_value = self.Lf_comboBox.currentText()
        Lo_value = self.Lo_comboBox.currentText()
        Lfo2_value = self.Lfo2_comboBox.currentText()
        Lfo4_value = self.Lfo4_comboBox.currentText()
        KS3_value = self.KS3_comboBox.currentText()
        Pld_2_value = self.Pld_2_comboBox.currentText()
        Pld_3_value = self.Pld_3_comboBox.currentText()
        Pli_2_value = self.Pli_2_comboBox.currentText()
        Ng_value = self.Ng_checkBox.isChecked()
        ekranlama_value = self.ekranlama_checkBox.isChecked()
        metal_value = self.metal_checkBox.isChecked()
        wm1_value = self.wm1_doubleSpinbox.value()
        wm2_value = self.wm2_doubleSpinbox.value()
        Uw_value = self.Uw_doubleSpinbox.value()
        Ng_double_value = self.Ng_doubleSpinbox.value()
        Ad_y_double_value = self.Ad_y_doubleSpinbox.value()
        Ad_ymax_double_value = self.Ad_ymax_doubleSpinbox.value()
        Ad_g_double_value = self.Ad_g_doubleSpinbox.value()
        Ad_u_double_value = self.Ad_u_doubleSpinbox.value()
        Adj_y_double_value = self.Adj_y_doubleSpinbox.value()
        Adj_y_double_value_2=self.Adj_y_doubleSpinbox_2.value()
        Adj_g_double_value = self.Adj_g_doubleSpinbox.value()
        Adj_u_double_value = self.Adj_u_doubleSpinbox.value()
        nt_value = self.nt_doubleSpinbox.value()
        nz_value = self.nz_checkBox.isChecked()
        tz_value = self.tz_checkBox.isChecked()
        Ll_value = self.Ll_checkbox.isChecked()
        nz_double_value = self.nz_doubleSpinbox.value()
        tz_double_value = self.tz_doubleSpinbox.value()
        Ll_double_value = self.Ll_doubleSpinbox.value()
        description = self.textEdit.toPlainText()
        Rapor_yazarı = self.lineEdit.text()
        Müsteri = self.lineEdit_2.text()
        Obje = self.lineEdit_4.text()
        Proje_no = self.lineEdit_3.text()
        R1_value=self.R1soru_comboBox.currentText()
        R4_value=self.R4soru_comboBox.currentText()


    # Verileri ilgili formatta yazdır
        değerler = (
            f"{Ad_value}\n"
            f"{Cd_value}\n"
            f"{rt_value}\n"
            f"{Ce_value}\n"
            f"{Adj_value}\n"
            f"{Cdj_value}\n"
            f"{Pb_value}\n"
            f"{Pta_value}\n"
            f"{Cld_value}\n"
            f"{Pli_value}\n"
            f"{Pld_value}\n"
            f"{Pspd_value}\n"
            f"{Cl_value}\n"
            f"{Peb_value}\n"
            f"{CT_value}\n"
            f"{ca_bolu_ct_value}\n"
            f"{rf_value}\n"
            f"{rp_value}\n"
            f"{Lf_value}\n"
            f"{Lo_value}\n"
            f"{Lfo2_value}\n"
            f"{Lfo4_value}\n"
            f"{KS3_value}\n"
            f"{Pld_2_value}\n"
            f"{Pld_3_value}\n"
            f"{Pli_2_value}\n"
            f"{Ng_value}\n"
            f"{wm1_value}\n"
            f"{wm2_value}\n"
            f"{Uw_value}\n"
            f"{ekranlama_value}\n"
            f"{metal_value}\n"
            f"{Ng_double_value}\n"
            f"{Ad_y_double_value}\n"
            f"{Ad_g_double_value}\n"
            f"{Ad_u_double_value}\n"
            f"{Adj_g_double_value}\n"
            f"{Adj_u_double_value}\n"
            f"{nt_value}\n"
            f"{nz_value}\n"
            f"{nz_double_value}\n"
            f"{tz_double_value}\n"
            f"{Ll_double_value}\n"
            f"{Hz_value}\n"
            f"{Ptu_value}\n"
            f"{tz_value}\n"   
            f"{Ll_value}\n"
            f"{description}\n"
            f"{Ad_ymax_double_value}\n"
            f"{Adj_y_double_value}\n"
            f"{Adj_y_double_value_2}\n"
            f"{Rapor_yazarı}\n"
            f"{Müsteri}\n"
            f"{Obje}\n"
            f"{Proje_no}\n"
            f"{R1_value}\n"
            f"{R4_value}\n"
                )

    
        with open("kullanıcı_değer.txt", "w",encoding='utf-8') as dosya_2:
            dosya_2.write(değerler)
        QMessageBox.information(self, "İNFO", "Değerler başarıyla kaydedildi")
        subprocess.Popen([sys.executable] + sys.argv)
        sys.exit()
        
        # print(f'Seçilen Ad değeri: {Ad_value}')
        # print(f'Seçilen Cd değeri: {Cd_value}')
        # print(f'Seçilen rt değeri: {rt_value}')
        # print(f'Seçilen Ce değeri: {Ce_value}')
        # print(f'Adj CheckBox durumu: {Adj_value}')
        # print(f'Seçilen Cdj değeri: {Cdj_value}')
        # print(f'Seçilen Pb değeri: {Pb_value}')
        # print(f'Seçilen Pta değeri: {Pta_value}')
        # print(f'Seçilen Cld değeri: {Cld_value}')
        # print(f'Seçilen Pli değeri: {Pli_value}')
        # print(f'Seçilen Pld değeri: {Pld_value}')
        # print(f'Seçilen Pspd değeri: {Pspd_value}')
        # print(f'Seçilen Cl değeri: {Cl_value}')
        # print(f'Seçilen Peb değeri: {Peb_value}')
        # print(f'Seçilen CT değeri: {CT_value}')
        # print(f'Seçilen ca_bolu_ct değeri: {ca_bolu_ct_value}')
        # print(f'Seçilen rf değeri: {rf_value}')
        # print(f'Seçilen rp değeri: {rp_value}')
        # print(f'Seçilen Lf değeri: {Lf_value}')
        # print(f'Seçilen Lo değeri: {Lo_value}')
        # print(f'Seçilen Lfo2 değeri: {Lfo2_value}')
        # print(f'Seçilen Lfo4 değeri: {Lfo4_value}')
        # print(f'Seçilen KS3 değeri: {KS3_value}')
        # print(f'Seçilen Pld2 değeri: {Pld_2_value}')
        # print(f'Seçilen Pld3 değeri: {Pld_3_value}')
        # print(f'Seçilen Pli2 değeri: {Pli_2_value}')
        # print(f'Ng CheckBox durumu: {Ng_value}')
        # print(f'wm1 değeri: {wm1_value}')
        # print(f'wm2 değeri: {wm2_value}')
        # print(f'Uw değeri: {Uw_value}')
        # print(f'Ekranlama CheckBox durumu: {ekranlama_value}')
        # print(f'Metal CheckBox durumu: {metal_value}')
        # print(f'Ng Double Spinbox değeri: {Ng_double_value}')
        # print(f'Ad_y Double Spinbox değeri: {Ad_y_double_value}')
        # print(f'Ad_g Double Spinbox değeri: {Ad_g_double_value}')
        # print(f'Ad_u Double Spinbox değeri: {Ad_u_double_value}')
        # print(f'Adj_g Double Spinbox değeri: {Adj_g_double_value}')
        # print(f'Adj_u Double Spinbox değeri: {Adj_u_double_value}')
        # print(f'nt Double Spinbox değeri: {nt_value}')
        # print(f'nz CheckBox durumu: {nz_value}')
        # print(f'nz Double Spinbox değeri: {nz_double_value}')
        # print(f'tz Double Spinbox değeri: {tz_double_value}')
        # print(f'LI Double Spinbox değeri: {Ll_double_value}')
        # print(f'Seçilen Hz değeri: {Hz_value}')
        # print(f'Seçilen Ptu değeri: {Ptu_value}')
        # print(f'Seçilen tz CheckBox değeri: {tz_value}')
        # print(f'Seçilen Ll CheckBox değeri: {Ll_value}')
        # print(f'description: {description}')
        # print(f'Seçilen Ad_ymax: {Ad_ymax_double_value}')
        # print(f'Seçilen Adj_y: {Adj_y_double_value}')
        # print(f'Seçilen Adj_y_max: {Adj_y_double_value_2}')
        # print(f'Rapor yazarı: {Rapor_yazarı}')
        # print(f'Müsteri: {Müsteri}')
        # print(f'Obje: {Obje}')
        # print(f'R1_value: {R1_value}')
        # print(f'R4_value: {R4_value}')
        
    def calculate(self):

        try:
            from result import LightningRiskCalculator_result
            l = LightningRiskCalculator_result()
            veriler =l.R_tespit()
        
            def format_number_scientific(number):
                return f"{number:.1e}"  # Bilimsel gösterim, 2 ondalık basamak
            

            r1 = format_number_scientific(float(veriler[0]))
            r2 = format_number_scientific(float(veriler[1]))
            r3 = format_number_scientific(float(veriler[2]))
            r4 = format_number_scientific(float(veriler[3]))
            sonuç = f"R1={r1}\nR2={r2}\nR3={r3}\nR4={r4}"

            QMessageBox.information(self, "Sonuç", sonuç)

            # Ad_value = self.Ad_comboBox.currentText()
            # Cd_value = self.Cd_comboBox.currentText()
            # rt_value = self.rt_comboBox.currentText()
            # Ce_value = self.Ce_comboBox.currentText()
            # Adj_value = self.Adj_checkBox.isChecked()
            # Cdj_value = self.Cdj_comboBox.currentText()
            # Pb_value = self.Pb_comboBox.currentText()
            # Pta_value = self.Pta_comboBox.currentText()
            # Cld_value = self.Cld_comboBox.currentText()
            # Pli_value = self.Pli_comboBox.currentText()
            # Pld_value = self.Pld_comboBox.currentText()
            # Pspd_value = self.Pspd_comboBox.currentText()
            # Hz_value = self.Hz_comboBox.currentText()
            # Ptu_value=self.Ptu_comboBox.currentText()
            # Cl_value = self.Cl_comboBox.currentText()
            # Peb_value = self.Peb_comboBox.currentText()
            # CT_value = self.CT_comboBox.currentText()
            # ca_bolu_ct_value = self.ca_bolu_ct_comboBox.currentText()
            # rf_value = self.rf_comboBox.currentText()
            # rp_value = self.rp_comboBox.currentText()
            # Lf_value = self.Lf_comboBox.currentText()
            # Lo_value = self.Lo_comboBox.currentText()
            # Lfo2_value = self.Lfo2_comboBox.currentText()
            # Lfo4_value = self.Lfo4_comboBox.currentText()
            # KS3_value = self.KS3_comboBox.currentText()
            # Pld_2_value = self.Pld_2_comboBox.currentText()
            # Pld_3_value = self.Pld_3_comboBox.currentText()
            # Pli_2_value = self.Pli_2_comboBox.currentText()
            # Ng_value = self.Ng_checkBox.isChecked()
            # ekranlama_value = self.ekranlama_checkBox.isChecked()
            # metal_value = self.metal_checkBox.isChecked()
            # wm1_value = self.wm1_doubleSpinbox.value()
            # wm2_value = self.wm2_doubleSpinbox.value()
            # Uw_value = self.Uw_doubleSpinbox.value()
            # Ng_double_value = self.Ng_doubleSpinbox.value()
            # Ad_y_double_value = self.Ad_y_doubleSpinbox.value()
            # Ad_ymax_double_value = self.Ad_ymax_doubleSpinbox.value()
            # Ad_g_double_value = self.Ad_g_doubleSpinbox.value()
            # Ad_u_double_value = self.Ad_u_doubleSpinbox.value()
            # Adj_y_double_value = self.Adj_y_doubleSpinbox.value()
            # Adj_y_double_value_max=self.Adj_y_doubleSpinbox_2.value()#####max mı
            # Adj_g_double_value = self.Adj_g_doubleSpinbox.value()
            # Adj_u_double_value = self.Adj_u_doubleSpinbox.value()
            # nt_value = self.nt_doubleSpinbox.value()
            # nz_value = self.nz_checkBox.isChecked()
            # tz_value = self.nz_checkBox.isChecked()
            # Ll_value = self.nz_checkBox.isChecked()
            # nz_double_value = self.nz_doubleSpinbox.value()
            # tz_double_value = self.tz_doubleSpinbox.value()
            # Ll_double_value = self.Ll_doubleSpinbox.value()
            # description = self.textEdit.toPlainText()
            # Rapor_yazarı = self.lineEdit.text()
            # Müsteri = self.lineEdit_2.text()
            # Obje = self.lineEdit_4.text()
            # Proje_no = self.lineEdit_3.text()
            # R1_value=self.R1soru_comboBox.currentText()
            # R4_value=self.R4soru_comboBox.currentText()
            # with open("saved_values.txt", "w", encoding="utf-8") as file:
            #     file.write(f"{Ad_value}\n")
            #     file.write(f"{Cd_value}\n")
            #     file.write(f"{rt_value}\n")
            #     file.write(f"{Ce_value}\n")
            #     file.write(f"{Adj_value}\n")
            #     file.write(f"{Cdj_value}\n")
            #     file.write(f"{Pb_value}\n")
            #     file.write(f"{Pta_value}\n")
            #     file.write(f"{Cld_value}\n")
            #     file.write(f"{Pli_value}\n")
            #     file.write(f"{Pld_value}\n")
            #     file.write(f"{Pspd_value}\n")
            #     file.write(f"{Cl_value}\n")
            #     file.write(f"{Peb_value}\n")
            #     file.write(f"{CT_value}\n")
            #     file.write(f"{ca_bolu_ct_value}\n")
            #     file.write(f"{rf_value}\n")
            #     file.write(f"{rp_value}\n")
            #     file.write(f"{Lf_value}\n")
            #     file.write(f"{Lo_value}\n")
            #     file.write(f"{Lfo2_value}\n")
            #     file.write(f"{Lfo4_value}\n")
            #     file.write(f"{KS3_value}\n")
            #     file.write(f"{Pld_2_value}\n")
            #     file.write(f"{Pld_3_value}\n")
            #     file.write(f"{Pli_2_value}\n")
            #     file.write(f"{Ng_value}\n")
            #     file.write(f"{wm1_value}\n")
            #     file.write(f"{wm2_value}\n")
            #     file.write(f"{Uw_value}\n")
            #     file.write(f"{ekranlama_value}\n")
            #     file.write(f"{metal_value}\n")
            #     file.write(f"{Ng_double_value}\n")
            #     file.write(f"{Ad_y_double_value}\n")
            #     file.write(f"{Ad_g_double_value }\n")
            #     file.write(f"{Ad_u_double_value}\n")
            #     file.write(f"{ Ad_ymax_double_value}\n")
            #     file.write(f"{Adj_g_double_value}\n")
            #     file.write(f"{Adj_u_double_value}\n")
            #     file.write(f"{Adj_y_double_value}\n")
            #     file.write(f"{Adj_y_double_value_max}\n")
            #     file.write(f"{nt_value}\n")
            #     file.write(f"{nz_value}\n")
            #     file.write(f"{nz_double_value}\n")
            #     file.write(f"{tz_value}\n")
            #     file.write(f"{Ll_value}\n")
            #     file.write(f"{Hz_value }\n")
            #     file.write(f"{Ptu_value}\n")
            #     file.write(f"{tz_double_value}\n")######sorun
            #     file.write(f"{Ll_double_value}\n")
            #     file.write(f"{description}\n")
            #     file.write(f"{Rapor_yazarı}\n")
            #     file.write(f"{Müsteri }\n")
            #     file.write(f"{ Obje}\n")
            #     file.write(f"{Proje_no }\n")
            #     file.write(f"{R1_value}\n")
            #     file.write(f"{R4_value}\n")


        except (IndexError, ValueError, TypeError, KeyError, ZeroDivisionError) as e:

            tb_str = traceback.format_exc()
            # self. ile başlayan kısmı ayıklamak için regex kullan
            değerler = f"{0}#{0}#{0}#{0}"
            QMessageBox.information(self, "Sonuç", değerler)
            match = re.search(r'self\.(\w+)', tb_str)
            
            if match:
                # self. ifadesinden sonra gelen kelimeyi yazdır

                messagebox.showerror("ERROR",f"{match.group(1)} DEĞERİ EKSİK VEYA YANLIŞ")
                
            else:
                messagebox.showerror("ERROR","VERİLERİNİZDE HATA VAR FAKAT TESPİT EDİLEMİYOR DEĞERLERİNİZİN DOĞRULUĞUNDA EMİN OLUN")



        

    def logo(self):
        # Tkinter kök penceresini oluştur (bu pencere görünmeyecek)
        root = Tk()
        root.withdraw()  # Ana pencereyi gizle

        # Kullanıcıdan dosya seçmesini sağla
        file_path = filedialog.askopenfilename(
            title="Resim Seç",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
        )

        if file_path:
            # Kaydedilecek klasör ve dosya yolunu oluştur
            output_directory = "_internal\\output_pdf_1\\images"
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)  # Klasörü oluştur

            # Resmi okuma ve kaydetme
            image = Image.open(file_path)
            save_path = os.path.join(output_directory, "customer.png")
            image.save(save_path)

            messagebox.showinfo("Resim Yükleme Durumu",f"Resim başarıyla kaydedildi: {save_path}")
        else:
            messagebox.showerror("ERROR","Hiçbir resim seçilmedi.")


    def cizim(self):
        try:
            from pdf_app_1 import LightningRiskWriter
            from cizim import MplCanvas
            ciz = MplCanvas()
            pdf = LightningRiskWriter()
            ciz.çizdir()
            pdf.rapor_yaz()
            
            
            
        except (IndexError, ValueError, TypeError, KeyError, ZeroDivisionError) as e:
            tb_str = traceback.format_exc()

            # self. ile başlayan kısmı ayıklamak için regex kullan

            match = re.search(r'self\.(\w+)', tb_str)
            
            if match:
                # self. ifadesinden sonra gelen kelimeyi yazdır
                messagebox.showerror("ERROR", f"{match.group(1)} DEĞERİ EKSİK VEYA YANLIŞ")
            else:
                messagebox.showerror("ERROR", "VERİLERİNİZDE HATA VAR FAKAT TESPİT EDİLEMİYOR DEĞERLERİNİZİN DOĞRULUĞUNDA EMİN OLUN")
            
            raise e  # Hata tekrar fırlatılır
        else:
            # Eğer try bloğunda hata yoksa burası çalışır


            self.open_html_files()


        

    def clear_values(self):
        self.Ad_comboBox.setCurrentIndex(0)
        self.Cd_comboBox.setCurrentIndex(0)
        self.rt_comboBox.setCurrentIndex(0)
        self.Ce_comboBox.setCurrentIndex(0)
        self.Adj_checkBox.setChecked(False)
        self.Cdj_comboBox.setCurrentIndex(0)
        self.Pb_comboBox.setCurrentIndex(0)
        self.Pta_comboBox.setCurrentIndex(0)
        self.Cld_comboBox.setCurrentIndex(0)
        self.Pli_comboBox.setCurrentIndex(0)
        self.Pld_comboBox.setCurrentIndex(0)
        self.Pspd_comboBox.setCurrentIndex(0)
        self.Cl_comboBox.setCurrentIndex(0)
        self.Peb_comboBox.setCurrentIndex(0)
        self.CT_comboBox.setCurrentIndex(0)
        self.ca_bolu_ct_comboBox.setCurrentIndex(0)
        self.rf_comboBox.setCurrentIndex(0)
        self.rp_comboBox.setCurrentIndex(0)
        self.Lf_comboBox.setCurrentIndex(0)
        self.Lo_comboBox.setCurrentIndex(0)
        self.Lfo2_comboBox.setCurrentIndex(0)
        self.Lfo4_comboBox.setCurrentIndex(0)
        self.KS3_comboBox.setCurrentIndex(0)
        self.Pld_2_comboBox.setCurrentIndex(0)
        self.Pld_3_comboBox.setCurrentIndex(0)
        self.Pli_2_comboBox.setCurrentIndex(0)
        self.Hz_comboBox.setCurrentIndex(0)

        self.Ng_checkBox.setChecked(False)
        self.wm1_doubleSpinbox.setValue(0.0)
        self.wm2_doubleSpinbox.setValue(0.0)
        self.Uw_doubleSpinbox.setValue(0.0)
        self.Ng_doubleSpinbox.setValue(0.0)
        self.Ad_y_doubleSpinbox.setValue(0.0)
        self.Ad_g_doubleSpinbox.setValue(0.0)
        self.Ad_u_doubleSpinbox.setValue(0.0)
        self.Adj_checkBox.setChecked(False)
        self.Adj_g_doubleSpinbox.setValue(0.0)
        self.Adj_u_doubleSpinbox.setValue(0.0)
        self.nt_doubleSpinbox.setValue(0.0)
        self.nz_checkBox.setChecked(False)
        self.nz_doubleSpinbox.setValue(0.0)
        self.tz_doubleSpinbox.setValue(0.0)
        self.Ll_doubleSpinbox.setValue(0.0)
        self.ekranlama_checkBox.setChecked(False)
        self.metal_checkBox.setChecked(False)              
        self.R1soru_comboBox.setCurrentIndex(0)
        self.R4soru_comboBox.setCurrentIndex(0)
        self.Ptu_comboBox.setCurrentIndex(0)
        self.Adj_y_doubleSpinbox_2.setValue(0.0)
        self.Adj_y_doubleSpinbox.setValue(0.0)
        self.Ad_ymax_doubleSpinbox.setValue(0.0)
        self.tz_checkBox.setChecked(False)
        self.Ll_checkbox.setChecked(False)
        self.textEdit.clear()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_4.clear()
        self.lineEdit_3.clear()


    def adjust_combobox_popup_width(self):
        comboboxes = self.findChildren(QComboBox)
        for combobox in comboboxes:
            view = QListView()
            view.setMinimumWidth(self.get_max_item_width(combobox))
            combobox.setView(view)

    def get_max_item_width(self, combobox):
        max_width = combobox.minimumSizeHint().width()
        for i in range(combobox.count()):
            item_text = combobox.itemText(i)
            item_width = combobox.fontMetrics().boundingRect(item_text).width()
            if item_width > max_width:
                max_width = item_width
        return max_width + 100

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.png'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())