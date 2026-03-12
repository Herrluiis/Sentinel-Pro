import numpy as np

class SentinelAI:
    def __init__(self):
        self.threshold = 0.85 # Nivel de confianza para detectar ataques
        print("[SISTEMA] Motor de IA Sentinel cargado y operativo.")

    def analizar_paquete(self, entropia, frecuencia):
        # Lógica de detección: si el tráfico es errático, se marca como amenaza
        score = (entropia * 0.7) + (frecuencia * 0.3)
        return score > self.threshold

    def analizar_trafico(self):
        # Esta función la usa el servidor web para mostrar el estado
        return "SISTEMA PROTEGIDO POR IA SENTINEL"
