import os
from datetime import datetime
# Kullanıcıdan isim al


yazar = input("Risk assessment by ? ")
müşteri = input("Customer / principal:")
açıklama = input("açıklama gir ")
proje_no = input("proje no nedir: ")
tarih = datetime.now()

# HTML içeriği
html_content_1 = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lightning Protection Risk Management</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            margin: 0;
        }}
        .container {{
            width: 80%;
            margin: 0 auto;
            padding: 20px;
            flex: 1;
        }}
        .header {{
            text-align: center;
            margin-bottom: 100px;
        }}
        .header img {{
            max-width: 100px;
        }}
        .content {{
            margin-bottom: 100px;
        }}
        .content p {{
            margin: 30px 0;
        }}
        .footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 10;
            padding: 1px 20px;
            background-color: #f1f1f1;
        }}
        .footer img {{
            display: block;
            margin: 0px auto 20;
        }}
        .footer p {{
            margin: 0;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="images/customer.png" alt="costumer Logo" width="500" height="50">
            <h2>Lightning protection Risk management</h2><br><br>
            <p>Created according to international standard: IEC 62305-2:2010-12</p>
            <p>Considering the country-specific annexes for: IEC 62305-2:2010-12</p><br>
            <p><strong>Summary of measures for<br> reducing damage caused by lightning effects, <br>resulting from the risk management<br> concerning the following project:</strong></p>
        </div>
        <div class="content">
            <p><strong>Date:</strong> {tarih.strftime("%Y-%m-%d")}</p>
            <p><strong>Project No.:</strong> {proje_no}</p>
            <p><strong>Project / object description:</strong> {açıklama}</p>
            <p><strong>Customer / principal:</strong> {müşteri}</p>
            <p><strong>Risk assessment by:</strong> {yazar}</p>
        </div>
    </div>
    <div class="footer">
        <img src="images/logo.png" alt="Radsan Logo" width="80" height="35">
        <p>Radsan Risk Tools 1.0 - {tarih.strftime("%Y-%m-%d")}</p>
        <p>Page 1 of 19</p>
    </div>
</body>
</html>
"""
html_content_7 = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Risk Analysis for Assessing the Risk for Structures</title>
    <style>
        body {{
            font-family: Arial, sans-serif; /* Sayfadaki yazı tipini Arial olarak ayarlar, Arial mevcut değilse sans-serif kullanılır */
            display: flex; /* Flexbox düzeni kullanarak öğeleri hizalar */
            flex-direction: column; /* Flex öğelerinin dikey olarak yerleşmesini sağlar */
            min-height: 100vh; /* Sayfanın en az yüksekliğini ekran yüksekliği kadar yapar */
            margin: 0; /* Varsayılan margin değerlerini sıfırlar */
        }}

        
        .section {{
            flex: 1; /* İçeriğin kalan alanı kaplamasını sağlar
            margin-bottom: 20px;
        }}
        .subsection {{
            margin-left: 20px;
            margin-bottom: 10px;
        }}
        .risk-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }}
        .risk-table th, .risk-table td {{
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }}
        .risk-table th {{
            background-color: #f2f2f2;
        }}
        .footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 10;
            padding: 1px 20px; /* İç boşlukları belirler */
            background-color: #f1f1f1;
        }}
        .footer img {{
            display: block; /* Resmi blok eleman olarak gösterir, böylece margin ayarları doğru şekilde uygulanır */
            margin: 0px auto 20; /* Resmin üstüne 20px boşluk ekler, yatayda ortalar ve altta boşluk bırakmaz */
        }}
        .footer p {{
            margin: 0; /* Footer içindeki paragrafların marginlerini sıfırlar */
        }}
    </style>
</head>
<body>

    <div class="section">
        <h2>4. Project data</h2>

        <div class="subsection">
            <h3>4.1 Selection of risks to be considered</h3>
            <p>Due to the type and use of the structure, object WATER STORAGE MEKKE, the following risks were selected and considered:</p>
            <table class="risk-table">
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

        <div class="subsection">
            <h3>4.2 Geographic and building parameters</h3>
            <p>The ground flash density Ng is the basis for a risk analysis according to IEC 62305-2:2010-12. It defines the number of direct lightning strikes in 1 year / km². A value of 2,00 lightning strikes / year / km² was determined for the location of the object STEEL WATER STORAGES IN MOASIM/MAKKAH by means of the ground flash density map. As a result, there is a calculated number of 20,00 of thunderstorm days per year for the location of the project.</p>
            <p>The dimensions of the building are decisive for the risk of a direct strike. The collection areas for direct / indirect lightning strikes are determined based on these dimensions. The structure STEEL WATER STORAGES IN MOASIM/MAKKAH has the following dimensions:</p>
            <p>L<sub>b</sub> Length: 110,00 m</p>
            <p>W<sub>b</sub> Width: 110,00 m</p>
        </div>
    </div>
    <div class="footer">
        <img src="images/logo.png" alt="Radsan Logo" width="80" height="35">
        <p>Radsan Risk Tools 1.0 - {tarih.strftime("%Y-%m-%d")}</p>
        <p>Page 1 of 19</p>
    </div>
</body>
</html>



"""
# Dizin ve dosya adı
dizin_yolu = "output_pdf"
dosya_adı = f"{müşteri.lower().replace(' ', '_')}_risk_analiz_raporu.html"
tam_yol = os.path.join(dizin_yolu, dosya_adı)

# Eğer dizin mevcut değilse oluştur
if not os.path.exists(dizin_yolu):
    os.makedirs(dizin_yolu)

# HTML dosyasını oluştur ve yaz
with open(tam_yol, "w", encoding="utf-8") as file:
    file.write(html_content_7)

print(f"{tam_yol} dosyası başarıyla oluşturuldu.")
