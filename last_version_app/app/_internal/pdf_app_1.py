import os
from datetime import datetime
from output_value import LightningRiskCalculator_output_value
from min_values import LightningRiskCalculator_min_values 
from middle_value import LightningRiskCalculator_middle_values
from result import LightningRiskCalculator_result
out=LightningRiskCalculator_output_value()
min = LightningRiskCalculator_min_values()
mid = LightningRiskCalculator_middle_values()
result = LightningRiskCalculator_result()
class LightningRiskWriter():
        
    def rapor_yaz(self):
        with open("kullanıcı_değer.txt", "r",encoding = "utf-8") as dosya:
            veriler_file = dosya.read()

        veriler = veriler_file.split("\n")
        def format_number_scientific(number):
                return f"{number:.1e}"  # Bilimsel gösterim, 2 ondalık basamak



        # Kullanıcıdan isim al
        tarih = datetime.now().strftime('%Y-%m-%d')
        açıklama = str(veriler[47])
        müşteri = str(veriler[52])
        yazar = str(veriler[51])
        proje_no = str(veriler[54])
        uzunluk_yapı = float(veriler[35]) 
        genişlik_yapı = float(veriler[34]) 
        yükseklik_yapı =  float(veriler[33])
        yükseklik_yapı_max = float(veriler[48])
        
        yapı_konum = str(veriler[53])
        yapı_AD_alan = min.a_d_belirle()
        ayrık_yapı_AD_alan = min.a_dj_belirle()########### emin misiniz
        c_dj = min.c_dj_belirle()

        CI_C=min.c_ı_belirle()
        n_d=mid.n_d_belirle()
        n_g=out.n_g_bul()
        Plı_c=str(veriler[9])
        CE_C=str(veriler[3])
        CLD_c=str(veriler[8]) 
        CT_C=str(veriler[14])
        Pld_C=str(veriler[23])
        Ll_C=str(veriler[46])
        Al_c=min.a_l_belirle()
        uw_c=float(veriler[29])
        uzunluk_ayrık_yapı=float(veriler[37])
        genislik_ayrık_yapı=float(veriler[36])
        yükseklik_ayrık_yapı=float(veriler[49])
        yükseklik_ayrık_yapı_max=float(veriler[50])
        ayrik_yapi_AD_alan=min.a_dj_belirle()
        patlama_riski=str(veriler[55])
        rp_c=str(veriler[17])  
        hz_c=str(veriler[43])
        R_1=format_number_scientific(result.R_1_belirle())
        R_2=format_number_scientific(result.R_2_belirle())
        R_3=format_number_scientific(result.R_3_belirle())
        R_4=format_number_scientific(result.R_4_belirle())

        P_B=str(veriler[6])
        P_EB=str(veriler[13])
        KS1=str(veriler[31])
        KS3=str(veriler[22])
        Ptu_c=str(veriler[44])
        Pta_c=str(veriler[7]) 
        Ng_C =str(veriler[26]) 
        if Ng_C == "True":
            t_d = n_g
        elif Ng_C =="False":
            t_d=n_g*10


        html_content_1 = f"""
        <!DOCTYPE html> <!-- HTML5 belge türü tanımı -->
        <html lang="tr"> <!-- Belge dilini Türkçe olarak belirtir -->
        <head>
            <meta charset="UTF-8"> <!-- Belgenin karakter kodlamasını UTF-8 olarak ayarlar -->
            <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Sayfa boyutunu ve ölçeğini ayarlar, mobil uyumluluğu sağlar -->
            <title>Lightning Protection Risk Management</title> <!-- Sayfanın başlık etiketini belirtir -->
            <style>
                body {{
                    font-family: Arial, sans-serif; /* Sayfadaki yazı tipini Arial olarak ayarlar, Arial mevcut değilse sans-serif kullanılır */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    min-height: 100vh; /* Sayfanın en az yüksekliğini ekran yüksekliği kadar yapar */
                    margin: 0; /* Varsayılan margin değerlerini sıfırlar */
                }}
                .container {{
                    width: 80%; /* Container genişliğini sayfanın %80'i olarak ayarlar */
                    margin: 0 auto; /* Container'ı yatayda ortalar */
                    padding: 20px; /* Container'ın içindeki boşluğu 20px yapar */
                    flex: 1; /* Container'ın esnekliğini sağlar, diğer flex öğeleriyle uyumlu olmasını sağlar */
                }}
                .header {{
                    text-align: center; /* Header içindeki metni ortalar */
                    margin-bottom: 100px; /* Header'ın altına 100px boşluk ekler */
                }}
                .header img {{
                    max-width: 100px; /* Header içindeki resmin maksimum genişliğini 100px olarak ayarlar */
                }}
                .content {{
                    margin-bottom: 100px; /* Content bölümünün altına 100px boşluk ekler */
                }}
                .content p {{
                    margin: 30px 0; /* Content içindeki paragrafların üst ve alt marginlerini 30px yapar */
                }}
                .footer {{
                    display: flex; /* Footer öğelerini yatayda hizalar */
                    justify-content: space-between; /* Footer öğeleri arasında boşluk bırakır */
                    align-items: center; /* Footer öğelerini dikeyde ortalar */
                    margin-top: 10px; /* Footer'ın üstüne 10px boşluk ekler */
                    padding: 10px 20px; /* İç boşlukları belirler */
                    background-color: #f1f1f1; /* Footer'ın arka plan rengini belirler */
                }}
                .footer img {{
                    display: block; /* Resmi blok eleman olarak gösterir, böylece margin ayarları doğru şekilde uygulanır */
                    margin: 0; /* Resmin marginlerini sıfırlar */
                }}
                .footer p {{
                    margin: 0; /* Footer içindeki paragrafların marginlerini sıfırlar */
                }}
            </style>
        </head>
        <body>
            <div class="container"> <!-- Ana içerik kapsayıcısı -->
                <div class="header"> <!-- Header bölümü -->
                    <img src="images/customer.png" alt="{müşteri}"> <!-- Header'da yer alan logo resmi -->
                    <h2>Lightning protection Risk management</h2> <!-- Başlık -->
                    <p>Created according to international standard: IEC 62305-2:2010-12</p><br> <!-- İlk bilgi metni -->
                    <p>Considering the country-specific annexes for: IEC 62305-2:2010-12</p><br> <!-- İkinci bilgi metni -->
                    <p><strong>Summary of measures for reducing damage caused by lightning effects, resulting from the risk management concerning the following project:</strong></p> <!-- Üçüncü bilgi metni, kalın olarak vurgulanmış -->
                </div>
                <div class="content"> <!-- İçerik bölümü -->
                    <p><strong>Date:</strong> {tarih}</p> <!-- Tarih bilgisi -->
                    <p><strong>Project No.:</strong> {proje_no}</p> <!-- Proje numarası -->
                    <p><strong>Project / object description:</strong>{açıklama}</p> <!-- Proje açıklaması -->
                    <p><strong>Customer / principal:</strong> {müşteri}</p> <!-- Müşteri bilgisi -->
                    <p><strong>Risk assessment by:</strong> {yazar}</p> <!-- Risk değerlendirmesi yapan kişi -->
                </div>
            </div>
            <div class="footer"> <!-- Footer bölümü -->
                <img src="images/logo.png" alt="Radsan Logo" width="80" height="35"> <!-- Footer'da yer alan logo resmi -->
                <p>Radsan Risk Tools - {tarih}</p> <!-- Footer'da yer alan metin -->
                <p>Page 1 of 19</p> <!-- Footer'da yer alan sayfa numarası -->
            </div>
        </body>
        </html>

        """
        html_content_2 = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Contents - Risk Analysis</title>
            <style>
                body {{
                    font-family: Arial, sans-serif; /* Sayfadaki yazı tipini Arial olarak ayarlar, Arial mevcut değilse sans-serif kullanılır */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    min-height: 100vh; /* Sayfanın en az yüksekliğini ekran yüksekliği kadar yapar */
                    margin: 0; /* Varsayılan margin değerlerini sıfırlar */
                }}

                .container {{
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    padding: 20px; /* İçeriğin etrafına 20px boşluk ekler */
                }}

                .subsection {{
                    margin-left: 10px; /* Alt bölümün sol tarafına 10px boşluk ekler */
                    margin-bottom: 5px; /* Alt bölümün altına 5px boşluk ekler */
                }}

                .content {{
                    margin-bottom: 20px; /* İçeriğin altına 20px boşluk ekler */
                }}

                .content p {{
                    margin: 8px 0; /* Paragrafların üst ve altına 8px boşluk ekler */
                }}

                p {{
                    margin-bottom: 1px;
                    margin-top: 1px; /* Paragraf altındaki boşluğu ayarlar */
                }}
                h2 {{
                    margin-bottom: 1px;
                    margin-top: 1px; /* Paragraf altındaki boşluğu ayarlar */
                    font-size: 18px; /* Font boyutunu ayarlar */
                }}


                .footer {{
                    display: flex; /* Footer öğelerini yatayda hizalar */
                    justify-content: space-between; /* Footer öğeleri arasında boşluk bırakır */
                    align-items: center; /* Footer öğelerini dikeyde ortalar */
                    margin-top: 10px; /* Footer'ın üstüne 10px boşluk ekler */
                    padding: 10px 20px; /* İç boşlukları belirler */
                    background-color: #f1f1f1; /* Footer'ın arka plan rengini belirler */
                }}
                .footer img {{
                    display: block; /* Resmi blok eleman olarak gösterir, böylece margin ayarları doğru şekilde uygulanır */
                    margin: 0; /* Resmin marginlerini sıfırlar */
                }}
                .footer p {{
                    margin: 0; /* Footer içindeki paragrafların marginlerini sıfırlar */
                }}

                .top-right-image {{
                    position: absolute; /* Resmi sayfanın köşesine yerleştirir */
                    top: 0;
                    right: 0;
                    width: 80px; /* Resmin genişliğini ayarlar */
                    height: auto; /* Yüksekliği otomatik ayarlar */
                    margin: 5px; /* Resme biraz boşluk bırakır */
                }}

                .caption {{
                    text-align: center; /* Açıklamayı ortalar */
                    margin-top: 5px; /* Açıklamanın üstüne 5px boşluk ekler */
                    font-size: 14px; /* Yazı boyutunu belirler */
                    color: #555; /* Yazı rengini belirler */
                }}
            </style>
        </head>
        <body>
            <div class="container"> <!-- Ana içerik kapsayıcısı -->
                <img src="images/customer.png" alt="{müşteri}" class="top-right-image"> <!-- Sağ üst köşede yer alan resim -->
                <p>Risk analysis for assessing the risk for structures<br>according to IEC 62305-2:2010-12</p> <!-- Açıklama metni -->
                <div class="content"></div>
            <ol>
                <li><strong>Abbreviations</strong></li>
                <li><strong>Normative basics</strong></li>
                <li><strong>Risk and sources of damage</strong></li>
                <li><strong>Project data</strong>
                    <ol>
                        <li>Selection of risks to be considered</li>
                        <li>Geographic and building parameters</li>
                        <li>Division of the structure into lightning protection zones/zones</li>
                    </ol>
                </li>
                <li><strong>Supply lines</strong></li>
                <li><strong>Properties of the structure</strong>
                    <ol>
                        <li>Risk of fire</li>
                        <li>Measures to reduce the consequences of a fire</li>
                        <li>Special hazards in the building for persons</li>
                        <li>External spatial shielding</li>
                    </ol>
                </li>
                <li><strong>Risk assessment</strong>
                    <ol>
                        <li>Risk R1, Human life</li>
                        <li>Risk R2, Service to the public</li>
                        <li>Risk R3, Cultural heritage</li>
                        <li>Risk R4, Economic value

                        </li>
                    </ol>
                </li>
                <li><strong>Selection of protection measures</strong></li>
                <li><strong>Legal obligation</strong></li>
                <li><strong>General information</strong></li>
                <li><strong>Definition</strong></li>
            </div>
            <footer class="footer"> <!-- Footer bölümü -->
                <img src="images/logo.png" alt="Radsan Logo" width="80" height="35"> <!-- Footer'da yer alan logo resmi -->
                <p>Radsan Risk Tools - {tarih}</p> <!-- Footer'da yer alan metin -->
                <p>Page 2 of 19</p> <!-- Footer'da yer alan sayfa numarası -->
            </footer>
        </body>
        </html>

        """
        html_content_3 = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Contents - Risk Analysis</title>
            <style>
                body {{
                    font-family: Arial, sans-serif; /* Sayfadaki yazı tipini Arial olarak ayarlar, Arial mevcut değilse sans-serif kullanılır */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    min-height: 100vh; /* Sayfanın en az yüksekliğini ekran yüksekliği kadar yapar */
                    margin: 0; /* Varsayılan margin değerlerini sıfırlar */
                }}

                .container {{
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    padding: 20px; /* İçeriğin etrafına 20px boşluk ekler */
                }}

                .subsection {{
                    margin-left: 10px; /* Alt bölümün sol tarafına 10px boşluk ekler */
                    margin-bottom: 5px; /* Alt bölümün altına 5px boşluk ekler */
                }}

                .content {{
                    margin-bottom: 20px; /* İçeriğin altına 20px boşluk ekler */
                }}

                .content p {{
                    margin: 8px 0; /* Paragrafların üst ve altına 8px boşluk ekler */
                }}

                p {{
                    margin-bottom: 1px;
                    margin-top: 1px;
                    font-size: 14px;  /* Paragraf altındaki boşluğu ayarlar */
                }}
                h2 {{
                    margin-bottom: 1px;
                    margin-top: 1px; /* Paragraf altındaki boşluğu ayarlar */
                    font-size: 18px; /* Font boyutunu ayarlar */
                }}
                li {{
                    margin-bottom: 1px;
                    margin-top: 1px; /* Paragraf altındaki boşluğu ayarlar */
                    font-size: 18px; /* Font boyutunu ayarlar */
                }}


                .footer {{
                    display: flex; /* Footer öğelerini yatayda hizalar */
                    justify-content: space-between; /* Footer öğeleri arasında boşluk bırakır */
                    align-items: center; /* Footer öğelerini dikeyde ortalar */
                    margin-top: 10px; /* Footer'ın üstüne 10px boşluk ekler */
                    padding: 10px 20px; /* İç boşlukları belirler */
                    background-color: #f1f1f1; /* Footer'ın arka plan rengini belirler */
                }}
                .footer img {{
                    display: block; /* Resmi blok eleman olarak gösterir, böylece margin ayarları doğru şekilde uygulanır */
                    margin: 0; /* Resmin marginlerini sıfırlar */
                }}
                .footer p {{
                    margin: 0; /* Footer içindeki paragrafların marginlerini sıfırlar */
                }}

                .top-right-image {{
                    position: absolute; /* Resmi sayfanın köşesine yerleştirir */
                    top: 0;
                    right: 0;
                    width: 80px; /* Resmin genişliğini ayarlar */
                    height: auto; /* Yüksekliği otomatik ayarlar */
                    margin: 5px; /* Resme biraz boşluk bırakır */
                }}

                .caption {{
                    text-align: center; /* Açıklamayı ortalar */
                    margin-top: 5px; /* Açıklamanın üstüne 5px boşluk ekler */
                    font-size: 14px; /* Yazı boyutunu belirler */
                    color: #555; /* Yazı rengini belirler */
                }}
            </style>
        </head>
        <body>
            <div class="container"> <!-- Ana içerik kapsayıcısı -->
                <img src="images/customer.png" alt="Açıklama" class="top-right-image"> <!-- Sağ üst köşede yer alan resim -->
                <p>Risk analysis for assessing the risk for structures<br>according to IEC 62305-2:2010-12</p> <!-- Açıklama metni -->
                <div class="content"></div>
            <ol>
                <li><strong>Abbreviations</strong></li>
            </ol>
            <p><strong>a</strong> Amortisation rate</p>
            <p><strong>a<sub>t</sub></strong> Amortisation period</p>
            <p><strong>c<sub>a</sub></strong> Value of animals in a zone in currency</p>
            <p><strong>c<sub>b</sub></strong> Value of a zone of the structure in currency</p>
            <p><strong>c<sub>c</sub></strong> Value of the contents of a zone in currency</p>
            <p><strong>c<sub>s</sub></strong> Value of the systems in a zone (including their activities) in currency</p>
            <p><strong>c<sub>t</sub></strong> Total value of the structure in currency</p>
            <p><strong>C<sub>D</sub>;C<sub>DJ</sub></strong> Location factor</p>
            <p><strong>C<sub>L</sub></strong> Annual costs of the total loss without protection measures</p>
            <p><strong>C<sub>PM</sub></strong> Annual costs of the selected protection measures</p>
            <p><strong>C<sub>RL</sub></strong> Annual costs of the residual loss</p>
            <p><strong>EB</strong> Lightning equipotential bonding</p>
            <p><strong>H</strong> Height of the structure</p>
            <p><strong>H<sub>P</sub></strong> Highest point of the structure</p>
            <p><strong>i</strong> Interest rate</p>
            <p><strong>K<sub>S1</sub></strong> Factor relevant to the shielding effectiveness of a structure (external spatial shielding)</p>
            <p><strong>K<sub>S1W</sub></strong> Mesh size of the shielding of a structure</p>
            <p><strong>K<sub>S2</sub></strong> Factor relevant to the shielding effectiveness of a structure (external spatial shielding)</p>
            <p><strong>K<sub>S2W</sub></strong> Mesh size of the shielding within a structure</p>
            <p><strong>L1</strong> Loss of human life</p>
            <p><strong>L2</strong> Loss of service to the public</p>
            <p><strong>L3</strong> Loss of cultural heritage</p>
            <p><strong>L4</strong> Loss of economic value</p>
            <p><strong>L</strong> Length of the structure</p>
            <p><strong>LEMP</strong> Lightning electromagnetic impulse</p>
            <p><strong>LP</strong> Lightning protection (consisting of a lightning protection system (LPS) and LEMP protection measures)</p>
            <p><strong>LPL</strong> Lightning protection level</p>
            <p><strong>LPS</strong> Lightning protection system</p>
            <p><strong>LPZ</strong> Lightning protection zone (zone where the lightning electromagnetic environment is defined)</p>
            <p><strong>m</strong> Maintenance rates</p>
            <p><strong>N<sub>D</sub></strong> Frequency of dangerous events caused by lightning strikes to a structure</p>
            <p><strong>N<sub>G</sub></strong> Ground flash density</p>
            <p><strong>P<sub>B</sub></strong> Probability that a lightning strike to a structure causes physical damage</p>
            <p><strong>PEB</strong> Lightning equipotential bonding</p>
            <p><strong>PSPD</strong> Coordinated SPD system</p>
            <p><strong>R</strong> Risk</p>
            <p><strong>R<sub>1</sub></strong> Risk of loss of human life in a structure</p>
            <p><strong>R<sub>2</sub></strong> Risk of loss of service to the public</p>
            <p><strong>R<sub>3</sub></strong> Risk of loss of cultural heritage</p>
            <p><strong>R<sub>4</sub></strong> Risk of loss of economical value in a structure</p>
            <p><strong>R<sub>A</sub></strong> Risk component (injury to living beings - Lightning strike to the structure)</p>
        </div>
        <footer class="footer"> <!-- Footer bölümü -->
            <img src="images/logo.png" alt="Radsan Logo" width="80" height="35"> <!-- Footer'da yer alan logo resmi -->
            <p>Radsan Risk Tools - {tarih}</p> <!-- Footer'da yer alan metin -->
            <p>Page 3 of 19</p> <!-- Footer'da yer alan sayfa numarası -->
        </footer>
        </body>

        </html>

        """
        html_content_4 = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Contents - Risk Analysis</title>
            <style>
                body {{
                    font-family: Arial, sans-serif; /* Sayfadaki yazı tipini Arial olarak ayarlar, Arial mevcut değilse sans-serif kullanılır */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    min-height: 100vh; /* Sayfanın en az yüksekliğini ekran yüksekliği kadar yapar */
                    margin: 0; /* Varsayılan margin değerlerini sıfırlar */
                }}

                .container {{
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    padding: 20px; /* İçeriğin etrafına 20px boşluk ekler */
                }}

                .subsection {{
                    margin-left: 10px; /* Alt bölümün sol tarafına 10px boşluk ekler */
                    margin-bottom: 5px; /* Alt bölümün altına 5px boşluk ekler */
                }}

                .content {{
                    margin-bottom: 20px; /* İçeriğin altına 20px boşluk ekler */
                }}

                .content p {{
                    margin: 8px 0; /* Paragrafların üst ve altına 8px boşluk ekler */
                }}

                p {{
                    margin-bottom: 1px;
                    margin-top: 1px;
                    font-size: 14px;  /* Paragraf altındaki boşluğu ayarlar */
                }}
                h2 {{
                    margin-bottom: 1px;
                    margin-top: 1px; /* Paragraf altındaki boşluğu ayarlar */
                    font-size: 18px; /* Font boyutunu ayarlar */
                }}
                ul {{
                    margin-bottom: 1px;
                    margin-top: 1px; /* Paragraf altındaki boşluğu ayarlar */
                    font-size: 18px; /* Font boyutunu ayarlar */
                }}
                li {{
                    margin-bottom: 1px;
                    margin-top: 1px; /* Paragraf altındaki boşluğu ayarlar */
                    font-size: 14px; /* Font boyutunu ayarlar */
                }}


                .footer {{
                    display: flex; /* Footer öğelerini yatayda hizalar */
                    justify-content: space-between; /* Footer öğeleri arasında boşluk bırakır */
                    align-items: center; /* Footer öğelerini dikeyde ortalar */
                    margin-top: 10px; /* Footer'ın üstüne 10px boşluk ekler */
                    padding: 10px 20px; /* İç boşlukları belirler */
                    background-color: #f1f1f1; /* Footer'ın arka plan rengini belirler */
                }}
                .footer img {{
                    display: block; /* Resmi blok eleman olarak gösterir, böylece margin ayarları doğru şekilde uygulanır */
                    margin: 0; /* Resmin marginlerini sıfırlar */
                }}
                .footer p {{
                    margin: 0; /* Footer içindeki paragrafların marginlerini sıfırlar */
                }}

                .top-right-image {{
                    position: absolute; /* Resmi sayfanın köşesine yerleştirir */
                    top: 0;
                    right: 0;
                    width: 80px; /* Resmin genişliğini ayarlar */
                    height: auto; /* Yüksekliği otomatik ayarlar */
                    margin: 5px; /* Resme biraz boşluk bırakır */
                }}

                .caption {{
                    text-align: center; /* Açıklamayı ortalar */
                    margin-top: 5px; /* Açıklamanın üstüne 5px boşluk ekler */
                    font-size: 14px; /* Yazı boyutunu belirler */
                    color: #555; /* Yazı rengini belirler */
                }}
            </style>
        </head>
        <body>
            <div class="container"> <!-- Ana içerik kapsayıcısı -->
                <img src="images/customer.png" alt="Açıklama" class="top-right-image"> <!-- Sağ üst köşede yer alan resim -->
                <p>Risk analysis for assessing the risk for structures<br>according to IEC 62305-2:2010-12</p> <!-- Açıklama metni -->
                <div class="content"></div>
            <ol>
                <li><strong>Abbreviations</strong></li>
            </ol>
            <p><strong>R<sub>B</sub></strong> Risk component (physical damage to a structure - Lightning strike to the structure)</p>
            <p><strong>R<sub>C</sub></strong> Risk component (failure of internal systems - Lightning strike to the structure)</p>
            <p><strong>R<sub>M</sub></strong> Risk component (failure of internal systems - Lightning strike near the structure)</p>
            <p><strong>R<sub>U</sub></strong> Risk component (injury to living beings - Lightning strike to a connected supply line)</p>
            <p><strong>R<sub>V</sub></strong> Risk component (physical damage to a structure - Lightning strike to a connected supply line)</p>
            <p><strong>R<sub>W</sub></strong> Risk component (failure of internal systems - Lightning strike to a connected supply line)</p>
            <p><strong>R<sub>Z</sub></strong> Risk component (failure of internal systems - Lightning strike near the connected supply line)</p>
            <p><strong>R<sub>T</sub></strong> Tolerable risk (maximum value of the risk which can be tolerated for the structure to be protected)</p>
            <p><strong>r<sub>f</sub></strong> Reduction factor considering the fire risk in a structure</p>
            <p><strong>r<sub>p</sub></strong> Reduction factor considering the measures to reduce the consequences of a fire</p>
            <p><strong>S<sub>M</sub></strong> Annual savings</p>
            <p><strong>SPD</strong> Surge protection device</p>
            <p><strong>SPM</strong> LEMP protection measures (measures to reduce the risk of failure of electrical and electronic equipment due to LEMP)</p>
            <p><strong>t<sub>ex</sub></strong> Duration of the presence of a dangerous explosive atmosphere</p>
            <p><strong>W</strong> Width of the structure</p>
            <p><strong>Z</strong> Zones of a structure</p>
            <ol start="2">
                <li><strong>Normative basics</strong></li>
            </ol>
            <p>The IEC 62305 standard series consists of the following parts:</p>
            <ul>
                <li>IEC 62305-1:2010-12 - "Protection against lightning - Part 1: General principles"</li>
                <li>IEC 62305-2:2010-12 - "Protection against lightning - Part 2: Risk management"</li>
                <li>IEC 62305-3:2010-12 - "Protection against lightning - Part 3: Physical damage to structures and life hazard"</li>
                <li>IEC 62305-4:2010-12 - "Protection against lightning - Part 4: Electrical and electronic systems within structures"</li>
            </ul>
            <ol start="3">
                <li><strong>Risk and sources of damage</strong></li>
            </ol>
            <p>In order to avoid damage resulting from a lightning strike, specific protection measures must be taken for the objects to be protected. The risk management described in the IEC 62305-2:2010-12 standard includes a risk analysis which allows to determine the lightning protection requirements of a structure. The aim of the risk management is to reduce the risk to an acceptable level by taking protection measures.</p>
            <p>To determine the prevailing risk, the relevant object must be considered without any protection measures (actual condition). Risks that may be caused as a result of direct / indirect lightning strikes to the structure and supply lines are referred to as risk R. The risk defines the possible annual loss. Risks that must be assessed for a structure could be:</p>
            <ul>
                <li>Risk R<sub>1</sub>: risk of loss of human life;</li>
                <li>Risk R<sub>2</sub>: risk of loss of services to the public;</li>
                <li>Risk R<sub>3</sub>: risk of loss of cultural heritage;</li>
                <li>Risk R<sub>4</sub>:risk of loss of economic value;</li>
            </ul>
            </div>
            <footer class="footer"> <!-- Footer bölümü -->
                <img src="images/logo.png" alt="Radsan Logo" width="80" height="35"> <!-- Footer'da yer alan logo resmi -->
                <p>Radsan Risk Tools - {tarih}</p> <!-- Footer'da yer alan metin -->
                <p>Page 4 of 19</p> <!-- Footer'da yer alan sayfa numarası -->
            </footer>
        </body>


        </html>

        """
        html_content_5 = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Risk Analysis</title>
            <style>
                body {{
                    font-family: Arial, sans-serif; /* Sayfadaki yazı tipini Arial olarak ayarlar, Arial mevcut değilse sans-serif kullanılır */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    min-height: 100vh; /* Sayfanın en az yüksekliğini ekran yüksekliği kadar yapar */
                    margin: 0; /* Varsayılan margin değerlerini sıfırlar */
                }}

                .container {{
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    padding: 20px; /* İçeriğin etrafına 20px boşluk ekler */
                }}

                .subsection {{
                    margin-left: 10px; /* Alt bölümün sol tarafına 10px boşluk ekler */
                    margin-bottom: 5px; /* Alt bölümün altına 5px boşluk ekler */
                }}

                .content {{
                    margin-bottom: 20px; /* İçeriğin altına 20px boşluk ekler */
                }}

                .content p {{
                    margin: 8px 0; /* Paragrafların üst ve altına 8px boşluk ekler */
                }}
                .image-section {{
                    text-align: center; /* Görsel bölümünü ortalar */
                    margin: 20px 0; /* Görsel bölümünün üst ve altına 10px boşluk ekler */
                }}

                .image-section img {{
                    max-width: 100%; /* Görselin maksimum genişliğini %100 yapar */
                    height: auto; /* Görselin yüksekliğini otomatik ayarlar */
                }}


                p {{
                    margin-bottom: 1px;
                    margin-top: 1px; /* Paragraf altındaki boşluğu ayarlar */
                }}
                h2 {{
                    margin-bottom: 1px;
                    margin-top: 1px; /* Paragraf altındaki boşluğu ayarlar */
                    font-size: 18px; /* Font boyutunu ayarlar */
                }}

                .footer {{
                    display: flex; /* Footer öğelerini yatayda hizalar */
                    justify-content: space-between; /* Footer öğeleri arasında boşluk bırakır */
                    align-items: center; /* Footer öğelerini dikeyde ortalar */
                    padding: 10px 20px; /* İç boşlukları belirler */
                    background-color: #f1f1f1; /* Footer'ın arka plan rengini belirler */
                }}
                .footer img {{
                    display: block; /* Resmi blok eleman olarak gösterir, böylece margin ayarları doğru şekilde uygulanır */
                    margin: 0; /* Resmin marginlerini sıfırlar */
                }}
                .footer p {{
                    margin: 0; /* Footer içindeki paragrafların marginlerini sıfırlar */
                }}

                .top-right-image {{
                    position: absolute; /* Resmi sayfanın köşesine yerleştirir */
                    top: 0;
                    right: 0;
                    width: 80px; /* Resmin genişliğini ayarlar */
                    height: auto; /* Yüksekliği otomatik ayarlar */
                    margin: 5px; /* Resme biraz boşluk bırakır */
                }}

                .caption {{
                    text-align: center; /* Açıklamayı ortalar */
                    margin-top: 5px; /* Açıklamanın üstüne 5px boşluk ekler */
                    font-size: 14px; /* Yazı boyutunu belirler */
                    color: #555; /* Yazı rengini belirler */
                }}

                /* Footer'ı sayfanın en altına yerleştirmek için */
                html, body {{
                    height: 100%;
                }}

                .footer {{
                    margin-top: auto; /* Footer'ı sayfanın en altına itmek için */
                }}
            </style>
        </head>
        <body>
            <div class="container"> <!-- Ana içerik kapsayıcısı -->
                <img src="images/customer.png" alt="Açıklama" class="top-right-image"> <!-- Sağ üst köşede yer alan resim -->
                <p>Risk analysis for assessing the risk for structures<br>according to IEC 62305-2:2010-12</p> <!-- Açıklama metni -->
                <div class="content"></div>


                    <p>All risks or the individual risks must be assessed depending on the type of consideration. Every risk is defined with a tolerable risk in form of a numerical value. To achieve a tolerable risk, technically and economically sound protection measures are defined e.g. external lightning protection measures according to IEC 62305-3:2010-12 and SPD measures according to IEC 62305-4:2010-12.</p>
                    <p>To be able to determine the risk focus more exactly, the risks are considered in detail. Every risk consists of a sum of risk components.</p>
                    <ul>
                        <li>R<sub>1</sub> = R<sub>A</sub> + R<sub>B</sub> + R<sub>C</sub> + R<sub>M</sub> + R<sub>U</sub> + R<sub>V</sub> + R<sub>W</sub> + R<sub>Z</sub></li>
                        <li>R<sub>2</sub> = R<sub>B</sub> + R<sub>C</sub> + R<sub>M</sub> + R<sub>V</sub> + R<sub>W</sub> + R<sub>Z</sub></li>
                        <li>R<sub>3</sub> = R<sub>B</sub> + R<sub>V</sub></li>
                        <li>R<sub>4</sub> = R<sub>A</sub> + R<sub>B</sub> + R<sub>C</sub> + R<sub>M</sub> + R<sub>U</sub> + R<sub>V</sub> + R<sub>W</sub> + R<sub>Z</sub></li>
                    </ul>
                    <p>Every risk component describes a certain danger and thus a possible loss. The loss resulting from lightning effects is defined as follows:</p>
                    <ul>
                        <li>L1 = Loss of human life</li>
                        <li>L2 = Loss of service to the public</li>
                        <li>L3 = Loss of cultural heritage</li>
                        <li>L4 = Loss of economic value</li>
                    </ul>
                    <p>The possible loss is assigned to the risk components as follows:</p>
                    <p>The risk components are differentiated according to the sources of damage.</p>
                <div>
                <div class="image-section">
                    <img src="images/fire.png" alt="Graph Image" width="340" sheight="auto">
                </div>
                <div class="content">
                    <h3>Source of damage S1: Risk components based on lightning strikes to the structure</h3>
                    <p><strong>R<sub>A</sub></strong> Component which refers to injury of living beings caused by an electric shock resulting from touch and step voltage within the structure and up to 3 m around the down conductors outside the structure. Type of damage L1 may occur for agricultural buildings and type of damage L4 with possible loss of animals.</p>
                    <p><strong>R<sub>B</sub></strong> Component which refers to physical damage caused by dangerous sparking within the structure resulting in fire and explosion. Even the environment can be at risk. All types of damage can occur (L1, L2, L3, L4).</p>
                </div>
            </div>
            <footer class="footer"> <!-- Footer bölümü -->
                <img src="images/logo.png" alt="Radsan Logo" width="80" height="35"> <!-- Footer'da yer alan logo resmi -->
                <p>Radsan Risk Tools - {tarih}</p> <!-- Footer'da yer alan metin -->
                <p>Page 5 of 19</p> <!-- Footer'da yer alan sayfa numarası -->
            </footer>
        </body>
        </html>

        """
        html_content_6 =  f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Risk Analysis</title>
            <style>
                body {{
                    font-family: Arial, sans-serif; /* Sayfadaki yazı tipini Arial olarak ayarlar, Arial mevcut değilse sans-serif kullanılır */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    min-height: 100vh; /* Sayfanın en az yüksekliğini ekran yüksekliği kadar yapar */
                    margin: 0; /* Varsayılan margin değerlerini sıfırlar */
                }}

                .container {{
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    padding: 20px; /* İçeriğin etrafına 20px boşluk ekler */
                }}

                .subsection {{
                    margin-left: 10px; /* Alt bölümün sol tarafına 10px boşluk ekler */
                    margin-bottom: 5px; /* Alt bölümün altına 5px boşluk ekler */
                }}

                .content {{
                    margin-bottom: 20px; /* İçeriğin altına 20px boşluk ekler */
                }}

                .content p {{
                    margin: 8px 0; /* Paragrafların üst ve altına 8px boşluk ekler */
                }}

                p {{
                    margin-bottom: 1px;
                    margin-top: 1px; /* Paragraf altındaki boşluğu ayarlar */
                }}
                h2 {{
                    margin-bottom: 15px;
                    margin-top: 15px; /* Paragraf altındaki boşluğu ayarlar */
                    font-size: 18px; /* Font boyutunu ayarlar */
                }}


                .footer {{
                    display: flex; /* Footer öğelerini yatayda hizalar */
                    justify-content: space-between; /* Footer öğeleri arasında boşluk bırakır */
                    align-items: center; /* Footer öğelerini dikeyde ortalar */
                    margin-top: 10px; /* Footer'ın üstüne 10px boşluk ekler */
                    padding: 10px 20px; /* İç boşlukları belirler */
                    background-color: #f1f1f1; /* Footer'ın arka plan rengini belirler */
                }}
                .footer img {{
                    display: block; /* Resmi blok eleman olarak gösterir, böylece margin ayarları doğru şekilde uygulanır */
                    margin: 0; /* Resmin marginlerini sıfırlar */
                }}
                .footer p {{
                    margin: 0; /* Footer içindeki paragrafların marginlerini sıfırlar */
                }}

                .top-right-image {{
                    position: absolute; /* Resmi sayfanın köşesine yerleştirir */
                    top: 0;
                    right: 0;
                    width: 80px; /* Resmin genişliğini ayarlar */
                    height: auto; /* Yüksekliği otomatik ayarlar */
                    margin: 5px; /* Resme biraz boşluk bırakır */
                }}

                .caption {{
                    text-align: center; /* Açıklamayı ortalar */
                    margin-top: 5px; /* Açıklamanın üstüne 5px boşluk ekler */
                    font-size: 14px; /* Yazı boyutunu belirler */
                    color: #555; /* Yazı rengini belirler */
                }}
            </style>
        </head>
        <body>
            <div class="container"> <!-- Ana içerik kapsayıcısı -->
                <img src="images/customer.png" alt="Açıklama" class="top-right-image"> <!-- Sağ üst köşede yer alan resim -->
                <p>Risk analysis for assessing the risk for structures<br>according to IEC 62305-2:2010-12</p> <!-- Açıklama metni -->
                <div class="content"></div>


                <p><b>R<sub>C</sub></b> : Component which refers to the failure of internal systems caused by LEMP. Types of damage L2 and L4 can occur in all cases and type of damage L1 in case of structures with a risk of explosion and hospitals or other structures in which the failure of internal systems can be lead to loss of human life.</p>
                
                <h2>Source of damage S2: Risk components for a structure as a result of lightning strikes near the structure</h2>
                <p><b>R<sub>M</sub></b> : Component which refers to the failure of internal systems caused by LEMP. Types of damage L2 and L4 can occur in all cases and type of damage L1 in case of structures with a risk of explosion and hospitals or other structures in which the failure of internal systems can be lead to loss of human life.</p>
                
                <h2>Source of damage S3: Risk components for a structure as a result of lighting strikes to the incoming supply line</h2>
                <p><b>R<sub>U</sub></b> : Component which refers to injury of living beings caused by an electric shock resulting from touch voltage within the structure. Type of damage L1 may occur for agriculture facilities and type of damage L4 with possible loss of animals.</p>
                <p><b>R<sub>V</sub></b> : Component which refers to physical damage caused by the lightning current injected into the structure by means of or along the supply line (fire or explosion due to dangerous sparking between the external installation and the metal parts, typically at the point where the supply line enters the structure). All types of damage (L1, L2, L3, L4) can occur.</p>
                <p><b>R<sub>W</sub></b> : Component which refers to the failure of internal systems caused by overvoltages injected into the structure by means of incoming supply lines. Types of damage L2 and L4 can occur in all cases and type of damage L1 in case of structures with a risk of explosion and hospitals or other structures in which the failure of internal systems can be lead to loss of human life.</p>
                
                <h2>Source of damage S4: Risk components for a structure as a result of lighting strikes near the incoming supply line</h2>
                <p><b>R<sub>Z</sub></b> : Component which refers to the failure of internal systems caused by overvoltages injected into the structure by means of incoming supply lines. Types of damage L2 and L4 can occur in all cases and type of damage L1 in case of structures with a risk of explosion and hospitals or other structures in which the failure of internal systems can be lead to loss of human life.</p>
                <br>
                <p>The risk components allow to analyse the risks and measures to avoid possible loss can be taken.</p>
                <br>
                <p>The following risk analysis according to IEC 62305-2:2010-12 for the this project - object {yapı_konum} shows the necessity of protection measures. The risk potential for the structure is determined and, if necessary, measures to reduce the risk have to be taken. The result of the risk analysis not only specifies the class of LPS, but also provides a complete protection concept including the</p>
                
            </div>
            <footer class="footer"> <!-- Footer bölümü -->
                <img src="images/logo.png" alt="Radsan Logo" width="80" height="35"> <!-- Footer'da yer alan logo resmi -->
                <p>Radsan Risk Tools - {tarih}</p> <!-- Footer'da yer alan metin -->
                <p>Page 6 of 19</p> <!-- Footer'da yer alan sayfa numarası -->
            </footer>
        </body>
        </html>
        """
        html_content_7 = f"""
        <!DOCTYPE html> <!-- HTML5 belge türü tanımı -->
        <html lang="tr"> <!-- Belge dilini Türkçe olarak belirtir -->
        <head>
            <meta charset="UTF-8"> <!-- Belgenin karakter kodlamasını UTF-8 olarak ayarlar -->
            <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Sayfa boyutunu ve ölçeğini ayarlar, mobil uyumluluğu sağlar -->
            <title>Risk Analysis for Assessing the Risk for Structures</title> <!-- Sayfanın başlık etiketini belirtir -->
            <style>
                body {{
                    font-family: Arial, sans-serif; /* Sayfadaki yazı tipini Arial olarak ayarlar, Arial mevcut değilse sans-serif kullanılır */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    min-height: 100vh; /* Sayfanın en az yüksekliğini ekran yüksekliği kadar yapar */
                    margin: 0; /* Varsayılan margin değerlerini sıfırlar */
                }}

                .section {{
                    flex: 1; /* Bölümün esnekliğini sağlar */
                    margin-bottom: 20px; /* Bölümün altına 20px boşluk ekler */
                }}

                .subsection {{
                    margin-left: 20px; /* Alt bölümün sol tarafına 20px boşluk ekler */
                    margin-bottom: 10px; /* Alt bölümün altına 10px boşluk ekler */
                }}

                .risk-table {{
                    width: 100%; /* Tablo genişliğini %100 yapar */
                    border-collapse: collapse; /* Tablonun kenar boşluklarını kaldırır */
                    margin: 30px 0; /* Tablonun üst ve altına 30px boşluk ekler */
                }}

                .risk-table th, .risk-table td {{
                    border: 1px solid #dddddd; /* Tablo hücrelerinin kenarlıklarını belirler */
                    text-align: left; /* Hücre içeriğini sola hizalar */
                    padding: 4px; /* Hücrelerin içindeki boşluğu 4px yapar */
                }}

                .risk-table th {{
                    background-color: #f2f2f2; /* Tablo başlık hücrelerinin arka plan rengini belirler */
                }}

                .footer {{
                    display: flex; /* Footer öğelerini yatayda hizalar */
                    justify-content: space-between; /* Footer öğeleri arasında boşluk bırakır */
                    align-items: center; /* Footer öğelerini dikeyde ortalar */
                    margin-top: 10px; /* Footer'ın üstüne 10px boşluk ekler */
                    padding: 10px 20px; /* İç boşlukları belirler */
                    background-color: #f1f1f1; /* Footer'ın arka plan rengini belirler */
                }}
                .footer img {{
                    display: block; /* Resmi blok eleman olarak gösterir, böylece margin ayarları doğru şekilde uygulanır */
                    margin: 0; /* Resmin marginlerini sıfırlar */
                }}
                .footer p {{
                    margin: 0; /* Footer içindeki paragrafların marginlerini sıfırlar */
                }}

                /* Sağ üst köşede yer alan resim için stil */
                .top-right-image {{
                    position: absolute; /* Resmi sayfanın köşesine yerleştirir */
                    top: 0;
                    right: 0;
                    width: 100px; /* Resmin genişliğini ayarlar */
                    height: auto; /* Yüksekliği otomatik ayarlar */
                    margin: 10px; /* Resme biraz boşluk bırakır */
                }}
                
                /* Konteynerin konumunu belirlemek için */
                .container {{
                    position: relative; /* Konteynerin göreceli konumunu belirler */
                }}
            </style>
        </head>
        <body>
            <div class="container"> <!-- Ana içerik kapsayıcısı -->
                <img src="images/customer.png" alt="Açıklama" class="top-right-image"> <!-- Sağ üst köşede yer alan resim -->
                <p>Risk analysis for assessing the risk for structures<br>according to IEC 62305-2:2010-12</p> <!-- Açıklama metni -->
            </div>

            <div class="section"> <!-- Bölüm -->
                <h2>4. Project data</h2> <!-- Bölüm başlığı -->

                <div class="subsection"> <!-- Alt bölüm -->
                    <h3>4.1 Selection of risks to be considered</h3> <!-- Alt bölüm başlığı -->
                    <p>Due to the type and use of the structure, object {yapı_konum}, the following risks were selected and considered:</p>
                    <table class="risk-table"> <!-- Risk tablosu -->
                        <tr>
                            <th>Risk</th>
                            <th>Description</th>
                            <th>RT</th>
                        </tr>
                        <tr>
                            <td>Risk R<sub>1</sub></td>
                            <td>Risk of losses of human life</td>
                            <td>1,00E-05</td>
                        </tr>
                        <tr>
                            <td>Risk R<sub>2</sub></td>
                            <td>Risk of loss of service to the public</td>
                            <td>1,00E-03</td>
                        </tr>
                        <tr>
                            <td>Risk R<sub>3</sub></td>
                            <td>Risk of loss of cultural heritage</td>
                            <td>1,00E-04</td>
                        </tr>
                        <tr>
                            <td>Risk R<sub>4</sub></td>
                            <td>Risk of loss of economic value</td>
                            <td>1,00E-03</td>
                        </tr>
                    </table>
                    <p>The tolerable risks RT were defined by selecting the risks.</p>
                    <p>The standard specifies the tolerable risk for the risks R<sub>1</sub>, R<sub>2</sub> and R<sub>3</sub>. No tolerable risk is defined for risk R<sub>4</sub>. To this end, it is considered whether the protection measures make economical sense with regard to the value of the structure.</p>
                    <p>The aim of a risk analysis is to reduce the risk to an acceptable level RT by an economically sound selection of protection measures.</p>
                </div>

                <div class="subsection"> <!-- Alt bölüm -->
                    <h3>4.2 Geographic and building parameters</h3> <!-- Alt bölüm başlığı -->
                    <p>The ground flash density Ng is the basis for a risk analysis according to IEC 62305-2:2010-12. It defines the number of direct lightning strikes in 1 year / km². A value of {n_g} lightning strikes / year / km² was determined for the location of the object {yapı_konum} by means of the ground flash density map. As a result, there is a calculated number of {t_d} of thunderstorm days per year for the location of the project.</p>
                    <p>The dimensions of the building are decisive for the risk of a direct strike. The collection areas for direct / indirect lightning strikes are determined based on these dimensions. The structure {yapı_konum} has the following dimensions:</p>
                    <p>L<sub>b</sub> Length: {uzunluk_yapı}</p>
                    <p>W<sub>b</sub> Width: {genişlik_yapı}</p>
                </div>
            </div>

            <div class="footer"> <!-- Footer bölümü -->
                <img src="images/logo.png" alt="Radsan Logo" width="80" height="35"> <!-- Footer'da yer alan logo resmi -->
                <p>Radsan Risk Tools-{tarih}</p> <!-- Footer'da yer alan metin -->
                <p>Page 7 of 19</p> <!-- Footer'da yer alan sayfa numarası -->
            </div>
        </body>
        </html>

        """
        html_content_8 = f"""
        <!DOCTYPE html> <!-- HTML5 belge türü tanımı -->
        <html lang="tr"> <!-- Belge dilini Türkçe olarak belirtir -->
        <head>
            <meta charset="UTF-8"> <!-- Belgenin karakter kodlamasını UTF-8 olarak ayarlar -->
            <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Sayfa boyutunu ve ölçeğini ayarlar, mobil uyumluluğu sağlar -->
            <title>Lightning Protection Risk Management</title> <!-- Sayfanın başlık etiketini belirtir -->
            <style>
                body {{
                    font-family: Arial, sans-serif; /* Sayfadaki yazı tipini Arial olarak ayarlar, Arial mevcut değilse sans-serif kullanılır */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    min-height: 100vh; /* Sayfanın en az yüksekliğini ekran yüksekliği kadar yapar */
                    margin: 0; /* Varsayılan margin değerlerini sıfırlar */
                }}

                .section {{
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */
                    margin-bottom: 20px; /* Bölümün altına 20px boşluk ekler */
                }}

                .subsection {{
                    margin-left: 20px; /* Alt bölümün sol tarafına 20px boşluk ekler */
                    margin-bottom: 10px; /* Alt bölümün altına 10px boşluk ekler */
                }}

                .container {{
                    position: relative; /* Konteynerin göreceli konumunu belirler */
                }}

                .content {{
                    margin-bottom: 20px; /* İçeriğin altına 20px boşluk ekler */
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */
                }}

                .content p {{
                    margin: 10px 0; /* Paragrafların üst ve altına 5px boşluk ekler */
                }}

                .image-section {{
                    text-align: center; /* Görsel bölümünü ortalar */
                    margin: 20px 0; /* Görsel bölümünün üst ve altına 20px boşluk ekler */
                }}

                .image-section img {{
                    max-width: 100%; /* Görselin maksimum genişliğini %100 yapar */
                    height: auto; /* Görselin yüksekliğini otomatik ayarlar */
                }}

                .footer {{
                    display: flex; /* Footer öğelerini yatayda hizalar */
                    justify-content: space-between; /* Footer öğeleri arasında boşluk bırakır */
                    align-items: center; /* Footer öğelerini dikeyde ortalar */
                    margin-top: 10px; /* Footer'ın üstüne 10px boşluk ekler */
                    padding: 10px 20px; /* İç boşlukları belirler */
                    background-color: #f1f1f1; /* Footer'ın arka plan rengini belirler */
                }}
                .footer img {{
                    display: block; /* Resmi blok eleman olarak gösterir, böylece margin ayarları doğru şekilde uygulanır */
                    margin: 0; /* Resmin marginlerini sıfırlar */
                }}
                .footer p {{
                    margin: 0; /* Footer içindeki paragrafların marginlerini sıfırlar */
                }}
                .top-right-image {{
                    position: absolute; /* Resmi sayfanın köşesine yerleştirir */
                    top: 0;
                    right: 0;
                    width: 100px; /* Resmin genişliğini ayarlar */
                    height: auto; /* Yüksekliği otomatik ayarlar */
                    margin: 10px; /* Resme biraz boşluk bırakır */
                }}
            </style>
        </head>
        <body>
            <div class="container"> <!-- Ana içerik kapsayıcısı -->
                <img src="images/customer.png" alt="Açıklama" class="top-right-image"> <!-- Sağ üst köşede yer alan resim -->
                <p>Risk analysis for assessing the risk for structures<br>according to IEC 62305-2:2010-12</p> <!-- Açıklama metni -->
            </div>
            <div class="content"> <!-- İçerik bölümü -->
                <p><strong>Hb Height:</strong> {yükseklik_yapı}</p>
                <p><strong>Hpb Highest point (if applicable):</strong> {yükseklik_yapı_max}</p>
                <p>This results in a calculated collection area for direct lightning strikes of {yapı_AD_alan} m² and for indirect lightning strikes (near the structure) of {ayrık_yapı_AD_alan} m².</p>
                <div class="image-section"> <!-- Görsel bölümü -->
                    <img src="images/complex_structure_ad.png" alt="Graph Image" width="430" sheight="auto">
                </div>
                <p>The environment surrounding the structure is an important factor for determining the number of direct / indirect lightning strikes. It was defined as follows for the building {yapı_konum}</p>
                <p><strong>Relative location Cd:</strong> {c_dj}</p>
                <p>If the ground flash density is referred to the size and the environment of the structure, a frequency of direct strikes Nd to the structure of {n_d} strikes / year.</p>
                <h3>4.3 Division of the structure into lightning protection zones/zones</h3> <!-- Alt bölüm başlığı -->
                <p>The structure {yapı_konum} was not divided into lightning protection zones / zones.</p>
                <h3>5. Supply lines</h3> <!-- Alt bölüm başlığı -->
                <p>All incoming and outgoing supply lines of the structure to be considered must be taken into account in the risk analysis. Conductive pipes do not have to be considered if they are connected to the main earthing busbar of the structure. If this is not the case, the risk of incoming pipes should be considered in the risk analysis (observe that equipotential bonding is required!).</p>
                <p>The following supply lines were considered for the structure {yapı_konum} in the risk analysis:</p>
            </div>
            <div class="footer"> <!-- Footer bölümü -->
                <img src="images/logo.png" alt="Radsan Logo" width="80" height="35"> <!-- Footer'da yer alan logo resmi -->
                <p>Radsan Risk Tools - {tarih}</p> <!-- Footer'da yer alan metin -->
                <p>Page 8 of 19</p> <!-- Footer'da yer alan sayfa numarası -->
            </div>
        </body>
        </html>

        """
        html_content_9 = f"""
        <!DOCTYPE html>
        <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Lightning Protection Risk Management</title>
            <style>
                body {{
                    font-family: Arial, sans-serif; /* Sayfadaki yazı tipini Arial olarak ayarlar, Arial mevcut değilse sans-serif kullanılır */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    min-height: 100vh; /* Sayfanın en az yüksekliğini ekran yüksekliği kadar yapar */
                    margin: 0; /* Varsayılan margin değerlerini sıfırlar */
                }}

                .container {{
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */ /* <-- Fosforla belirtilen değişiklik */
                }}

                .subsection {{
                    margin-left: 20px; /* Alt bölümün sol tarafına 20px boşluk ekler */
                    margin-bottom: 10px; /* Alt bölümün altına 10px boşluk ekler */
                }}

                .content {{
                    margin-bottom: 20px; /* İçeriğin altına 20px boşluk ekler */
                }}

                .content p {{
                    margin: 5px 0; /* Paragrafların üst ve altına 5px boşluk ekler */
                }}

                .image-section {{
                    text-align: center; /* Görsel bölümünü ortalar */
                    margin: 20px 0; /* Görsel bölümünün üst ve altına 20px boşluk ekler */
                }}

                .image-section img {{
                    max-width: 100%; /* Görselin maksimum genişliğini %100 yapar */
                    height: auto; /* Görselin yüksekliğini otomatik ayarlar */
                }}

                .footer {{
                    display: flex; /* Footer öğelerini yatayda hizalar */
                    justify-content: space-between; /* Footer öğeleri arasında boşluk bırakır */
                    align-items: center; /* Footer öğelerini dikeyde ortalar */
                    margin-top: 10px; /* Footer'ın üstüne 10px boşluk ekler */
                    padding: 10px 20px; /* İç boşlukları belirler */
                    background-color: #f1f1f1; /* Footer'ın arka plan rengini belirler */
                }}
                .footer img {{
                    display: block; /* Resmi blok eleman olarak gösterir, böylece margin ayarları doğru şekilde uygulanır */
                    margin: 0; /* Resmin marginlerini sıfırlar */
                }}
                .footer p {{
                    margin: 0; /* Footer içindeki paragrafların marginlerini sıfırlar */
                }}
                .top-right-image {{
                    position: absolute; /* Resmi sayfanın köşesine yerleştirir */
                    top: 0;
                    right: 0;
                    width: 100px; /* Resmin genişliğini ayarlar */
                    height: auto; /* Yüksekliği otomatik ayarlar */
                    margin: 10px; /* Resme biraz boşluk bırakır */
                }}
            </style>
        </head>
        <body>

            <div class="container"> <!-- Ana içerik kapsayıcısı -->
                <img src="images/customer.png" alt="Açıklama" class="top-right-image"> <!-- Sağ üst köşede yer alan resim -->
                <p>Risk analysis for assessing the risk for structures<br>according to IEC 62305-2:2010-12</p> <!-- Açıklama metni -->
                <div class="content">
                    <p>- data</p>
                    <p>- power</p>
                    <h3>5.1 data</h3>
                    <p><strong>Installation factor:</strong> {CI_C}</p>
                    <p><strong>Type of conductor:</strong> {Plı_c}</p>
                    <p><strong>Environment:</strong> {CE_C}</p>
                    <p><strong>Connection of the conductor:</strong> {CLD_c}</p>
                    <p><strong>Transformer:</strong> {CT_C}</p>
                    <p><strong>Conductor shielding:</strong> External: {Pld_C}</p>
                    <p>The conductor length outside the structure up to the next node is {Ll_C}.</p>
                    <p>Based on this, the following collection areas were determined for the supply line:</p>
                    <p>- Collection area for direct lightning strikes to a supply line: {Al_c} m²</p>
                    <p>The dielectric strength of the electrical equipment which is connected with the data is Uw <= {uw_c}</p>
                    <p>{Ptu_c}</p>
                    <h3>5.2 power</h3>
                    <p><strong>Installation factor:</strong> {CI_C}</p>
                    <p><strong>Type of conductor:</strong> {Plı_c}</p>
                    <p><strong>Environment:</strong> {CE_C}</p>
                    <p><strong>Connection of the conductor:</strong> {CLD_c}</p>
                    <p><strong>Transformer:</strong> {CT_C}</p>
                    <p><strong>Conductor shielding:</strong> {Pld_C}</p>
                    <p>The conductor length outside the structure up to the next node is {Ll_C} m.</p>
            
                </div>
            </div>
            <div class="footer"> <!-- Footer bölümü -->
                <img src="images/logo.png" alt="Radsan Logo" width="80" height="35"> <!-- Footer'da yer alan logo resmi -->
                <p>Radsan Risk Tools - {tarih}</p> <!-- Footer'da yer alan metin -->
                <p>Page 9 of 19</p> <!-- Footer'da yer alan sayfa numarası -->
            </div>
        </body>
        </html>

        """
        html_content_10 = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Risk Analysis Report</title>
            <style>
                body {{
                    font-family: Arial, sans-serif; /* Sayfadaki yazı tipini Arial olarak ayarlar, Arial mevcut değilse sans-serif kullanılır */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    min-height: 100vh; /* Sayfanın en az yüksekliğini ekran yüksekliği kadar yapar */
                    margin: 0; /* Varsayılan margin değerlerini sıfırlar */
                }}

                .container {{
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                }}

                .subsection {{
                    margin-left: 10px; /* Alt bölümün sol tarafına 10px boşluk ekler */
                    margin-bottom: 5px; /* Alt bölümün altına 5px boşluk ekler */
                }}

                .content {{
                    margin-bottom: 1px; /* İçeriğin altına 1px boşluk ekler */
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */
                }}

                .content p {{
                    margin: 1px 0; /* Paragrafların üst ve altına 1px boşluk ekler */
                }}

                .image-section {{
                    text-align: center; /* Görsel bölümünü ortalar */
                    margin: 10px 0; /* Görsel bölümünün üst ve altına 10px boşluk ekler */
                }}

                .image-section img {{
                    max-width: 100%; /* Görselin maksimum genişliğini %100 yapar */
                    height: auto; /* Görselin yüksekliğini otomatik ayarlar */
                }}

                .data-table {{
                    width: 100%;
                    border-collapse: collapse;
                }}

                .data-table th, .data-table td {{
                    border: 1px solid #ddd;
                    padding: 4px; /* Hücreler arasındaki boşluğu azaltır */
                }}

                .data-table th {{
                    padding-top: 1px; /* Üst boşluğu azaltır */
                    padding-bottom: 1px; /* Alt boşluğu azaltır */
                    text-align: left;
                    background-color: #f2f2f2;
                }}

                p {{
                    margin-bottom: 5px; /* Paragraf altındaki boşluğu azaltır */
                    line-height: 1; /* Satır yüksekliğini kısaltır (isteğe bağlı) */
                }}

                ul {{
                    margin-top: 5px; /* Liste üstündeki boşluğu azaltır */
                    padding-left: 20px; /* Liste başlığı ile liste elemanları arasındaki boşluğu ayarlar */
                }}       

                .footer {{
                    display: flex; /* Footer öğelerini yatayda hizalar */
                    justify-content: space-between; /* Footer öğeleri arasında boşluk bırakır */
                    align-items: center; /* Footer öğelerini dikeyde ortalar */
                    padding: 10px 20px; /* İç boşlukları belirler */
                    background-color: #f1f1f1; /* Footer'ın arka plan rengini belirler */
                }}

                .footer img {{
                    display: block; /* Resmi blok eleman olarak gösterir, böylece margin ayarları doğru şekilde uygulanır */
                    margin: 0; /* Resmin marginlerini sıfırlar */
                }}

                .footer p {{
                    margin: 0; /* Footer içindeki paragrafların marginlerini sıfırlar */
                }}

                .top-right-image {{
                    position: absolute; /* Resmi sayfanın köşesine yerleştirir */
                    top: 0;
                    right: 0;
                    width: 80px; /* Resmin genişliğini ayarlar */
                    height: auto; /* Yüksekliği otomatik ayarlar */
                    margin: 5px; /* Resme biraz boşluk bırakır */
                }}
            </style>
        </head>
        <body>
            <div class="container"> <!-- Ana içerik kapsayıcısı -->
                <img src="images/customer.png" alt="Açıklama" class="top-right-image"> <!-- Sağ üst köşede yer alan resim -->
                <p>Risk analysis for assessing the risk for structures<br>according to IEC 62305-2:2010-12</p> <!-- Açıklama metni -->
                <div class="content">
                    <table class="data-table">
                        <tr>
                            <th>Length (L<sub>a</sub>)</th>
                            <td>{uzunluk_ayrık_yapı}</td>
                        </tr>
                        <tr>
                            <th>Width (W<sub>a</sub>)</th>
                            <td>{genislik_ayrık_yapı}</td>
                        </tr>
                        <tr>
                            <th>Height (H<sub>a</sub>)</th>
                            <td>{yükseklik_ayrık_yapı}</td>
                        </tr>
                        <tr>
                            <th>Highest point (H<sub>pa</sub>)</th>
                            <td>{yükseklik_ayrık_yapı_max}</td>
                        </tr>
                    </table>

                    <p>As a result, the calculated collection area for lightning strikes to the connected structure is {ayrık_yapı_AD_alan} m².</p>

                    <div class="image-section">
                        <img src="images/complex_structure_adj.png" alt="Graph Image" width="430" sheight="auto">
                    </div>

                    <p>Based on this, the following collection areas were determined for the supply line:</p>
                    <ul>
                    </ul>
                    <p>The dielectric strength of the electrical equipment which is connected with the power is  {uw_c}</p>
                    <p>{Ptu_c}</p>

                    <h2 class="section-title">6. Properties of the structure</h2>
                    <h3 class="section-title">6.1 Risk of fire</h3>
                    <p>The risk of fire is one of the most important criteria for determining whether an LPS (lightning protection system) must be installed. The risk of fire is classified according to the specific fire load. The fire load should be determined by a fire safety expert or defined after consultation with the proprietor of the building and his / her insurance company. A distinction is made according to the following criteria:</p>
                    <ul>
                        <li class="list-item">None</li>
                        <li class="list-item">Low (specific fire load in the building less than 400 MJ/m²)</li>
                        <li class="list-item">Ordinary (specific fire load in the building between 400 MJ/m² and 800 MJ/m²)</li>
                    </ul>
                </div>
                <footer class="footer"> <!-- Footer bölümü -->
                    <img src="images/logo.png" alt="Radsan Logo" width="80" height="35"> <!-- Footer'da yer alan logo resmi -->
                    <p>Radsan Risk Tools - {tarih}</p> <!-- Footer'da yer alan metin -->
                    <p>Page 10 of 19</p> <!-- Footer'da yer alan sayfa numarası -->
                </footer>
            </div>
        </body>
        </html>

        """
        html_content_11 = f"""
        <!DOCTYPE html>
        <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Risk Analizi</title>
            <style>
                body {{
                    font-family: Arial, sans-serif; /* Sayfadaki yazı tipini Arial olarak ayarlar, Arial mevcut değilse sans-serif kullanılır */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    min-height: 100vh; /* Sayfanın en az yüksekliğini ekran yüksekliği kadar yapar */
                    margin: 0; /* Varsayılan margin değerlerini sıfırlar */
                }}

                .container {{
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                }}

                .subsection {{
                    margin-left: 10px; /* Alt bölümün sol tarafına 10px boşluk ekler */
                    margin-bottom: 5px; /* Alt bölümün altına 5px boşluk ekler */
                }}

                .content {{
                    margin-bottom: 1px; /* İçeriğin altına 5px boşluk ekler */
                }}

                .content p {{
                    margin: 1px 0; /* Paragrafların üst ve altına 5px boşluk ekler */
                }}

                .image-section {{
                    text-align: center; /* Görsel bölümünü ortalar */
                    margin: 10px 0; /* Görsel bölümünün üst ve altına 10px boşluk ekler */
                }}

                .image-section img {{
                    max-width: 100%; /* Görselin maksimum genişliğini %100 yapar */
                    height: auto; /* Görselin yüksekliğini otomatik ayarlar */
                }}
                p {{
                    margin-bottom: 1px; /* Paragraf altındaki boşluğu azaltır */
                    line-height: 1; /* Satır yüksekliğini kısaltır (isteğe bağlı) */
                }}

                ul {{
                    margin-top: 10px; /* Liste üstündeki boşluğu azaltır */
                    padding-left: 1px; /* Liste başlığı ile liste elemanları arasındaki boşluğu ayarlar */
                }}     
                h2 {{
                    margin-top: 10px; 
                    margin-bottom: 10px;
                    /* Liste üstündeki boşluğu azaltır */
                    padding-left: 1px; /* Liste başlığı ile liste elemanları arasındaki boşluğu ayarlar */
                    
                }}     
                
                .footer {{
                    display: flex; /* Footer öğelerini yatayda hizalar */
                    justify-content: space-between; /* Footer öğeleri arasında boşluk bırakır */
                    align-items: center; /* Footer öğelerini dikeyde ortalar */
                    margin-top: 10px; /* Footer'ın üstüne 10px boşluk ekler */
                    padding: 10px 20px; /* İç boşlukları belirler */
                    background-color: #f1f1f1; /* Footer'ın arka plan rengini belirler */
                }}
                .footer img {{
                    display: block; /* Resmi blok eleman olarak gösterir, böylece margin ayarları doğru şekilde uygulanır */
                    margin: 0; /* Resmin marginlerini sıfırlar */
                }}
                .footer p {{
                    margin: 0; /* Footer içindeki paragrafların marginlerini sıfırlar */
                }}

                .top-right-image {{
                    position: absolute; /* Resmi sayfanın köşesine yerleştirir */
                    top: 0;
                    right: 0;
                    width: 80px; /* Resmin genişliğini ayarlar */
                    height: auto; /* Yüksekliği otomatik ayarlar */
                    margin: 5px; /* Resme biraz boşluk bırakır */
                }}
            </style>
        </head>
        <body>
            <div class="container"> <!-- Ana içerik kapsayıcısı -->
                <img src="images/customer.png" alt="Açıklama" class="top-right-image"> <!-- Sağ üst köşede yer alan resim -->
                <p>Risk analysis for assessing the risk for structures<br>according to IEC 62305-2:2010-12</p> <!-- Açıklama metni -->
                <div class="content">
                </div>
                <ul>
                    <br>
                    <li>High (specific fire load in the building greater than 800 MJ/m²)</li>
                    <li>Explosion: zone 2 / 22</li>
                    <li>Explosion: zone 1 / 21</li>
                    <li>Explosion: zone 0 / 20</li>
                <ul>
                <p>The risk of fire in a structure is an important factor for determining the required protection measures. The risk of fire for the structure {yapı_konum} was defined as follows:</p>
                <ul>
                    <li>{patlama_riski}</li>
                <ul>
                <h2>6.2 Measures to reduce the consequences of a fire</h2>
                <p>The following measures were selected to reduce the consequences of a fire:</p>
                <ul>
                    <li>{rp_c}</li>
                </ul>
                <h2>6.3 Special hazards in the building for persons</h2>
                <p>Due to the number of persons, the possible risk of panic for the structure {yapı_konum} was defined as follows:</p>
                <ul>
                    <li>{hz_c}</li>
                </ul>
                <h2>6.4 External spatial shielding</h2>
                <p>Spatial shielding attenuates the magnetic field within a structure caused by lightning strikes to or near the object and reduces internal surges.</p>
                <p>This can be achieved by an intermeshed equipotential bonding network in which all conductive parts of the structure and the internal systems are integrated. Consequently, the external / internal spatial shield is only a part of a shielded building structure. It must be observed that metal coverings and claddings are connected to one another and conductively to the equipotential bonding of the building. In this context, the relevant normative requirements must be observed.</p>
                <p>Covering of the structure {yapı_konum}:</p>
                <ul>
                    <li>{Pta_c}</li>
                </ul>
                <h2>7. Risk assessment</h2>
                <p>As described in 4.1, the following risks according to 7. were assessed. The blue bar shows the tolerable risk value and the green / red bar shows the risk determined.</p>
                <h3>7.1 Risk R1, Human life</h3>
                <p>The following risk was determined for persons outside and inside the structure {yapı_konum}:</p>
                <ul>
                    <li>Tolerable risk R<sub>T</sub>: 1,00E-05</li>
                    <li>Calculated risk R1: {R_1}</li>
                </ul>
            </div> <!-- .container div kapanışı eklendi(en aşağı atmak için gerekli ) --> 

            <footer class="footer"> <!-- Footer bölümü -->
                <img src="images/logo.png" alt="Radsan Logo" width="80" height="35"> <!-- Footer'da yer alan logo resmi -->
                <p>Radsan Risk Tools - {tarih}</p> <!-- Footer'da yer alan metin -->
                <p>Page 11 of 19</p> <!-- Footer'da yer alan sayfa numarası -->
            </footer>
        </body>
        </html>

        """
        html_content_12 = f"""
        <!DOCTYPE html>
        <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Risk Analizi - Devam</title>
            <style>
                body {{
                    font-family: Arial, sans-serif; /* Sayfadaki yazı tipini Arial olarak ayarlar, Arial mevcut değilse sans-serif kullanılır */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    min-height: 100vh; /* Sayfanın en az yüksekliğini ekran yüksekliği kadar yapar */
                    margin: 0; /* Varsayılan margin değerlerini sıfırlar */
                }}

                .container {{
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                }}

                .subsection {{
                    margin-left: 10px; /* Alt bölümün sol tarafına 10px boşluk ekler */
                    margin-bottom: 5px; /* Alt bölümün altına 5px boşluk ekler */
                }}

                .content {{
                    margin-bottom: 1px; /* İçeriğin altına 5px boşluk ekler */
                }}

                .content p {{
                    margin: 8px 0; /* Paragrafların üst ve altına 5px boşluk ekler */
                }}

                .image-section {{
                    text-align: center; /* Görsel bölümünü ortalar */
                    margin: 20px 0; /* Görsel bölümünün üst ve altına 10px boşluk ekler */
                }}

                .image-section img {{
                    max-width: 100%; /* Görselin maksimum genişliğini %100 yapar */
                    height: auto; /* Görselin yüksekliğini otomatik ayarlar */
                }}

                p {{
                    margin-bottom: 1px; /* Paragraf altındaki boşluğu azaltır */
                    line-height: 1; /* Satır yüksekliğini kısaltır (isteğe bağlı) */
                }}

                ul {{
                    margin-top: 10px; /* Liste üstündeki boşluğu azaltır */
                    padding-left: 1px; /* Liste başlığı ile liste elemanları arasındaki boşluğu ayarlar */
                }}

                h2 {{
                    margin-top: 10px;
                    margin-bottom: 10px;
                    /* Liste üstündeki boşluğu azaltır */
                    padding-left: 1px; /* Liste başlığı ile liste elemanları arasındaki boşluğu ayarlar */
                }}

                .footer {{
                    display: flex; /* Footer öğelerini yatayda hizalar */
                    justify-content: space-between; /* Footer öğeleri arasında boşluk bırakır */
                    align-items: center; /* Footer öğelerini dikeyde ortalar */
                    margin-top: 10px; /* Footer'ın üstüne 10px boşluk ekler */
                    padding: 10px 20px; /* İç boşlukları belirler */
                    background-color: #f1f1f1; /* Footer'ın arka plan rengini belirler */
                }}
                .footer img {{
                    display: block; /* Resmi blok eleman olarak gösterir, böylece margin ayarları doğru şekilde uygulanır */
                    margin: 0; /* Resmin marginlerini sıfırlar */
                }}
                .footer p {{
                    margin: 0; /* Footer içindeki paragrafların marginlerini sıfırlar */
                }}

                .top-right-image {{
                    position: absolute; /* Resmi sayfanın köşesine yerleştirir */
                    top: 0;
                    right: 0;
                    width: 80px; /* Resmin genişliğini ayarlar */
                    height: auto; /* Yüksekliği otomatik ayarlar */
                    margin: 5px; /* Resme biraz boşluk bırakır */
                }}
                .caption {{
                    text-align: top; /* Açıklamayı ortalar */
                    margin-top: 5px; /* Açıklamanın üstüne 5px boşluk ekler */
                    font-size: 14px; /* Yazı boyutunu belirler */
                    color: #555; /* Yazı rengini belirler */
                }}
            </style>
        </head>
        <body>
            <div class="container"> <!-- Ana içerik kapsayıcısı -->
                <img src="images/customer.png" alt="Açıklama" class="top-right-image"> <!-- Sağ üst köşede yer alan resim -->
                <p>Risk analysis for assessing the risk for structures<br>according to IEC 62305-2:2010-12</p> <!-- Açıklama metni -->
                <div class="content">
                
                <br><br>

                <p>The risk R1 consists of following risk components:</p>
                <div class="image-section">
                    <img src="images/graph_1.png" alt="Graph Image" width="430" sheight="auto">
                </div>
                
                <p>To reduce the risk, it is necessary to take measures as described in 8.</p>
                <br><br>
                <h2>7.2 Risk R2, Service to the public</h2>
                <p>The risk R2, failure of services to the public, was determined for the structure <strong>{yapı_konum}</strong> as follows:</p>
                <ul>
                    <li>Tolerable risk R<sub>T</sub>: 1,00E-03</li>
                    <li>Calculated risk R2: {R_2}</li>
                </ul>
                
                


                <p>The risk R2 consists of following risk components:</p>
                <div class="image-section">
                    <img src="images/graph_2.png" alt="Graph Image" width="430" sheight="auto">
                    <div class="caption"></div>
                </div>
                
                <p>To reduce the risk, it is necessary to take measures as described in 8.</p>
                </div> <!-- .content div kapanışı ekledi -->
                </ul>
            </div> <!-- .container div kapanışı -->

            <footer class="footer"> <!-- Footer bölümü -->
                <img src="images/logo.png" alt="Radsan Logo" width="80" height="35"> <!-- Footer'da yer alan logo resmi -->
                <p>Radsan Risk Tools - {tarih}</p> <!-- Footer'da yer alan metin -->
                <p>Page 12 of 19</p> <!-- Footer'da yer alan sayfa numarası -->
            </footer>

        </body>
        </html>

        """
        html_content_13 = f"""
        <!DOCTYPE html>
        <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Risk Analizi - Devam</title>
            <style>
                body {{
                    font-family: Arial, sans-serif; /* Sayfadaki yazı tipini Arial olarak ayarlar, Arial mevcut değilse sans-serif kullanılır */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    min-height: 100vh; /* Sayfanın en az yüksekliğini ekran yüksekliği kadar yapar */
                    margin: 0; /* Varsayılan margin değerlerini sıfırlar */
                }}

                .container {{
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                }}

                .subsection {{
                    margin-left: 10px; /* Alt bölümün sol tarafına 10px boşluk ekler */
                    margin-bottom: 5px; /* Alt bölümün altına 5px boşluk ekler */
                }}

                .content {{
                    margin-bottom: 1px; /* İçeriğin altına 5px boşluk ekler */
                }}

                .content p {{
                    margin: 8px 0; /* Paragrafların üst ve altına 5px boşluk ekler */
                }}

                .image-section {{
                    text-align: center; /* Görsel bölümünü ortalar */
                    margin: 20px 0; /* Görsel bölümünün üst ve altına 10px boşluk ekler */
                }}

                .image-section img {{
                    max-width: 100%; /* Görselin maksimum genişliğini %100 yapar */
                    height: auto; /* Görselin yüksekliğini otomatik ayarlar */
                }}

                p {{
                    margin-bottom: 1px; /* Paragraf altındaki boşluğu azaltır */
                    line-height: 1; /* Satır yüksekliğini kısaltır (isteğe bağlı) */
                }}

                ul {{
                    margin-top: 10px; /* Liste üstündeki boşluğu azaltır */
                    padding-left: 1px; /* Liste başlığı ile liste elemanları arasındaki boşluğu ayarlar */
                }}

                h2 {{
                    margin-top: 10px;
                    margin-bottom: 10px;
                    /* Liste üstündeki boşluğu azaltır */
                    padding-left: 1px; /* Liste başlığı ile liste elemanları arasındaki boşluğu ayarlar */
                }}

                .footer {{
                    display: flex; /* Footer öğelerini yatayda hizalar */
                    justify-content: space-between; /* Footer öğeleri arasında boşluk bırakır */
                    align-items: center; /* Footer öğelerini dikeyde ortalar */
                    margin-top: 10px; /* Footer'ın üstüne 10px boşluk ekler */
                    padding: 10px 20px; /* İç boşlukları belirler */
                    background-color: #f1f1f1; /* Footer'ın arka plan rengini belirler */
                }}
                .footer img {{
                    display: block; /* Resmi blok eleman olarak gösterir, böylece margin ayarları doğru şekilde uygulanır */
                    margin: 0; /* Resmin marginlerini sıfırlar */
                }}
                .footer p {{
                    margin: 0; /* Footer içindeki paragrafların marginlerini sıfırlar */
                }}

                .top-right-image {{
                    position: absolute; /* Resmi sayfanın köşesine yerleştirir */
                    top: 0;
                    right: 0;
                    width: 80px; /* Resmin genişliğini ayarlar */
                    height: auto; /* Yüksekliği otomatik ayarlar */
                    margin: 5px; /* Resme biraz boşluk bırakır */
                }}
                .caption {{
                    text-align: top; /* Açıklamayı ortalar */
                    margin-top: 5px; /* Açıklamanın üstüne 5px boşluk ekler */
                    font-size: 14px; /* Yazı boyutunu belirler */
                    color: #555; /* Yazı rengini belirler */
                }}
            </style>
        </head>
        <body>
            <div class="container"> <!-- Ana içerik kapsayıcısı -->
                <img src="images/customer.png" alt="Açıklama" class="top-right-image"> <!-- Sağ üst köşede yer alan resim -->
                <p>Risk analysis for assessing the risk for structures<br>according to IEC 62305-2:2010-12</p> <!-- Açıklama metni -->
                
                <h2>7.3 Risk R3, Cultural heritage</h2>
                <p>The risk R3, loss of cultural heritage, was determined for the structure <strong>{yapı_konum}</strong> as follows:</p>
                <ul>
                    <li>Tolerable risk R<sub>T</sub>: 1,00E-04</li>
                    <li>Calculated risk R3: {R_3}</li>

                </ul>


                <p>The risk R consists of following risk components:</p>
                <div class="image-section">
                    <img src="images/graph_3.png" alt="Graph Image" width="430" sheight="auto">
                </div>
                
                <p>To reduce the risk, it is necessary to take measures as described in 8.</p>

                <h2>7.3 Risk R4, Economic</h2>
                <p>The risk R3, loss of cultural heritage, was determined for the structure <strong>{yapı_konum}</strong> as follows:</p>
                <ul>
                    <li>Tolerable risk R<sub>T</sub>: 1,00E-04</li>
                    <li>Calculated risk R4: {R_4}</li>
                </ul>


                <p>The risk R4 consists of following risk components:</p>
                <div class="image-section">
                    <img src="images/graph_4.png" alt="Graph Image" width="430" sheight="auto">
                </div>
                
                <p>To reduce the risk, it is necessary to take measures as described in 8.</p>

            </div> 
                <footer class="footer"> <!-- Footer bölümü -->
                    <img src="images/logo.png" alt="Radsan Logo" width="80" height="35"> <!-- Footer'da yer alan logo resmi -->
                    <p>Radsan Risk Tools - {tarih}</p> <!-- Footer'da yer alan metin -->
                    <p>Page 13 of 19</p> <!-- Footer'da yer alan sayfa numarası -->
                </footer>

        </body>
        </html>

        """
        html_content_14 = f"""
        <!DOCTYPE html>
        <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Lightning Protection Risk Management</title>
            <style>
                body {{
                    font-family: Arial, sans-serif; /* Sayfadaki yazı tipini Arial olarak ayarlar, Arial mevcut değilse sans-serif kullanılır */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    min-height: 100vh; /* Sayfanın en az yüksekliğini ekran yüksekliği kadar yapar */
                    margin: 0; /* Varsayılan margin değerlerini sıfırlar */
                }}

                .container {{
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    padding: 20px; /* İçeriğin etrafına 20px boşluk ekler */
                }}

                .subsection {{
                    margin-left: 10px; /* Alt bölümün sol tarafına 10px boşluk ekler */
                    margin-bottom: 5px; /* Alt bölümün altına 5px boşluk ekler */
                }}

                .content {{
                    margin-bottom: 20px; /* İçeriğin altına 20px boşluk ekler */
                }}

                .content p {{
                    margin: 8px 0; /* Paragrafların üst ve altına 8px boşluk ekler */
                }}

                p {{
                    margin-bottom: 10px; /* Paragraf altındaki boşluğu ayarlar */
                    line-height: 1.5; /* Satır yüksekliğini ayarlar */
                }}


                .footer {{
                    display: flex; /* Footer öğelerini yatayda hizalar */
                    justify-content: space-between; /* Footer öğeleri arasında boşluk bırakır */
                    align-items: center; /* Footer öğelerini dikeyde ortalar */
                    margin-top: 10px; /* Footer'ın üstüne 10px boşluk ekler */
                    padding: 10px 20px; /* İç boşlukları belirler */
                    background-color: #f1f1f1; /* Footer'ın arka plan rengini belirler */
                }}
                .footer img {{
                    display: block; /* Resmi blok eleman olarak gösterir, böylece margin ayarları doğru şekilde uygulanır */
                    margin: 0; /* Resmin marginlerini sıfırlar */
                }}
                .footer p {{
                    margin: 0; /* Footer içindeki paragrafların marginlerini sıfırlar */
                }}

                .top-right-image {{
                    position: absolute; /* Resmi sayfanın köşesine yerleştirir */
                    top: 0;
                    right: 0;
                    width: 80px; /* Resmin genişliğini ayarlar */
                    height: auto; /* Yüksekliği otomatik ayarlar */
                    margin: 5px; /* Resme biraz boşluk bırakır */
                }}

                .caption {{
                    text-align: center; /* Açıklamayı ortalar */
                    margin-top: 5px; /* Açıklamanın üstüne 5px boşluk ekler */
                    font-size: 14px; /* Yazı boyutunu belirler */
                    color: #555; /* Yazı rengini belirler */
                }}
            </style>
        </head>
        <body>
            <div class="container"> <!-- Ana içerik kapsayıcısı -->
                <img src="images/customer.png" alt="Açıklama" class="top-right-image"> <!-- Sağ üst köşede yer alan resim -->
                <p>Risk analysis for assessing the risk for structures<br>according to IEC 62305-2:2010-12</p> <!-- Açıklama metni -->
                <div class="content">
                    <p><strong>pB:</strong> Lightning protection system (LPS) Class of LPS IV : {P_B}</p>
                    <p><strong>pEB:</strong> Lightning equipotential bonding Equipotential bonding for LPL III or IV : {P_EB}</p>
                    <p><strong>KS1-2:</strong> External spatial shielding (all zones) continuous metal shield with a thickness <br> not lower than 0.1 mm : {KS1}</p>

                    <p><strong>Type of internal wiring</strong></p>
                    <p><strong>KS3:</strong> Shielded cables and cables running in metal conduits : {KS3}</p>
                </div>
            </div> 
            <footer class="footer"> <!-- Footer bölümü -->
                <img src="images/logo.png" alt="Radsan Logo" width="80" height="35"> <!-- Footer'da yer alan logo resmi -->
                <p>Radsan Risk Tools - {tarih}</p> <!-- Footer'da yer alan metin -->
                <p>Page 14 of 19</p> <!-- Footer'da yer alan sayfa numarası -->
            </footer>
        </body>
        </html>

        """

        html_content_15 = f"""
        <!DOCTYPE html>
        <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Lightning Protection Risk Management</title>
            <style>
                body {{
                    font-family: Arial, sans-serif; /* Sayfadaki yazı tipini Arial olarak ayarlar, Arial mevcut değilse sans-serif kullanılır */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    min-height: 100vh; /* Sayfanın en az yüksekliğini ekran yüksekliği kadar yapar */
                    margin: 0; /* Varsayılan margin değerlerini sıfırlar */
                }}

                .container {{
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    padding: 20px; /* İçeriğin etrafına 20px boşluk ekler */
                }}

                .subsection {{
                    margin-left: 10px; /* Alt bölümün sol tarafına 10px boşluk ekler */
                    margin-bottom: 5px; /* Alt bölümün altına 5px boşluk ekler */
                }}

                .content {{
                    margin-bottom: 20px; /* İçeriğin altına 20px boşluk ekler */
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */
                }}

                .content p {{
                    margin: 8px 0; /* Paragrafların üst ve altına 8px boşluk ekler */
                }}

                p {{
                    margin-bottom: 10px; /* Paragraf altındaki boşluğu ayarlar */
                    line-height: 1.5; /* Satır yüksekliğini ayarlar */
                }}

                .footer {{
                    display: flex; /* Footer öğelerini yatayda hizalar */
                    justify-content: space-between; /* Footer öğeleri arasında boşluk bırakır */
                    align-items: center; /* Footer öğelerini dikeyde ortalar */
                    padding: 10px 20px; /* İç boşlukları belirler */
                    background-color: #f1f1f1; /* Footer'ın arka plan rengini belirler */
                }}

                .footer img {{
                    display: block; /* Resmi blok eleman olarak gösterir, böylece margin ayarları doğru şekilde uygulanır */
                    margin: 0; /* Resmin marginlerini sıfırlar */
                }}

                .footer p {{
                    margin: 0; /* Footer içindeki paragrafların marginlerini sıfırlar */
                }}

                .top-right-image {{
                    position: absolute; /* Resmi sayfanın köşesine yerleştirir */
                    top: 0;
                    right: 0;
                    width: 80px; /* Resmin genişliğini ayarlar */
                    height: auto; /* Yüksekliği otomatik ayarlar */
                    margin: 5px; /* Resme biraz boşluk bırakır */
                }}

                .caption {{
                    text-align: center; /* Açıklamayı ortalar */
                    margin-top: 5px; /* Açıklamanın üstüne 5px boşluk ekler */
                    font-size: 14px; /* Yazı boyutunu belirler */
                    color: #555; /* Yazı rengini belirler */
                }}
            </style>
        </head>
        <body>
            <div class="container"> <!-- Ana içerik kapsayıcısı -->
                <img src="images/customer.png" alt="Açıklama" class="top-right-image"> <!-- Sağ üst köşede yer alan resim -->
                <p>Risk analysis for assessing the risk for structures<br>according to IEC 62305-2:2010-12</p> <!-- Açıklama metni -->
                <div class="content">
                    <h3>9. Legal obligation</h3>
                    <p>The risk analysis performed refers to the information provided by the operator and/or proprietor of the building or expert which has been assumed, assessed or defined on site. Please note that this information must be verified after assessment.</p>
                    <p>The procedure of the DEHNsupport software for calculating the risks is based on the IEC 62305-2:2010-12 standard.</p>
                    <p>Please note that all assumptions, documents, illustrations, drawings, dimensions, parameters and results are not legally binding for the person performing the risk analysis.</p>
                    <div style="text-align: center; margin-top: 20px;">
                        <p>ANKARA, 25.04.2020</p>
                        <div style="display: flex; justify-content: space-between; margin-top: 40px;">
                            <div>
                                <br><br><br>
                                <p>_______________________________</p>
                                <p>Place, date</p>
                            </div>
                            <div>
                                <br><br><br>
                                <p>_______________________________</p>
                                <p>Stamp, signature</p>
                            </div>
                        </div>
                    </div>
                </div>
                <footer class="footer"> <!-- Footer bölümü -->
                    <img src="images/logo.png" alt="Radsan Logo" width="80" height="35"> <!-- Footer'da yer alan logo resmi -->
                    <p>Radsan Risk Tools - {tarih}</p> <!-- Footer'da yer alan metin -->
                    <p>Page 15 of 19</p> <!-- Footer'da yer alan sayfa numarası -->
                </footer>
            </div>
        </body>
        </html>

        """
        html_content_16 = f"""
        <!DOCTYPE html>
        <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Lightning Protection Risk Management</title>
            <style>
                body {{
                    font-family: Arial, sans-serif; /* Sayfadaki yazı tipini Arial olarak ayarlar, Arial mevcut değilse sans-serif kullanılır */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    min-height: 100vh; /* Sayfanın en az yüksekliğini ekran yüksekliği kadar yapar */
                    margin: 0; /* Varsayılan margin değerlerini sıfırlar */
                }}

                .container {{
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    padding: 20px; /* İçeriğin etrafına 20px boşluk ekler */
                }}

                .subsection {{
                    margin-left: 10px; /* Alt bölümün sol tarafına 10px boşluk ekler */
                    margin-bottom: 5px; /* Alt bölümün altına 5px boşluk ekler */
                }}

                .content {{
                    margin-bottom: 20px; /* İçeriğin altına 20px boşluk ekler */
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */
                }}

                .content p {{
                    margin: 8px 0; /* Paragrafların üst ve altına 8px boşluk ekler */
                }}

                p {{
                    margin-bottom: 10px; /* Paragraf altındaki boşluğu ayarlar */
                    line-height: 1.5; /* Satır yüksekliğini ayarlar */
                }}

                .footer {{
                    display: flex; /* Footer öğelerini yatayda hizalar */
                    justify-content: space-between; /* Footer öğeleri arasında boşluk bırakır */
                    align-items: center; /* Footer öğelerini dikeyde ortalar */
                    padding: 10px 20px; /* İç boşlukları belirler */
                    background-color: #f1f1f1; /* Footer'ın arka plan rengini belirler */
                }}

                .footer img {{
                    display: block; /* Resmi blok eleman olarak gösterir, böylece margin ayarları doğru şekilde uygulanır */
                    margin: 0; /* Resmin marginlerini sıfırlar */
                }}

                .footer p {{
                    margin: 0; /* Footer içindeki paragrafların marginlerini sıfırlar */
                }}

                .top-right-image {{
                    position: absolute; /* Resmi sayfanın köşesine yerleştirir */
                    top: 0;
                    right: 0;
                    width: 80px; /* Resmin genişliğini ayarlar */
                    height: auto; /* Yüksekliği otomatik ayarlar */
                    margin: 5px; /* Resme biraz boşluk bırakır */
                }}

                .caption {{
                    text-align: center; /* Açıklamayı ortalar */
                    margin-top: 5px; /* Açıklamanın üstüne 5px boşluk ekler */
                    font-size: 14px; /* Yazı boyutunu belirler */
                    color: #555; /* Yazı rengini belirler */
                }}
            </style>
        </head>
        <body>
            <div class="container"> <!-- Ana içerik kapsayıcısı -->
                <img src="images/customer.png" alt="Açıklama" class="top-right-image"> <!-- Sağ üst köşede yer alan resim -->
                <p>Risk analysis for assessing the risk for structures<br>according to IEC 62305-2:2010-12</p> <!-- Açıklama metni -->
                <div class="content">
                    <h3>10. General information</h3>
                    <h4>10.1 Components of the external lightning protection system</h4>
                    <p>Lightning protection components used for the construction of the external lightning protection system must comply with the mechanical and electrical requirements defined in the IEC 62561-x standard series. This standard series is for example divided into following parts:</p>
                    <ul>
                        <li>IEC 62561-1:2012 Requirements for connection components</li>
                        <li>IEC 62561-2:2012 Requirements for conductors and earth electrodes</li>
                        <li>IEC 62561-3:2012 Requirements for isolating spark gaps</li>
                        <li>IEC 62561-4:2010 Requirements for conductor fasteners</li>
                        <li>IEC 62561-5:2011 Requirements for electrode inspection housings and earth electrode seals</li>
                    </ul>
                    <h4>10.1.1 IEC 62561-1:2012 Requirements for connection components</h4>
                    <p>The requirements for connection components such as clamps are defined in IEC 62561-1. For the installer of lightning protection systems this means that the connection components are to be selected for the load (H or N) to be expected at the place of installation. Therefore, a clamp for load H (100 kA) is to be used e.g. for an air-termination rod (100% lightning current) and a clamp for load N (50 kA) e.g. for a mesh or an earth entry (lightning current already distributed). The suitability for these applications must be proven by the manufacturer.</p>
                    <h4>10.1.2 IEC 62561-2:2012 Requirements for conductors and earth electrodes</h4>
                    <p>The IEC 62561-2 specifies concrete requirements for conductors, such as air-termination and down conductors as well as earth electrodes. These are defined as follows:</p>
                    <ul>
                        <li>Mechanical properties (minimum tensile strength and elongation),</li>
                        <li>Electrical properties (maximum resistivity) and</li>
                        <li>Corrosion protection properties (artificial aging).</li>
                    </ul>
                    <p>The IEC 62561-2 standard also specifies the requirements for earth electrodes and earth rods. In this context, the material, geometry, minimum dimensions as well as the mechanical and electrical properties are important. These normative requirements are relevant product features, which must be documented in the manufacturers' documents and product datasheets.</p>
                </div>
                <footer class="footer"> <!-- Footer bölümü -->
                    <img src="images/logo.png" alt="Radsan Logo" width="80" height="35"> <!-- Footer'da yer alan logo resmi -->
                    <p>Radsan Risk Tools - {tarih}</p> <!-- Footer'da yer alan metin -->
                    <p>Page 16 of 19</p> <!-- Footer'da yer alan sayfa numarası -->
                </footer>
            </div>
        </body>
        </html>

        """
        html_content_17 = f"""
        <!DOCTYPE html>
        <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Lightning Protection Risk Management</title>
            <style>
                body {{
                    font-family: Arial, sans-serif; /* Sayfadaki yazı tipini Arial olarak ayarlar, Arial mevcut değilse sans-serif kullanılır */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    min-height: 100vh; /* Sayfanın en az yüksekliğini ekran yüksekliği kadar yapar */
                    margin: 0; /* Varsayılan margin değerlerini sıfırlar */
                }}

                .container {{
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    padding: 20px; /* İçeriğin etrafına 20px boşluk ekler */
                }}

                .subsection {{
                    margin-left: 10px; /* Alt bölümün sol tarafına 10px boşluk ekler */
                    margin-bottom: 5px; /* Alt bölümün altına 5px boşluk ekler */
                }}

                .content {{
                    margin-bottom: 20px; /* İçeriğin altına 20px boşluk ekler */
                }}

                .content p {{
                    margin: 8px 0; /* Paragrafların üst ve altına 8px boşluk ekler */
                }}

                p {{
                    margin-bottom: 10px; /* Paragraf altındaki boşluğu ayarlar */
                    line-height: 1.5; /* Satır yüksekliğini ayarlar */
                }}

                .footer {{
                    display: flex; /* Footer öğelerini yatayda hizalar */
                    justify-content: space-between; /* Footer öğeleri arasında boşluk bırakır */
                    align-items: center; /* Footer öğelerini dikeyde ortalar */
                    margin-top: 10px; /* Footer'ın üstüne 10px boşluk ekler */
                    padding: 10px 20px; /* İç boşlukları belirler */
                    background-color: #f1f1f1; /* Footer'ın arka plan rengini belirler */
                }}
                .footer img {{
                    display: block; /* Resmi blok eleman olarak gösterir, böylece margin ayarları doğru şekilde uygulanır */
                    margin: 0; /* Resmin marginlerini sıfırlar */
                }}
                .footer p {{
                    margin: 0; /* Footer içindeki paragrafların marginlerini sıfırlar */
                }}

                .top-right-image {{
                    position: absolute; /* Resmi sayfanın köşesine yerleştirir */
                    top: 0;
                    right: 0;
                    width: 80px; /* Resmin genişliğini ayarlar */
                    height: auto; /* Yüksekliği otomatik ayarlar */
                    margin: 5px; /* Resme biraz boşluk bırakır */
                }}

                .caption {{
                    text-align: center; /* Açıklamayı ortalar */
                    margin-top: 5px; /* Açıklamanın üstüne 5px boşluk ekler */
                    font-size: 14px; /* Yazı boyutunu belirler */
                    color: #555; /* Yazı rengini belirler */
                }}
            </style>
        </head>
        <body>
            <div class="container"> <!-- Ana içerik kapsayıcısı -->
                <img src="images/customer.png" alt="Açıklama" class="top-right-image"> <!-- Sağ üst köşede yer alan resim -->
                <p>Risk analysis for assessing the risk for structures<br>according to IEC 62305-2:2010-12</p> <!-- Açıklama metni -->
                <div class="content">
                    <h4>10.1.3 IEC 62561-3:2012 Requirements for isolating spark gaps</h4>
                    <p>Isolating spark gaps can be used to galvanically isolate an earth-termination system. IEC 62561-3 specifies that isolating spark gaps must be dimensioned in such a way that the components, if installed according to the manufacturer's instructions, are reliable, durable and safe for persons and nearby installations.</p>
                    <h4>10.1.4 IEC 62561-4:2010 Requirements for conductor fasteners</h4>
                    <p>The IEC 62561-4 standard specifies the requirements and tests for metal and non-metal conductor fasteners used with air-termination and down conductors.</p>
                    <h4>10.1.5 IEC 62561-5:2011 Requirements for electrode inspection housings and earth electrode seals</h4>
                    <p>All earth electrode inspection housings and earth electrode seals must be designed in such a way that they are reliable and safe for persons and the environment when used as intended. IEC 62561-5 specifies the requirements and tests for earth electrode inspection housings (e.g. pressure load) and for earth electrode seals (e.g. leak test).</p>
                    <h3>11. Definition</h3>
                </div>
            </div>
            <footer class="footer"> <!-- Footer bölümü -->
                <img src="images/logo.png" alt="Radsan Logo" width="80" height="35"> <!-- Footer'da yer alan logo resmi -->
                <p>Radsan Risk Tools - {tarih}</p> <!-- Footer'da yer alan metin -->
                <p>Page 17 of 19</p> <!-- Footer'da yer alan sayfa numarası -->
            </footer>
        </body>
        </html>

        """
        html_content_18 = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Risk Analysis Page 18</title>
            <style>
                body {{
                    font-family: Arial, sans-serif; /* Sayfadaki yazı tipini Arial olarak ayarlar, Arial mevcut değilse sans-serif kullanılır */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    min-height: 100vh; /* Sayfanın en az yüksekliğini ekran yüksekliği kadar yapar */
                    margin: 0; /* Varsayılan margin değerlerini sıfırlar */
                }}

                .container {{
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    padding: 20px; /* İçeriğin etrafına 20px boşluk ekler */
                }}

                .subsection {{
                    margin-left: 10px; /* Alt bölümün sol tarafına 10px boşluk ekler */
                    margin-bottom: 5px; /* Alt bölümün altına 5px boşluk ekler */
                }}

                .content {{
                    margin-bottom: 20px; /* İçeriğin altına 20px boşluk ekler */
                }}

                .content p {{
                    margin: 8px 0; /* Paragrafların üst ve altına 8px boşluk ekler */
                }}

                p {{
                    margin-bottom: 1px;
                    margin-top: 1px; /* Paragraf altındaki boşluğu ayarlar */
                }}
                h2 {{
                    margin-bottom: 1px;
                    margin-top: 1px; /* Paragraf altındaki boşluğu ayarlar */
                    font-size: 18px; /* Font boyutunu ayarlar */
                }}


                .footer {{
                    display: flex; /* Footer öğelerini yatayda hizalar */
                    justify-content: space-between; /* Footer öğeleri arasında boşluk bırakır */
                    align-items: center; /* Footer öğelerini dikeyde ortalar */
                    margin-top: 10px; /* Footer'ın üstüne 10px boşluk ekler */
                    padding: 10px 20px; /* İç boşlukları belirler */
                    background-color: #f1f1f1; /* Footer'ın arka plan rengini belirler */
                }}
                .footer img {{
                    display: block; /* Resmi blok eleman olarak gösterir, böylece margin ayarları doğru şekilde uygulanır */
                    margin: 0; /* Resmin marginlerini sıfırlar */
                }}
                .footer p {{
                    margin: 0; /* Footer içindeki paragrafların marginlerini sıfırlar */
                }}

                .top-right-image {{
                    position: absolute; /* Resmi sayfanın köşesine yerleştirir */
                    top: 0;
                    right: 0;
                    width: 80px; /* Resmin genişliğini ayarlar */
                    height: auto; /* Yüksekliği otomatik ayarlar */
                    margin: 5px; /* Resme biraz boşluk bırakır */
                }}

                .caption {{
                    text-align: center; /* Açıklamayı ortalar */
                    margin-top: 5px; /* Açıklamanın üstüne 5px boşluk ekler */
                    font-size: 14px; /* Yazı boyutunu belirler */
                    color: #555; /* Yazı rengini belirler */
                }}
            </style>
        </head>
        <body>
            <div class="container"> <!-- Ana içerik kapsayıcısı -->
                <img src="images/customer.png" alt="Açıklama" class="top-right-image"> <!-- Sağ üst köşede yer alan resim -->
                <p>Risk analysis for assessing the risk for structures<br>according to IEC 62305-2:2010-12</p> <!-- Açıklama metni -->
                <div class="content"></div>
            <h2>Coordinated SPD system</h2>
            <p>SPDs properly selected, coordinated and installed to form a system intended to reduce failures of electrical and electronic systems.</p>
            
            <h2>Isolating interfaces</h2>
            <p>Devices which are capable of reducing conducted surges on lines entering the LPZ. These include isolation transformers with earthed screen between windings, metal-free fibre optic cables and opto-isolators. Insulation withstand characteristics of these devices are suitable for this application intrinsically or via SPD.</p>
            
            <h2>LEMP (lightning electromagnetic impulse)</h2>
            <p>All electromagnetic effects of lightning current via resistive, inductive and capacitive coupling, which create surges and electromagnetic fields.</p>
            
            <h2>LP (lightning protection)</h2>
            <p>Complete system for protection of structures against lightning, including their internal systems and contents, as well as persons, in general consisting of an LPS and SPM.</p>
            
            <h2>LPL (lightning protection level)</h2>
            <p>Number related to a set of lightning current parameters values relevant to the probability that the associated maximum and minimum design values will not be exceeded in naturally occurring lightning.</p>
            
            <h2>LPS (lightning protection system)</h2>
            <p>Complete system used to reduce physical damage due to lightning flashes to a structure.</p>
            
            <h2>EB (lightning equipotential bonding)</h2>
            <p>Bonding to LPS of separated metallic parts, by direct conductive connections or via surge protective devices, to reduce potential differences caused by lightning current.</p>
            
            <h2>SPD (surge protection device)</h2>
            <p>Device intended to limit transient overvoltages and divert surge currents; contains at least one non-linear component.</p>
            
            <h2>Node</h2>
            <p>Point on a line from which onward surge propagation can be assumed to be neglected. Examples of nodes are a point on a power line branch distribution at an HV / LV transformer or on a power substation, a telecommunication exchange or an equipment (e.g. multiplexer or xDSL equipment) on a telecommunication line.</p>
            
            <h2>Physical damage</h2>
            <p>Damage to a structure (or to its contents) due to mechanical, thermal, chemical or explosive effects of lightning.</p>
            
            <h2>Injury to living beings</h2>
            <p>Permanent injuries, including loss of life, to people or to animals by electric shock due to touch and step voltages caused by lightning.</p>
            
            <h2>Risk R</h2>
            <p>Value of probable average annual loss (humans and goods) due to lightning, relative to the total value (humans and goods) of the structure to be protected.</p>
            
            <h2>Zone of a structure ZS</h2>
        </div>
        <footer class="footer"> <!-- Footer bölümü -->
            <img src="images/logo.png" alt="Radsan Logo" width="80" height="35"> <!-- Footer'da yer alan logo resmi -->
            <p>Radsan Risk Tools - {tarih}</p> <!-- Footer'da yer alan metin -->
            <p>Page 18 of 19</p> <!-- Footer'da yer alan sayfa numarası -->
        </footer>
        </body>
        </html>

        """
        html_content_19 = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Risk Analysis Page 19</title>
            <style>
                body {{
                    font-family: Arial, sans-serif; /* Sayfadaki yazı tipini Arial olarak ayarlar, Arial mevcut değilse sans-serif kullanılır */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    min-height: 100vh; /* Sayfanın en az yüksekliğini ekran yüksekliği kadar yapar */
                    margin: 0; /* Varsayılan margin değerlerini sıfırlar */
                }}

                .container {{
                    flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar */
                    display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
                    flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
                    padding: 20px; /* İçeriğin etrafına 20px boşluk ekler */
                }}

                .subsection {{
                    margin-left: 10px; /* Alt bölümün sol tarafına 10px boşluk ekler */
                    margin-bottom: 5px; /* Alt bölümün altına 5px boşluk ekler */
                }}

                .content {{
                    margin-bottom: 20px; /* İçeriğin altına 20px boşluk ekler */
                }}

                .content p {{
                    margin: 8px 0; /* Paragrafların üst ve altına 8px boşluk ekler */
                }}

                p {{
                    margin-bottom: 1px;
                    margin-top: 1px; /* Paragraf altındaki boşluğu ayarlar */
                }}
                h2 {{
                    margin-bottom: 1px;
                    margin-top: 1px; /* Paragraf altındaki boşluğu ayarlar */
                    font-size: 18px; /* Font boyutunu ayarlar */
                }}


                .footer {{
                    display: flex; /* Footer öğelerini yatayda hizalar */
                    justify-content: space-between; /* Footer öğeleri arasında boşluk bırakır */
                    align-items: center; /* Footer öğelerini dikeyde ortalar */
                    margin-top: 10px; /* Footer'ın üstüne 10px boşluk ekler */
                    padding: 10px 20px; /* İç boşlukları belirler */
                    background-color: #f1f1f1; /* Footer'ın arka plan rengini belirler */
                }}
                .footer img {{
                    display: block; /* Resmi blok eleman olarak gösterir, böylece margin ayarları doğru şekilde uygulanır */
                    margin: 0; /* Resmin marginlerini sıfırlar */
                }}
                .footer p {{
                    margin: 0; /* Footer içindeki paragrafların marginlerini sıfırlar */
                }}

                .top-right-image {{
                    position: absolute; /* Resmi sayfanın köşesine yerleştirir */
                    top: 0;
                    right: 0;
                    width: 80px; /* Resmin genişliğini ayarlar */
                    height: auto; /* Yüksekliği otomatik ayarlar */
                    margin: 5px; /* Resme biraz boşluk bırakır */
                }}

                .caption {{
                    text-align: center; /* Açıklamayı ortalar */
                    margin-top: 5px; /* Açıklamanın üstüne 5px boşluk ekler */
                    font-size: 14px; /* Yazı boyutunu belirler */
                    color: #555; /* Yazı rengini belirler */
                }}
            </style>
        </head>
        <body>
            <div class="container"> <!-- Ana içerik kapsayıcısı -->
                <img src="images/customer.png" alt="Açıklama" class="top-right-image"> <!-- Sağ üst köşede yer alan resim -->
                <p>Risk analysis for assessing the risk for structures<br>according to IEC 62305-2:2010-12</p> <!-- Açıklama metni -->
                <div class="content"></div>

            <p>Part of a structure with homogeneous characteristics where only one set of parameters is involved in assessment of a risk component.</p>

            <h2>LPZ (lightning protection zone)</h2>
            <p>Zone where the lightning electromagnetic environment is sdefined. The zone boundaries of an LPZ are not necessarily physical boundaries (e.g. walls, floor and ceiling).</p>

            <h2>Magnetic shield</h2>
            <p>Closed, metallic, grid-like or continuous screen enveloping the structure to be protected, or part of it, used to reduce failures of electrical and electronic systems.</p>

            <h2>Lightning protective cable</h2>
            <p>Special cable with increased dielectric strength and whose metallic sheath is in continuous contact with the soil either directly or by use of conducting plastic covering.</p>

            <h2>Lightning protective cable duct</h2>
            <p>Cable duct of low resistivity in contact with the soil (concrete with interconnected structural steel reinforcements or metallic duct).</p>

            </div>
            <footer class="footer"> <!-- Footer bölümü -->
                <img src="images/logo.png" alt="Radsan Logo" width="80" height="35"> <!-- Footer'da yer alan logo resmi -->
                <p>Radsan Risk Tools - {tarih}</p> <!-- Footer'da yer alan metin -->
                <p>Page 19 of 19</p> <!-- Footer'da yer alan sayfa numarası -->
            </footer>
        </body>
        </html>

        """

        html_content_birleşik = f"""


        </head>
        <body>
            
            </div>
                {html_content_1}{html_content_2}{html_content_3}{html_content_4}{html_content_5}{html_content_6}{html_content_7}{html_content_8}{html_content_9}{html_content_10}{html_content_11}{html_content_12}{html_content_13}{html_content_14}{html_content_15}{html_content_16}{html_content_17}{html_content_18}{html_content_19}

            </div>

        </body>
        </html>

        """

        import os

        # Kod dizini
        kod_dizin = os.path.dirname(os.path.abspath(__file__))

        # Klasör adı
        klasör_adı = "output_pdf_1"
        klasör_yolu = os.path.join(kod_dizin, klasör_adı)

        # Klasörü oluştur (eğer mevcut değilse)
        if not os.path.exists(klasör_yolu):
            os.makedirs(klasör_yolu)
            print(f"{klasör_yolu} klasörü oluşturuldu.")

        # HTML içerikleri ve dosya adları
        html_content_list = [html_content_1, html_content_2, html_content_3, html_content_4, html_content_5,html_content_6, html_content_7, html_content_8, html_content_9, html_content_10,html_content_11, html_content_12, html_content_13, html_content_14, html_content_15,html_content_16, html_content_17, html_content_18, html_content_19]
        rapor_numaraları = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,]

        # HTML dosyalarını oluştur
        for numara, html_content in zip(rapor_numaraları, html_content_list):
            dosya_adı = f"{müşteri.lower().replace(' ', '_')}_risk_analiz_raporu_{numara}.html"
            tam_yol = os.path.join(klasör_yolu, dosya_adı)

            try:
                with open(tam_yol, "w", encoding="utf-8") as file:
                    file.write(html_content)
                    print(f"{tam_yol} dosyası başarıyla oluşturuldu.")
            except Exception as e:
                print(f"Dosya oluşturulurken bir hata oluştu: {e}")

        dosya_adı_1 = f"{müşteri.lower().replace(' ', '_')}_risk_analiz_raporubirrr.html"
        tam_yol = os.path.join(klasör_yolu, dosya_adı_1)

        try:
            with open(tam_yol, "w", encoding="utf-8") as file:
                file.write(html_content_birleşik)
                print(f"{tam_yol} dosyası başarıyla oluşturuldu.")
        except Exception as e:
            print(f"Dosya oluşturulurken bir hata oluştu: {e}")



x = LightningRiskWriter()
x.rapor_yaz()