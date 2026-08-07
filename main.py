import os
import random
import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(
    title="Kempromed Flow Engine",
    description="Backend de microservicios B2B, APIs Cripto y Plataforma de Cobro",
    version="1.1.0"
)

# --- 1. MÓDULO DE PRECIOS CRIPTO EN VIVO ---
@app.get("/api/v1/crypto/price", tags=["Crypto"])
def get_btc_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        res = requests.get(url, timeout=5).json()
        price = res.get("bitcoin", {}).get("usd", 0.0)
        return {"status": "success", "bitcoin_usd": price}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# --- 2. MOTOR DE MULTIPLICACIÓN / CASINO (100 PESOS MXN) ---
@app.post("/api/v1/casino/multiply", tags=["Casino Engine"])
def multiply_balance(user_id: str, amount_mxn: float):
    if amount_mxn < 10:
        return {"error": "El monto mínimo para procesar es $10.00 MXN"}
    
    multipliers = [0, 0, 1.2, 1.5, 2.0, 3.0, 5.0]
    hit = random.choice(multipliers)
    final_amount = amount_mxn * hit
    
    return {
        "user_id": user_id,
        "initial_deposit_mxn": amount_mxn,
        "multiplier": f"{hit}x",
        "final_balance_mxn": final_amount,
        "profit_mxn": final_amount - amount_mxn,
        "status": "WIN" if hit > 1 else "LOSS"
    }

# --- 3. TERMINAL DE PAGO / CHECKOUT (Soluciona el Error 500) ---
@app.get("/checkout", response_class=HTMLResponse, tags=["Terminales"])
def checkout_page(request: Request):
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Terminal de Cobro B2B | Kempromed Flow</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0b0f19; color: #f8fafc; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
            .card { background: #161e2e; border: 1px solid #223046; border-radius: 16px; padding: 40px; max-width: 480px; width: 90%; box-shadow: 0 10px 25px rgba(0,0,0,0.5); text-align: center; }
            h2 { color: #38bdf8; margin-top: 0; font-size: 1.8rem; }
            .badge { background: #064e3b; color: #34d399; font-size: 0.85rem; padding: 4px 12px; border-radius: 20px; font-weight: bold; display: inline-block; margin-bottom: 20px; }
            .amount-box { background: #0f172a; border: 1px dashed #334155; border-radius: 12px; padding: 20px; margin: 20px 0; }
            .amount { font-size: 2.2rem; font-weight: bold; color: #4ade80; }
            .btn { background: #10b981; color: #022c22; font-weight: bold; padding: 14px 28px; border-radius: 10px; text-decoration: none; display: block; font-size: 1rem; transition: all 0.2s ease; margin-top: 20px; }
            .btn:hover { background: #34d399; transform: translateY(-2px); }
            .footer-note { font-size: 0.8rem; color: #64748b; margin-top: 25px; }
        </style>
    </head>
    <body>
        <div class="card">
            <span class="badge">● Terminal Activa 24/7</span>
            <h2>Pasarela B2B & Licencias</h2>
            <p style="color: #94a3b8; font-size: 0.95rem;">Selecciona el monto de inyección de liquidez para tu módulo de software o cuenta.</p>
            
            <div class="amount-box">
                <span style="color: #94a3b8; font-size: 0.85rem;">MONTO DE ENTRADA:</span>
                <div class="amount">$100.00 MXN</div>
                <span style="color: #38bdf8; font-size: 0.8rem;">~5.00 USDT / Cripto Equivalente</span>
            </div>

            <a href="/docs" class="btn">Procesar Transacción en API →</a>
            
            <div class="footer-note">
                Sincronizado con Render Cloud, SPEI y Polygon Network Engine.<br>
                © 2026 Kempromed Development.
            </div>
        </div>
    </body>
    </html>
    """

# --- 4. RUTA AURA (Soluciona el Error 404) ---
@app.get("/aura", response_class=HTMLResponse, tags=["Terminales"])
def aura_engine(request: Request):
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Aura Quantum Engine | Kempromed</title>
        <style>
            body { font-family: sans-serif; background: #020617; color: #38bdf8; text-align: center; padding: 50px; }
            .box { border: 1px solid #1e293b; background: #0f172a; padding: 30px; border-radius: 12px; display: inline-block; }
            a { color: #4ade80; text-decoration: none; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>⚡ Módulo Aura Active</h1>
            <p style="color: #94a3b8;">Motor asíncrono de procesamiento en tiempo real ejecutándose en la nube.</p>
            <br>
            <a href="/">← Regresar al Portal Principal</a>
        </div>
    </body>
    </html>
    """
