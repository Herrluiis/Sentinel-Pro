from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    mensaje = (f"Hola {user}, bienvenido a la Central de Sentinel Pro.\n\n"
               "🛡️ EL FIREWALL MÁS POTENTE DEL MERCADO.\n"
               "✅ Supera seguridad bancaria.\n"
               "✅ IA de detección proactiva.\n\n"
               "Escribe /precios para ver las licencias disponibles.")
    await update.message.reply_text(mensaje)

async def precios(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu = ("💎 LICENCIAS DISPONIBLES:\n"
            "1. Starter (1 Nodo): $500 USD\n"
            "2. Enterprise (10 Nodos): $3,500 USD\n"
            "3. Bank-Killer (Ilimitado): $10,000 USD\n\n"
            "Para comprar, contacta al administrador @TuUsuario.")
    await update.message.reply_text(menu)

if __name__ == '__main__':
    # Aquí pondremos el TOKEN que te da @BotFather
    app = ApplicationBuilder().token("TU_TOKEN_AQUI").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("precios", precios))
    print("[VENTAS] Bot de Sentinel Pro activo y buscando clientes...")
    app.run_polling()
