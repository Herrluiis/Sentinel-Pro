import uuid

def generar_orden(plan, precio):
    # Genera un ID de transacción único para el cliente
    order_id = str(uuid.uuid4())[:8]
    print(f"[PAGOS] Generando orden {order_id} por ${precio} USD")
    
    # Aquí es donde se conectaría con la API de tu banco o wallet
    enlace_pago = f"https://gateway.sentinelpro.com/pay/{order_id}"
    
    return order_id, enlace_pago

# Ejemplo de uso:
# id, link = generar_orden("Bank-Killer", 10000)
