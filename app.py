from flask import Flask, render_template, request, redirect, url_for
import qrcode
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        link = request.form['link']
        if link:
            # Generar el código QR
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(link)
            qr.make(fit=True)

            # Crear y guardar la imagen
            img = qr.make_image(fill='black', back_color='white')
            img_path = 'static/codigo_qr.png'  # Guarda la imagen en una carpeta estática
            img.save(img_path)

            return render_template('index.html', img_path=img_path)

    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True)
