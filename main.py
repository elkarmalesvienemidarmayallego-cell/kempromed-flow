import os
import random
import requests
import stripe
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse

app = FastAPI(
    title="Kempromed Flow | High-Yield B2B Engine",
    description="Plataforma Comercial Backend: Liquidez Cripto, Licencias SaaS y Motor de Entropía.",
    version="3.0.0"
)

# Inicializar Stripe con la variable de entorno
STRIPE_KEY = os.getenv("STRIPE_SECRET_KEY", "")
if STRIPE_KEY:
    stripe.api_key = STRIPE_KEY

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

# --- 2. TERMINAL DE PAGO / CHECKOUT ---
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
            <p style="color:#94a3b8; font-size:0.9rem;">Ingresa el monto a procesar (MXN):</p>
            
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

# --- 3. REDIRECCIÓN A STRIPE CHECKOUT OFICIAL ---
@app.post("/api/v1/stripe/create-checkout", tags=["Stripe Gateway"])
def create_stripe_checkout(amount: float = Form(...)):
    if not stripe.api_key:
        return JSONResponse(status_code=400, content={"error": "Falta configurar STRIPE_SECRET_KEY en Render."})
    
    try:
        # Convertir monto a centavos para Stripe (ejemplo: $1000.00 -> 100000)
        amount_cents = int(amount * 100)
        
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'mxn',
                    'product_data': {
                        'name': 'Inyección de Liquidez / Licencia SaaS',
                        'description': 'Servicios Digitales Kempromed Flow',
                    },
                    'unit_amount': amount_cents,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://kempromed-flow.onrender.com/?payment=success',
            cancel_url='https://kempromed-flow.onrender.com/checkout',
        )
        return RedirectResponse(url=session.url, status_code=303)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

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
@app.get("/", response_class=HTMLResponse)
def serve_kempromed_flow_landing():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Kempromed Flow | Engine 100% Operativo</title>
        <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    </head>
    <body class="bg-slate-950 text-slate-100 min-h-screen font-sans">
        
        <div class="max-w-4xl mx-auto p-6 space-y-8">
            <!-- Header Institutional -->
            <header class="flex justify-between items-center border-b border-slate-800 pb-6">
                <div>
                    <span class="text-xs font-mono text-cyan-400 tracking-widest">KEMPROMED FLOW</span>
                    <h1 class="text-2xl md:text-3xl font-extrabold text-white mt-1">ENGINE 100% OPERATIVO</h1>
                </div>
                <div class="flex items-center gap-2 bg-emerald-950/50 border border-emerald-800 px-3 py-1.5 rounded-full">
                    <span class="w-2.5 h-2.5 bg-emerald-500 rounded-full animate-pulse"></span>
                    <span class="text-xs font-mono text-emerald-400 font-semibold">LIVE</span>
                </div>
            </header>

            <!-- Main Hero Card -->
            <div class="bg-gradient-to-b from-slate-900 to-slate-950 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
                <div class="absolute top-0 right-0 p-4 opacity-10 font-mono text-xs text-cyan-400">REF ORIGINAL</div>
                <p class="text-xs font-mono text-slate-400 mb-2">INFRAESTRUCTURA FINTECH B2B</p>
                
                <!-- Bitcoin Data Mock -->
                <div class="bg-slate-950/80 border border-slate-800/80 rounded-xl p-5 my-4">
                    <div class="flex justify-between items-center mb-2">
                        <span class="text-xs font-mono text-cyan-400 bg-cyan-950 px-2.5 py-1 rounded">01 — DATA ORACLE</span>
                        <span class="text-xs text-emerald-400 font-mono">+1.92% 24h</span>
                    </div>
                    <div class="text-3xl md:text-4xl font-black font-mono text-white my-2">$62,847.33</div>
                    <div class="text-xs text-slate-400 flex gap-4">
                        <span>VOL 28.48 USD</span>
                        <span>HIGH 63,210</span>
                        <span>LOW 61,442</span>
                    </div>
                </div>

                <!-- Specs Grid -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-6">
                    <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
                        <div class="text-xs text-slate-400 mb-1">UPTIME</div>
                        <div class="text-xl font-bold font-mono text-emerald-400">99.99%</div>
                        <div class="text-[10px] text-slate-500 mt-1">SLA Last 90d</div>
                    </div>
                    <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
                        <div class="text-xs text-slate-400 mb-1">LATENCY</div>
                        <div class="text-xl font-bold font-mono text-cyan-400">1.8ms</div>
                        <div class="text-[10px] text-slate-500 mt-1">p95 Edge</div>
                    </div>
                    <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
                        <div class="text-xs text-slate-400 mb-1">NODES ACTIVE</div>
                        <div class="text-xl font-bold font-mono text-purple-400">128</div>
                        <div class="text-[10px] text-slate-500 mt-1">Auto-scaled</div>
                    </div>
                </div>

                <!-- Call to Action -->
                <div class="mt-8 pt-6 border-t border-slate-800 flex flex-col md:flex-row justify-between items-center gap-4">
                    <p class="text-xs text-slate-400">Optimiza tu flujo financiero con infraestructura cloud de alto rendimiento.</p>
                    <a href="#contacto" class="w-full md:w-auto text-center bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold px-6 py-3 rounded-xl transition-all shadow-lg shadow-cyan-500/20">
                        ACCEDER AHORA →
                    </a>
                </div>
            </div>

            <!-- Footer specs -->
            <footer class="text-center text-xs font-mono text-slate-500 py-4 border-t border-slate-900">
                KEMPROMED FLOW • SPEC SHEET 2025 • Documentación técnica para inversores
            </footer>
        </div>
    </body>
    </html>
    """
