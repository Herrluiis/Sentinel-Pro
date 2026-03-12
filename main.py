from flask import Flask, render_template_string, request
import datetime

app = Flask(__name__)

# Datos de Luis Herrera
TITULAR = "Luis Herrera"
MI_WHATSAPP = "524774132965"

@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sentinel Pro | Luis Herrera</title>
        <style>
            body { background: #000; color: #0f0; font-family: 'Courier New', monospace; text-align: center; margin: 0; padding: 20px; }
            .container { max-width: 600px; margin: auto; border: 2px solid #0f0; padding: 20px; border-radius: 10px; box-shadow: 0 0 20px #0f0; }
            #console { background: #050505; color: #0f0; text-align: left; padding: 15px; height: 150px; overflow-y: hidden; border: 1px solid #050; margin: 20px 0; font-size: 0.8em; }
            .btn { color: #000; background: #0f0; text-decoration: none; padding: 15px; display: block; font-weight: bold; border-radius: 5px; animation: pulse 2s infinite; }
            @keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(0, 255, 0, 0.7); } 70% { box-shadow: 0 0 0 15px rgba(0, 255, 0, 0); } 100% { box-shadow: 0 0 0 0 rgba(0, 255, 0, 0); } }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🛡️ SENTINEL PRO v1.0</h1>
            <p>Architect: <b>{{ titular }}</b></p>
            <div id="console"></div>
            <p>ESTADO: <span id="status">INICIANDO ESCANEO...</span></p>
            <a href="/comprar/bank-killer" class="btn">ADQUIRIR LICENCIA BANK-KILLER</a>
        </div>
        <script>
            const lines = [
                "> Iniciando Sentinel Pro...",
                "> Cargando módulos de IA...",
                "> Bypass Cloudflare exitoso...",
                "> Analizando vulnerabilidades en sector financiero...",
                "> Encriptando túnel de salida...",
                "> Conexión lista con Luis Herrera.",
                "> Esperando comando de usuario..."
            ];
            let i = 0;
            function type() {
                const c = document.getElementById('console');
                if (i < lines.length) {
                    c.innerHTML += lines[i] + "<br>";
                    i++;
                    setTimeout(type, 1000);
                }
            }
            type();
        </script>
    </body>
    </html>
    """, titular=TITULAR)

@app.route('/comprar/bank-killer')
def comprar():
    msg = "Hola Luis Herrera, quiero adquirir la licencia Bank-Killer de Sentinel Pro."
    url = f"https://wa.me/{MI_WHATSAPP}?text={msg.replace(' ', '%20')}"
    return render_template_string('<script>window.location.href="{{ url }}";</script>', url=url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
