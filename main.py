from flask import Flask, render_template_string, request
import datetime

app = Flask(__name__)

# Configuración de Luis Herrera
TITULAR = "Luis Herrera"
PLANES = {
    "bank-killer": {"nombre": "Bank-Killer", "precio": 10000}
}

@app.route('/')
def home():
    # Este bloque HTML es lo que Google lee para ponerte en el buscador
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Sentinel Pro | Luis Herrera Ciberseguridad</title>
        <meta name="description" content="Servicios de Firewall e IA por Luis Herrera. Sentinel Pro: Protección total.">
        <meta name="keywords" content="Luis Herrera, Sentinel Pro, Ciberseguridad, Termux, Firewall">
        <style>
            body { background: #000; color: #0f0; font-family: monospace; text-align: center; }
            .box { border: 2px solid #0f0; padding: 20px; display: inline-block; margin-top: 100px; }
            a { color: #fff; text-decoration: none; border: 1px solid #fff; padding: 10px; }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🛡️ SENTINEL PRO OPERATIVO</h1>
            <p>Desarrollado por: <b>{{ titular }}</b></p>
            <p>Estado: SISTEMA PROTEGIDO POR IA</p>
            <br>
            <a href="/comprar/bank-killer">ADQUIRIR PLAN BANK-KILLER ($10,000)</a>
        </div>
    </body>
    </html>
    """, titular=TITULAR)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
