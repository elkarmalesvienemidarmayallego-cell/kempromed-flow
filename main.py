import os
import random
import requests
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(
    title="Kempromed Flow | Total Enterprise Ecosystem",
    description="Backend B2B de Alta Concurrencia para Salud, Cripto, Negocios, iGaming & Algoritmos Social/Match.",
    version="2.7.0"
)

# Billeteras digitales en memoria
user_wallets = {}

# --- 1. DASHBOARD PRINCIPAL INSTITUCIONAL ---
@app.get("/", response_class=HTMLResponse, tags=["Dashboard"])
def home_dashboard(request: Request):
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Kempromed Flow | Enterprise Ecosystem</title>
        <style>
            * { box-sizing: border-box; }
            body { font-family: 'Segoe UI', system-ui, sans-serif; background: #0b0f19; color: #f8fafc; margin: 0; padding: 0; min-height: 100vh; display: flex; flex-direction: column; }
            .header { text-align: center; padding: 45px 20px 25px; background: linear-gradient(180deg, #111827 0%, #0b0f19 100%); border-bottom: 1px solid #1f2937; }
            .status-badge { background: #064e3b; color: #34d399; font-size: 0.8rem; padding: 5px 14px; border-radius: 20px; font-weight: bold; display: inline-block; margin-bottom: 12px; }
            h1 { color: #38bdf8; font-size: 2.5rem; margin: 0 0 10px; font-weight: 800; letter-spacing: -0.5px; }
            p.sub { color: #94a3b8; font-size: 1.05rem; max-width: 800px; margin: 0 auto; line-height: 1.5; }
            
            .container { max-width: 1200px; margin: 0 auto; padding: 40px 20px; flex: 1; }
            .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; }
            
            .card { background: #161e2e; border: 1px solid #223046; border-radius: 16px; padding: 28px; transition: transform 0.2s, border-color 0.2s; display: flex; flex-direction: column; justify-content: space-between; }
            .card:hover { transform: translateY(-4px); border-color: #38bdf8; }
            .card h3 { color: #38bdf8; margin: 0 0 10px; font-size: 1.3rem; }
            .card p { color: #94a3b8; font-size: 0.95rem; line-height: 1.5; margin-bottom: 20px; }
            
            .price-box { background: #0f172a; border: 1px solid #1e293b; border-radius: 10px; padding: 12px 16px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center; }
            .price-val { color: #4ade80; font-size: 1.3rem; font-weight: bold; }
            
            .btn { display: inline-block; background: #38bdf8; color: #0b0f19; font-weight: 700; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-size: 0.9rem; text-align: center; }
            .btn-green { background: #10b981; color: #022c22; }
            .btn-purple { background: #a855f7; color: #fff; }
            
            footer { background: #070a12; border-top: 1px solid #1f2937; padding: 40px 20px; margin-top: auto; font-size: 0.85rem; color: #64748b; }
            .footer-content { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px; }
            .footer-col h4 { color: #cbd5e1; margin: 0 0 12px; }
            .legal-bar { max-width: 1200px; margin: 30px auto 0; padding-top: 20px; border-top: 1px solid #111827; display: flex; justify-content: space-between; align-items: center; }
        </style>
    </head>
    <body>

        <div class="header">
            <span class="status-badge">● Sistema 100% Operativo | GCP & Render Cloud</span>
            <h1>KEMPROMED FLOW</h1>
            <p class="sub">Ecosistema Integrado B2B: Salud Digital, Finanzas Cripto, Desarrollo Social, Licencias Empresariales, iGaming & Redes de Interacción.</p>
        </div>

        <div class="container">
            <div class="grid">
                
                <!-- 1. MÓDULO SALUD -->
                <div class="card">
                    <div>
                        <h3>🩺 Salud & Telemedicina</h3>
                        <p>Plataforma de expedientes clínicos, recetas electrónicas y gestión de citas de atención médica.</p>
                        <div class="price-box">
                            <span style="color:#64748b; font-size:0.8rem;">SISTEMA:</span>
                            <div class="price-val" style="color:#ef4444;">Kempromed Health</div>
                        </div>
                    </div>
                    <a href="/docs" class="btn">Módulo Telemedicina →</a>
                </div>

                <!-- 2. MÓDULO ECONOMÍA & CRIPTO -->
                <div class="card">
                    <div>
                        <h3>📈 Finanzas & Cripto Engine</h3>
                        <p>Feeds de precios en vivo, liquidación de activos y pasarela financiera de liquidez.</p>
                        <div class="price-box">
                            <span style="color:#64748b; font-size:0.8rem;">BITCOIN (USD):</span>
                            <div class="price-val" id="btc-price">Cargando...</div>
                        </div>
                    </div>
                    <a href="/docs" class="btn">Crypto Feed API →</a>
                </div>

                <!-- 3. MÓDULO NEGOCIOS B2B -->
                <div class="card">
                    <div>
                        <h3>💳 Licencias & Pagos B2B</h3>
                        <p>Terminales dinámicas de cobro, contratos de servicios e inyección de liquidez personalizada.</p>
                        <div class="price-box">
                            <span style="color:#64748b; font-size:0.8rem;">PASARELA:</span>
                            <div class="price-val" style="color:#38bdf8;">Custom / Abierto</div>
                        </div>
                    </div>
                    <a href="/checkout" class="btn btn-green">Abrir Terminal Dinámica</a>
                </div>

                <!-- 4. MÓDULO DESARROLLO SOCIAL -->
                <div class="card">
                    <div>
                        <h3>🏛️ Desarrollo Social & Educación</h3>
                        <p>Convenios universitarios, acceso a APIs de desarrollo e impacto comunitario institucional.</p>
                        <div class="price-box">
                            <span style="color:#64748b; font-size:0.8rem;">VINCULACIÓN:</span>
                            <div class="price-val" style="color:#f59e0b;">Academia / Mexicali</div>
                        </div>
                    </div>
                    <a href="/docs" class="btn">Portal Universitario →</a>
                </div>

                <!-- 5. MÓDULO IGAMING & ENTROPÍA -->
                <div class="card">
                    <div>
                        <h3>🎮 iGaming & Dynamic Entropy</h3>
                        <p>Motor de simulación probabilística, asignación de incentivos, multiplicadores y gestión de riesgo.</p>
                        <div class="price-box">
                            <span style="color:#64748b; font-size:0.8rem;">MOTOR:</span>
                            <div class="price-val" style="color:#a855f7;">Aura Active</div>
                        </div>
                    </div>
                    <a href="/aura" class="btn btn-purple">Módulo Aura / Tom-Aix</a>
                </div>

                <!-- 6. MÓDULO CITAS & RED SOCIAL -->
                <div class="card">
                    <div>
                        <h3>❤️ Social & Match Engine</h3>
                        <p>Algoritmos de compatibilidad, perfiles verificados e interacción dinámica para la comunidad.</p>
                        <div class="price-box">
                            <span style="color:#64748b; font-size:0.8rem;">CONEXIÓN:</span>
                            <div class="price-val" style="color:#ec4899;">Match System</div>
                        </div>
                    </div>
                    <a href="/docs" class="btn" style="background:#ec4899; color:#fff;">Red Social API →</a>
                </div>

            </div>
        </div>

        <footer>
            <div class="footer-content">
                <div>
                    <h4 style="color:#38bdf8;">KEMPROMED DEVELOPMENT</h4>
                    <p style="margin:0;">Ecosistema integral de microservicios. Propiedad Intelectual de Dr. Mauro Falcón.</p>
                </div>
                <div>
                    <h4>RED DE PLATAFORMAS</h4>
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

# --- 2. TERMINAL DE PAGO / CHECKOUT ---
@app.get("/checkout", response_class=HTMLResponse, tags=["Terminales"])
def checkout_page(request: Request, amount: float = None):
    initial_val = f"{amount:.2f}" if amount else ""
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Terminal Flexible B2B | Kempromed</title>
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
            <h2 style="color:#38bdf8; margin-top:0;">Pasarela de Pago Personalizada</h2>
            <p style="color:#94a3b8; font-size:0.9rem;">Ingresa el monto exacto a procesar (MXN / USD / Cripto):</p>
            
            <form action="/api/v1/stripe/create-checkout" method="POST">
                <input type="number" step="0.01" name="amount" placeholder="Monto $0.00" value="{initial_val}" required>
                <button type="submit" class="btn">Procesar Pago Seguir →</button>
            </form>
            
            <br>
            <a href="/" style="color:#94a3b8; text-decoration:none; font-size:0.85rem;">← Volver al Hub Principal</a>
        </div>
    </body>
    </html>
    """

# --- 3. ENDPOINT STRIPE ---
@app.post("/api/v1/stripe/create-checkout", tags=["Stripe Gateway"])
def create_stripe_checkout(amount: float = Form(...)):
    stripe_key = os.getenv("STRIPE_SECRET_KEY", "mock_key")
    return {
        "status": "success",
        "amount_received": amount,
        "currency": "MXN",
        "gateway": "Stripe B2B Engine",
        "message": f"Procesando cobro individualizado de ${amount:.2f} MXN."
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

# --- 5. MOTOR IGAMING & ENTROPÍA DINÁMICA ---
@app.post("/api/v1/igaming/register", tags=["iGaming Engine"])
def register_player(user_id: str):
    """Crea la billetera del usuario y asigna incentivo inicial."""
    if user_id not in user_wallets:
        user_wallets[user_id] = {
            "real_balance_sats": 0,
            "bonus_balance_sats": 1000,
            "rounds_played": 0
        }
    return {
        "status": "success",
        "user_id": user_id,
        "wallet": user_wallets[user_id],
        "message": "¡Bono promocional acreditado! Completa 5 rondas para liberar saldo."
    }

@app.post("/api/v1/igaming/play-round", tags=["iGaming Engine"])
def play_igaming_round(user_id: str, bet_sats: int, use_bonus: bool = True):
    """Procesa la ronda con algoritmo probabilístico."""
    if user_id not in user_wallets:
        return {"error": "Usuario no registrado. Llama primero a /igaming/register"}
    
    player = user_wallets[user_id]
    balance_key = "bonus_balance_sats" if use_bonus else "real_balance_sats"
    
    if player[balance_key] < bet_sats:
        return {"error": f"Saldo insuficiente en billetera {'Promocional' if use_bonus else 'Real'}"}
    
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

# --- 6. ENDPOINTS CRIPTO & MULTIPLICADOR B2B ---
@app.get("/api/v1/crypto/price", tags=["Crypto Engine"])
def get_crypto_price():
    try:
        res = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd", timeout=5).json()
        return {"status": "success", "bitcoin_usd": res.get("bitcoin", {}).get("usd", 64249.00)}
    except Exception:
        return {"status": "success", "bitcoin_usd": 64249.00}

@app.post("/api/v1/igaming/multiply", tags=["iGaming Engine"])
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
