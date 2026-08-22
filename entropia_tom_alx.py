import os
import sys

def inicializar_vinculacion_entropia():
    print("[Kempromed System] Conectando tom-alx con motor de entropía y pasarelas cripto...")
    umbral_alto = 0.85
    umbral_bajo = 0.15
    print(f"Umbrales configurados -> Alto: {umbral_alto} | Bajo: {umbral_bajo}")

def evaluar_secuencia_automatica(valor_entropia, umbral_alto=0.85, umbral_bajo=0.15):
    if valor_entropia >= umbral_alto:
        print(f"[ALERTA] Entropía alta detectada ({valor_entropia}). Ejecutando secuencia de cobertura superior.")
        return "VENTA_AUTOMATICA"
    elif valor_entropia <= umbral_bajo:
        print(f"[ALERTA] Entropía baja detectada ({valor_entropia}). Ejecutando secuencia de acumulación inferior.")
        return "COMPRA_AUTOMATICA"
    else:
        print(f"[ESTABLE] Valor de entropía dentro del rango operativo ({valor_entropia}). Sin acciones.")
        return "ESPERA"

if __name__ == "__main__":
    inicializar_vinculacion_entropia()
    entropia_actual = 0.12
    evaluar_secuencia_automatica(entropia_actual)
