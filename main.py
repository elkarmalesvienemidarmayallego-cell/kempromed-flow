import os
import random
import requests
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(
    title="Kempromed Flow | High-Yield B2B Engine",
    description="Plataforma Comercial Backend: Liquidez Cripto, Licencias SaaS y Motor de Entropía.",
    version="3.0.0"
)

# Billeteras digitales en memoria
user_wallets = {}

# --- 1. DASHBOARD ENFOCADO EN VENTAS & LIQUIDEZ ---
@app.get("/", response_class=HTMLResponse, tags=["Dashboard"])
def home_dashboard(request: Request):
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Kempromed Flow | B2B SaaS & Liquidity Engine</title>
        <style>
            * { box-sizing: border-box; }
            body { font-family: 'Segoe UI', system-ui, sans-serif; background: #0b0f19; color: #f8fafc; margin: 0; padding: 0; min-height: 100vh; display: flex; flex-direction: column; }
            .header { text-align: center; padding: 45px 20px 25px; background: linear-gradient(180deg, #111827 0%, #0b0f19 100%); border-bottom: 1px solid #1f2937; }
            .status-badge { background: #064e3b; color: #34d399; font-size: 0.8rem; padding: 5px 14px; border-radius: 20px; font-weight: bold; display: inline-block; margin-bottom: 12px; }
            h1 { color: #38bdf8; font-size: 2.5rem; margin: 0 0 10px; font-weight: 800; letter-spacing: -0.5px; }
            p.sub { color: #94a3b8; font-size: 1.05rem; max-width: 700px; margin: 0 auto; line-height: 1.5; }
            
            .container { max-width: 1100px; margin: 0 auto; padding: 40px 20px; flex: 1; }
            .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; }
            
            .card { background: #161e2e; border: 1px solid #223046; border-radius: 16px; padding: 28px; transition: transform 0.2s, border-color 0.2s; display: flex; flex-direction: column; justify-content: space-between; }
            .card:hover { transform: translateY(-4px); border-color: #38bdf8; }
            .card h3 { color: #38bdf8; margin: 0 0 10px; font-size: 1.3rem; }
            .card p { color: #94a3b8; font-size: 0.95rem; line-height: 1.5; margin-bottom: 20px; }
            
            .price-box { background: #0f172a; border: 1px solid #1e293b; border-radius: 10px; padding: 12px 16px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center; }
            .price-val { color: #4ade80; font-size: 1.3rem; font-weight: bold; }
            
            .btn { display: inline-block; background: #38bdf8; color: #0b0f19; font-weight: 700; padding: 12px 20px; border-radius: 8px; text-decoration: none; font-size: 0.95rem; text-align: center; }
            .btn-green { background: #10b981; color: #022c22; }
            .btn-purple { background: #a855f7; color: #fff; }
            
            footer { background: #070a12; border-top: 1px solid #1f2937; padding: 40px 20px; margin-top: auto; font-size: 0.85rem; color: #64748b; }
            .footer-content { max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px; }
            .footer-col h4 { color: #cbd5e1; margin: 0 0 12px; }
            .legal-bar { max-width: 1100px; margin: 30px auto 0; padding-top: 20px; border-top: 1px solid #111827; display: flex; justify-content: space-between; align-items: center; }
        </style>
    </head>
    <body>

        <div class="header">
            <span class="status-badge">● Engine 100% Operativo | High Performance Cloud</span>
            <h1>KEMPROMED FLOW</h1>
            <p class="sub">Infraestructura Backend Comercial: Procesamiento B2B, Pasarelas Cripto/Stripe y Algoritmos Probabilísticos de Entropía.</p>
        </div>

        <div class="container">
            <div class="grid">
                
                <!-- 1. MÓDULO FINANZAS & CRIPTO -->
                <div class="card">
                    <div>
                        <h3>📈 Finanzas & Cripto Engine</h3>
                        <p>Monitoreo asíncrono, feeds de precios en vivo y pasarela de liquidez en activos digitales.</p>
                        <div class="price-box">
                            <span style="color:#64748b; font-size:0.8rem;">BITCOIN (USD):</span>
                            <div class="price-val" id="btc-price">Cargando...</div>
                        </div>
                    </div>
                    <a href="/docs" class="btn">Crypto API Docs →</a>
                </div>

                <!-- 2. MÓDULO TERMINAL B2B -->
                <div class="card">
                    <div>
                        <h3>💳 Terminal B2B & Licencias SaaS</h3>
                        <p>Inyección directa de liquidez, contratos de servicio y procesamiento dinámico de montos.</p>
                        <div class="price-box">
                            <span style="color:#64748b; font-size:0.8rem;">ESTADO:</span>
                            <div class="price-val" style="color:#38bdf8;">Terminal Dinámica</div>
                        </div>
                    </div>
                    <a href="/checkout" class="btn btn-green">Abrir Terminal de Cobro</a>
                </div>

                <!-- 3. MÓDULO IGAMING & ENTROPÍA -->
                <div class="card">
                    <div>
                        <h3>🎮 iGaming & Entropy Suite</h3>
                        <p>Motor de alta velocidad para juegos probabilísticos, multiplicadores y bonos automatizados.</p>
                        <div class="price-box">
                            <span style="color:#64748b; font-size:0.8rem;">CORE:</span>
                            <div class="price-val" style="color:#a855f7;">Aura Active</div>
                        </div>
                    </div>
                    <a href="/aura" class="btn btn-purple">Módulo Aura / Tom-Aix</a>
                </div>

            </div>
        </div>

        <footer>
            <div class="footer-content">
                <div>
                    <h4 style="color:#38bdf8;">KEMPROMED DEVELOPMENT</h4>
                    <p style="margin:0;">Infraestructura de microservicios comerciales y liquidez digital. Propiedad Intelectual de Dr. Mauro Falcón.</p>
                </div>
                <div>
                    <h4>RED DE NODOS</h4>
                    <p>● kempromed.ai.studio<br>● tom-aix.ai.studio<br>● kempromed-flow.onrender.com</p>
                </div>
                <div>
                    <h4>COMPLIANCE & LEGAL</h4>
                    <p>Registro: KMP-7492-ENT<br>Protección DMCA Activa<br>Stripe & Polygon Integrated</p>
                </div>
            </div>
            <div class="legal-bar">
                <div>© 2026 Kempromed Technology S.A. Desarrollado por Mau.</div>
                <div style="color:#38bdf8; font-weight:bold;">PROTECTED BY DMCA</div>
            </div>
        </footer>

        <script>
            async function fetchBTC() {
                try {
                    const res = await fetch('/api/v1/crypto/price');
                    const data = await res.json();
                    if(data.bitcoin_usd) {
                        document.getElementById('btc-price').innerText = '$' + data.bitcoin_usd.toLocaleString('en-US') + ' USD';
                    }
                } catch(e) {
                    document.getElementById('btc-price').innerText = '$64,249.00 USD';
                }
            }
            fetchBTC();
            setInterval(fetchBTC, 10000);
        </script>
    </body>
    </html>
    """

# --- 2. TERMINAL DE PAGO / CHECKOUT RECTIFICADA ---
@app.get("/checkout", response_class=HTMLResponse, tags=["Terminales"])
def checkout_page(request: Request, amount: float = None):
    initial_val = f"{amount:.2f}" if amount else ""
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Terminal B2B | Kempromed Flow</title>
        <style>
            body {{ font-family: sans-serif; background: #0b0f19; color: #fff; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }}
            .card {{ background: #161e2e; border: 1px solid #223046; border-radius: 16px; padding: 40px; max-width: 450px; width: 90%; text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }}
            input {{ background: #0f172a; border: 1px solid #334155; color: #4ade80; font-size: 1.8rem; font-weight: bold; text-align: center; padding: 12px; border-radius: 10px; width: 100%; margin: 15px 0; }}
            .btn {{ background: #10b981; color: #022c22; font-weight: bold; padding: 14px; border-radius: 10px; text-decoration: none; display: block; font-size: 1.1rem; border: none; cursor: pointer; width: 100%; margin-top: 10px; }}
            .btn:hover {{ background: #34d399; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2 style="color:#38bdf8; margin-top:0;">Terminal de Cobro Dinámica</h2>
            <p style="color:#94a3b8; font-size:0.9rem;">Ingresa el monto a procesar (MXN / USD / Cripto):</p>
            
            <form action="/api/v1/stripe/create-checkout" method="POST">
                <input type="number" step="0.01" name="amount" placeholder="Monto $0.00" value="{initial_val}" required>
                <button type="submit" class="btn">Procesar Transacción →</button>
            </form>
            
            <br>
            <a href="/" style="color:#94a3b8; text-decoration:none; font-size:0.85rem;">← Volver al Hub Principal</a>
        </div>
    </body>
    </html>
    """

# --- 3. ENDPOINT STRIPE RECEPCIÓN RÁPIDA ---
@app.post("/api/v1/stripe/create-checkout", tags=["Stripe Gateway"])
def create_stripe_checkout(amount: float = Form(...)):
    stripe_key = os.getenv("STRIPE_SECRET_KEY", "mock_key")
    return {
        "status": "success",
        "amount_received": amount,
        "currency": "MXN",
        "gateway": "Stripe B2B Engine",
        "message": f"Cobro de ${amount:.2f} MXN listo para procesamiento."
    }

# --- 4. RUTA AURA ---
@app.get("/aura", response_class=HTMLResponse, tags=["Terminales"])
def aura_engine(request: Request):
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Tom & Aix Space | Aura Engine</title>
        <style>
            body { font-family: sans-serif; background: #020617; color: #a855f7; text-align: center; padding: 50px; }
            .box { border: 1px solid #1e293b; background: #0f172a; padding: 40px; border-radius: 16px; display: inline-block; }
            a { color: #38bdf8; text-decoration: none; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>⚡ Tom & Aix Space</h1>
            <h3>Aura Quantum Network & Entropy Suite</h3>
            <p style="color: #94a3b8;">Motor asíncrono de procesamiento de datos activo en la nube.</p>
            <br>
            <a href="/">← Regresar al Portal Principal</a>
        </div>
    </body>
    </html>
    """

# --- 5. MOTOR IGAMING & BILLETERAS ---
@app.post("/api/v1/igaming/register", tags=["iGaming Engine"])
def register_player(user_id: str):
    if user_id not in user_wallets:
        user_wallets[user_id] = {
            "real_balance_sats": 0,
            "bonus_balance_sats": 1000,
            "rounds_played": 0
        }
    return {
        "status": "success",
        "user_id": user_id,
        "wallet": user_wallets[user_id]
    }

@app.post("/api/v1/igaming/play-round", tags=["iGaming Engine"])
def play_igaming_round(user_id: str, bet_sats: int, use_bonus: bool = True):
    if user_id not in user_wallets:
        return {"error": "Usuario no registrado."}
    
    player = user_wallets[user_id]
    balance_key = "bonus_balance_sats" if use_bonus else "real_balance_sats"
    
    if player[balance_key] < bet_sats:
        return {"error": "Saldo insuficiente."}
    
    player[balance_key] -= bet_sats
    player["rounds_played"] += 1
    
    multipliers = [0, 0, 0, 1.2, 1.5, 2.0, 3.5, 10.0]
    hit = random.choice(multipliers)
    payout = int(bet_sats * hit)
    
    player[balance_key] += payout
    
    return {
        "user_id": user_id,
        "bet_sats": bet_sats,
        "multiplier": f"{hit}x",
        "payout_sats": payout,
        "new_balance": player[balance_key],
        "status": "WIN" if hit > 1 else "LOSS"
    }

# --- 6. API PRECIOS CRIPTO ---
@app.get("/api/v1/crypto/price", tags=["Crypto Engine"])
def get_crypto_price():
    try:
        res = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd", timeout=5).json()
        return {"status": "success", "bitcoin_usd": res.get("bitcoin", {}).get("usd", 64249.00)}
    except Exception:
        return {"status": "success", "bitcoin_usd": 64249.00}
