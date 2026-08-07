import os
import random
import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Kempromed Flow Engine",
    description="Backend de microservicios B2B, APIs Cripto y Plataforma de Cobro",
    version="1.1.0"
)

# --- 1. RUTA RAÍZ (LANDING PAGE PRINCIPAL) ---
@app.get("/", response_class=HTMLResponse, tags=["Dashboard"])
def home_dashboard(request: Request):
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Kempromed Flow | Developer Hub</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 40px 20px; text-align: center; }
            h1 { color: #38bdf8; font-size: 2.5rem; margin-bottom: 10px; }
            p { color: #94a3b8; font-size: 1.1rem; }
            .grid { display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-top: 40px; }
            .card { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 25px; width: 300px; text-align: left; }
            .card h3 { color: #34d399; margin-top: 0; }
            .btn { display: inline-block; background: #38bdf8; color: #0f172a; font-weight: bold; padding: 10px 20px; border-radius: 8px; text-decoration: none; margin-top: 15px; }
        </style>
    </head>
    <body>
        <h1>Kempromed Flow Engine</h1>
        <p>Hub Oficial de Microservicios, APIs Financieras y Plataformas Web</p>
        
        <div class="grid">
            <div class="card">
                <h3>💳 Pasarela & Licencias</h3>
                <p>Terminal de procesamiento B2B para cobros e inyección de liquidez.</p>
                <a href="/checkout" class="btn">Ir a Checkout</a>
            </div>
            <div class="card">
                <h3>⚡ Sistema Quantum</h3>
                <p>Motor asíncrono de procesamiento de datos en tiempo real.</p>
                <a href="/aura" class="btn">Ver Módulo Aura</a>
            </div>
            <div class="card">
                <h3>📖 Documentación API</h3>
                <p>Explora y prueba los endpoints interactivos en Swagger UI.</p>
                <a href="/docs" class="btn" style="background:#4ade80;">Swagger UI</a>
            </div>
        </div>
    </body>
    </html>
    """

# --- 2. TERMINAL DE PAGO / CHECKOUT ---
@app.get("/checkout", response_class=HTMLResponse, tags=["Terminales"])
def checkout_page(request: Request):
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Terminal de Cobro B2B | Kempromed Flow</title>
        <style>
            body { font-family: sans-serif; background: #0b0f19; color: #fff; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
            .card { background: #161e2e; border: 1px solid #223046; border-radius: 16px; padding: 40px; max-width: 450px; text-align: center; }
            .amount { font-size: 2.2rem; color: #4ade80; font-weight: bold; margin: 15px 0; }
            .btn { background: #10b981; color: #000; font-weight: bold; padding: 12px 24px; border-radius: 8px; text-decoration: none; display: inline-block; }
        </style>
    </head>
    <body>
        <div class="card">
            <h2 style="color:#38bdf8;">Pasarela B2B & Licencias</h2>
            <p>Monto de entrada:</p>
            <div class="amount">$100.00 MXN</div>
            <a href="/docs" class="btn">Procesar Transacción →</a>
            <br><br>
            <a href="/" style="color:#94a3b8; text-decoration:none;">← Volver al Hub</a>
        </div>
    </body>
    </html>
    """

# --- 3. RUTA AURA ---
@app.get("/aura", response_class=HTMLResponse, tags=["Terminales"])
def aura_engine(request: Request):
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Aura Engine | Kempromed</title>
        <style>
            body { font-family: sans-serif; background: #020617; color: #38bdf8; text-align: center; padding: 50px; }
            a { color: #4ade80; text-decoration: none; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1>⚡ Módulo Aura Active</h1>
        <p style="color: #94a3b8;">Motor asíncrono de procesamiento en vivo corriendo en Render.</p>
        <a href="/">← Regresar al Portal Principal</a>
    </body>
    </html>
    """

# --- 4. API DE MULTIPLICADOR / CASINO ---
@app.post("/api/v1/casino/multiply", tags=["Casino Engine"])
def multiply_balance(user_id: str, amount_mxn: float):
    multipliers = [0, 0, 1.2, 1.5, 2.0, 3.0, 5.0]
    hit = random.choice(multipliers)
    final_amount = amount_mxn * hit
    return {
        "user_id": user_id,
        "initial_deposit_mxn": amount_mxn,
        "multiplier": f"{hit}x",
        "final_balance_mxn": final_amount,
        "status": "WIN" if hit > 1 else "LOSS"
    }
